import time

import pytesseract
from PIL import Image
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

from log.Log import Logger


class BaseOperate():

    def __init__(self,driver,loggname):
    # def __init__(self,loggname):
    #     driver = webdriver.Chrome()
        self.logger = Logger(loggname)
        self.driver = driver
        self.driver.maximize_window()


    def html_zoom(self,size):
        self.driver.execute_script(size)

    def open_url(self,url):
        self.driver.get(url)

    def findElementByXPathClear(self,xpath):
        try:
            self.inputXPath1 = self.driver.find_element(By.XPATH,xpath)
            self.inputXPath1.clear()
            self.logger.getLog("清除{}".format(self.inputXPath1.get_attribute("placeholder")))
        except WebDriverException as e:
            self.logger.getErrorLog(str(e))

    def  findItemInputViewt(self,xpath,text):
        try:
            self.inputXPath2 = self.driver.find_element(By.XPATH,xpath)
            self.inputXPath2.send_keys(text)
            time.sleep(1)
            self.logger.getLog("输入{}".format(text))
        except WebDriverException as  e:
            self.logger.getErrorLog(str(e))

    def findElementByCssSelector(self,css_selector):
        self.css_picture = self.driver.find_element(By.CSS_SELECTOR,css_selector)
        return self.css_picture

    def getTextByClassName(self,classname):
        self.text = self.driver.find_element(By.CLASS_NAME,classname).text
        return self.text


    def clickDelay(self,xpath):
        clickXPath = self.driver.find_element(By.XPATH,xpath)
        self.driver.execute_script("arguments[0].click();",clickXPath)
        time.sleep(1)

    def clickDelay_by_list(self,list):
        self.driver.execute_script("arguments[0].click();",list)
        time.sleep(1)

    def listElementXPathAndClass(self,xpath,classname):
        self.list = self.driver.find_elements(By.XPATH,xpath)
        arrayList = self.list.__getitem__(0).find_elements(By.CLASS_NAME,classname)
        return  arrayList

    def listElementXPathAndLinktext(self,xpath,link_text):
        self.list = self.driver.find_elements(By.XPATH,xpath)
        arrayList = self.list.__getitem__(0).find_elements(By.LINK_TEXT,link_text)
        return  arrayList

    def codeVerification(self,img):
        img = Image.open('code.png')
        # 对图片进行灰度处理
        img = img.convert('L')
        x = img.width
        y = img.height
        # 获取图片每个像素的值，小于阈值的设置为黑色，大于则为白色
        for img_x in range(x):
            for img_y in range(y):
                if img.getpixel((img_x, img_y)) < 130:
                    img.putpixel((img_x, img_y), 0)
                else:
                    img.putpixel((img_x, img_y), 255)
        # 对图片进行降噪 ，去掉点干扰和线干扰
        for img_x in range(1, x - 1):
            if img_x >= 0 and img_x != (x - 2):
                img_x_left = img_x - 1
                img_x_right = img_x + 1
            for img_y in range(1, y - 1):
                # if  img_y>1 or img_y<(y-2):
                img_y_up = img_y - 1
                img_y_down = img_y + 1
                # if img_x <=19 or img_x>=(x-11):
                #     img.putpixel((img_x,img_y),255)
                # if img_y <=8 or img_y>=(y-10):
                #     img.putpixel((img_x,img_y),255)
                if img_y >= 0 and img_y != (y - 2):
                    # 中心点上，右，下，左
                    center_up = img.getpixel((img_x, img_y_up))
                    center_right = img.getpixel((img_x_right, img_y))
                    center_right_right = img.getpixel((img_x_right + 1, img_y))
                    center_down = img.getpixel((img_x, img_y_down))
                    center_down_down = img.getpixel((img_x, img_y_down + 1))
                    center_left = img.getpixel((img_x_left, img_y))
                    # 右上，右下，左上，左下
                    center_right_up = img.getpixel((img_x_right, img_y_up))
                    center_right_down = img.getpixel((img_x_right, img_y_down))
                    center_right_down_down = img.getpixel((img_x_right, img_y_down + 1))
                    center_left_up = img.getpixel((img_x_left, img_y_up))
                    center_left_down = img.getpixel((img_x_left, img_y_down))
                    center_left_down_down = img.getpixel((img_x_left, img_y_down + 1))
                    if img.getpixel((img_x, img_y)) == 0:
                        if center_left == 255:  # 0.先按照左边为白判断
                            if center_right == 0:
                                if center_right_right == 255:  # 1.再按照右边为黑，右右为白
                                    if center_left_down_down != 0 or center_right_down_down != 0:  # 2.再按照左下下不为黑 或者 右下下不为黑
                                        img.putpixel((img_x, img_y), 255)  # 取白
                                elif center_up == 255 and center_down == 255:
                                    img.putpixel((img_x, img_y), 255)
                            elif center_right == 255:  # 1.右边为白
                                if center_down == 255 and center_up == 255:  # 2.下白，上百
                                    img.putpixel((img_x, img_y), 255)  # 取白
                                elif center_up == 255:  # 2.上为白
                                    img.putpixel((img_x, img_y), 255)  # 取白
                                elif center_down == 255:  # 2.下为白
                                    img.putpixel((img_x, img_y), 255)  # 取白
                    else:
                        pass
        tesseract_dir = '--tesseract "D:\\Tesseract-OCR\\tessdata"'
        result = pytesseract.image_to_string(img,config=tesseract_dir)
        # 去除不相关标识符,用字典的方式 string代表查到的字符 replace_dict[string]为查到字符对应的替换
        code = ''
        for key in result:
            if key.isalnum():
                code += key
        if code.isspace():
            # 没识别出来返回空
            return "unknow"
        # 识别出来返回code
        else:
            return code

    def quitBrowse(self):
        self.driver.quit()

