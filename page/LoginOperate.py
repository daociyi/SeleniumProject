import time
from PIL import Image
from selenium import webdriver

from base.BaseOperate import BaseOperate
from log.Log import Logger


class LoginPage(BaseOperate,Logger):
    def login(self,username,password):
        url = 'http://192.168.16.233:25046/#/login'
        self.open_url(url)
        self.html_zoom("document.body.style.zoom='0.8'")
        self.findItemInputViewt('//*[@id="login"]/div[3]/div[1]/div[2]/input',username)
        self.findItemInputViewt('//*[@id="login"]/div[3]/div[2]/div[2]/input',password)
        # tets = driver.find_element_by_xpath('//*[@id="login"]/div[3]/div[2]/div[2]/input').get_attribute("class")
        # print(tets)
        #获取当前url用于后面条件判断
        url = self.driver.current_url
        print(url)
        # wait = WebDriverWait(driver, 5)
            #对当前url进行判断，当current_url不等于url时才结束判断
        while  url ==self.driver.current_url:
            time.sleep(1)
            code = self.findElementByCssSelector('#vCanvas')
            #获取验证码图像元素的大小（x，y）
            location = code.location
            #获取验证码元素的尺寸（width，height）
            size = code.size
            #设置left用于获取验证码元素的x坐标
            left = location['x']
            #设置top用于获取验证码元素的y坐标
            top = location['y']
            #right为x坐标+尺寸的宽，也就是向右平移width个位置
            right = left + size['width']
            #height为y坐标+尺寸的高，也就是向下平移height个位置
            #这样就获得了另一个为（right，bottom）的坐标用于后续裁剪时使用
            bottom = top + size['height']
            #截图
            self.driver.save_screenshot('code.png')
            img = Image.open('code.png')
            #裁剪图片按照crop方法的点对点裁剪，按照对角线获取裁剪的图片大小
            img_crop = img.crop((left, top, right, bottom))
            #保存图片
            img_crop.save('code.png', 'png')
            #将图片放入识别验证码方法中
            codeNum = self.codeVerification(img)
            print(codeNum)
            #输入识别出的验证码
            self.findItemInputViewt('//*[@id="login"]/div[3]/div[3]/div[2]/input',codeNum)
            # driver.find_element_by_xpath('//*[@id="login"]/div[3]/div[3]/div[2]/input').send_keys(codeNum)
            # exp = ('xpath','//*[@id="login"]/div[3]/div[3]/div[2]/input')
            # wait.until(EC.text_to_be_present_in_element_value(exp,codeNum))
            # ptt = EC.text_to_be_present_in_element(exp,u'sadd')
            # print(ptt)
            time.sleep(1)
            self.clickDelay('//div[@id="login"]/div[3]/div[5]/button')
            #再获得一次current_url用于判断
            #如果url还是相同则清除输入的验证码，并更换新的验证码
            if url == self.driver.current_url:
                self.findElementByXPathClear('//*[@id="login"]/div[3]/div[3]/div[2]/input')
                # code_update =self.findElementByXPath('//*[@id="login"]/div[3]/div[3]/div[4]')
                # #使用运行脚本的方法执行点击事件
                # driver.execute_script("arguments[0].click()", code_update)
                self.clickDelay('//*[@id="login"]/div[3]/div[3]/div[4]')
            #如果url不同则跳过
            else:
                pass
            time.sleep(2)
        result = u"登录成功"
        print(u"登录成功")
        print(u"成功")
        return  result

if __name__ == '__main__':
    driver = webdriver.Chrome()
    lp = LoginPage(driver)
    lp.login("guanli","2022Standards")
    lp.quitBrowse()
