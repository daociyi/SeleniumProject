import time
from python.base import BaseOperate
from python.base.Config import driver
from PIL import Image



def login(username,password):
    # 中文需要加u，意思是编码UTF-8
    BaseOperate.findItemInputViewt('//*[@id="login"]/div[3]/div[1]/div[2]/input',username)
    BaseOperate.findItemInputViewt('//*[@id="login"]/div[3]/div[2]/div[2]/input',password)
    #获取当前url用于后面条件判断
    url = driver.current_url
        #对当前url进行判断，当current_url不等于url时才结束判断
    while  url ==driver.current_url:
        time.sleep(1)
        code = driver.find_element_by_css_selector('#vCanvas')
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
        driver.save_screenshot('code.png')
        img = Image.open('code.png')
        #裁剪图片按照crop方法的点对点裁剪，按照对角线获取裁剪的图片大小
        img_crop = img.crop((left, top, right, bottom))
        #保存图片
        img_crop.save('code.png', 'png')
        #将图片放入识别验证码方法中
        codeNum = BaseOperate.codeVerification(img)
        print(codeNum)
        #输入识别出的验证码
        driver.find_element_by_xpath('//*[@id="login"]/div[3]/div[3]/div[2]/input').send_keys(codeNum)
        time.sleep(1)
        BaseOperate.clickDelay('//*[@id="login"]/div[3]/div[5]/button')
        #再获得一次current_url用于判断
        driver.current_url
        #如果url还是相同则清除输入的验证码，并更换新的验证码
        if url == driver.current_url:
            BaseOperate.findElementByXPathClear('//*[@id="login"]/div[3]/div[3]/div[2]/input')
            # code_update =BaseOperate.findElementByXPath('//*[@id="login"]/div[3]/div[3]/div[4]')
            # #使用运行脚本的方法执行点击事件
            # driver.execute_script("arguments[0].click()", code_update)
            BaseOperate.clickDelay('//*[@id="login"]/div[3]/div[3]/div[4]')
        #如果url不同则跳过
        else:
            pass
        time.sleep(2)
    result = u"登录成功"
    print(u"登录成功")
    print(u"成功")
    return  result

