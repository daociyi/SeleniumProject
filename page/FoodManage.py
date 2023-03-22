import random
import time

from selenium import webdriver

from base.BaseOperate import BaseOperate
from page.LoginOperate import LoginPage
class FoodPage(BaseOperate):
    def addFood(self,product):
        print(self.driver.current_window_handle)
        url = 'http://192.168.16.233:25046/#/foodManage'
        self.driver.implicitly_wait(2)

        self.open_url(url=url)
        self.clickDelay('/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/button[1]')
        num = random.randint(1,150)
        self.findItemInputViewt('//*[@id="accountRecordDetail"]/form/div[1]/div[3]/div/div[1]/input',num)
        self.clickDelay('//*[@id="accountRecordDetail"]/form/div[1]/div[4]/div/div/div/input')
        sup_li = self.listElementXPathAndClass('/html/body/div[3]/div[1]/div[1]/ul','el-select-dropdown__item')
        sup_num = random.randint(0,len(sup_li)-1)
        self.driver.execute_script("arguments[0].click();",sup_li[sup_num])
        self.clickDelay('//*[@id="accountRecordDetail"]/form/div[1]/div[5]/div/div/div/input')
        checkPerson_li = self.listElementXPathAndClass('/html/body/div[4]/div[1]/div[1]/ul','el-select-dropdown__item')
        checkPerson_num = random.randint(0,len(checkPerson_li)-1)
        self.clickDelay_by_list(checkPerson_li[checkPerson_num])
        self.findItemInputViewt('//*[@id="accountRecordDetail"]/form/div[1]/div[1]/div/div/div/input',product)
        self.findItemInputViewt('//*[@id="accountRecordDetail"]/form/div[4]/div[2]/div[1]/div/input',r"C:\Users\Administrator\Desktop\QQ截图20200616163201.png")
        self.clickDelay('//*[@id="accountRecordDetail"]/form/div[5]/button')
        result = u"新增台账完成"
        print(u"新增台账完成")
        return result

    def updateFood(self,update_product_name):
        url = 'http://218.6.70.66:25046/#/foodManage'
        self.open_url(url=url)
        time.sleep(2)
        record_list = self.listElementXPathAndLinktext('//*[@id="accountRecord"]/div[3]/table',"详细信息")
        record_list_num = random.randint(0,len(record_list)-1)
        self.clickDelay_by_list(record_list[record_list_num])
        num = random.randint(1,150)
        self.findElementByXPathClear('//*[@id="accountRecordDetail"]/form/div[1]/div[3]/div/div[1]/input')
        self.findItemInputViewt('//*[@id="accountRecordDetail"]/form/div[1]/div[3]/div/div[1]/input',num)
        self.clickDelay('//*[@id="accountRecordDetail"]/form/div[1]/div[4]/div/div/div/input')
        sup_li = self.listElementXPathAndClass('/html/body/div[3]/div[1]/div[1]/ul','el-select-dropdown__item')
        sup_num = random.randint(0,len(sup_li)-1)
        self.clickDelay_by_list(sup_li[sup_num])
        self.clickDelay('//*[@id="accountRecordDetail"]/form/div[1]/div[5]/div/div/div/input')
        checkPerson_li = self.listElementXPathAndClass('/html/body/div[4]/div[1]/div[1]/ul','el-select-dropdown__item')
        checkPerson_num = random.randint(0,len(checkPerson_li)-1)
        self.clickDelay_by_list(checkPerson_li[checkPerson_num])
        self.findElementByXPathClear('//*[@id="accountRecordDetail"]/form/div[1]/div[1]/div/div/div/input')
        self.findItemInputViewt('//*[@id="accountRecordDetail"]/form/div[1]/div[1]/div/div/div/input',update_product_name)
        self.clickDelay('//*[@id="accountRecordDetail"]/form/div[5]/button')
        # alert_resul = driver.find_element_by_class_name('el-message__content')
        # print(alert_resul.text)
        alert_result = self.getTextByClassName('el-message__content')
        # print(alert_result)
        # text = alert_result.text
        # print(text)
        # result = u"修改台账完成"
        # print(u"修改台账完成")
        return alert_result



    def addReserveSample(self,dish):
        # a = self.listElementXPathAndClass('/html/body/div/div/div[1]/header/ul','nav')
        # self.driver.execute_script("arguments[0].click();",a[2])
        self.open_url(url='http://218.6.70.66:25046/#/foodManage/sampleRetention')
        time.sleep(2)
        # li = self.listElementXPathAndClass('/html/body/div/div/div[2]/div[1]/div[1]/ul','el-menu-item')
        # self.driver.execute_script("arguments[0].click();",li[3])
        # time.sleep(2)
        # self.clickDelay('//*[@id="header"]/ul/a[3]')
        #
        # self.clickDelay('//*[@id="index"]/div[2]/div[1]/div[1]/ul/li[4]/span')
        self.clickDelay('//*[@id="sampleRetention"]/div[1]/div[2]/button[1]/span')
        self.clickDelay('//*[@id="sampleRetentionDetail"]/form/div[1]/div[2]/div/div/div/input')
        meal = self.listElementXPathAndClass('/html/body/div[3]/div[1]/div[1]/ul','el-select-dropdown__item')
        meal_num = random.randint(0,len(meal)-1)
        self.driver.execute_script("arguments[0].click();",meal[meal_num])

        # self.clickDelay('/html/body/div[2]/div[1]/div[1]/ul/li[1]/span')
        self.findItemInputViewt('//*[@id="sampleRetentionDetail"]/form/div[1]/div[3]/div/div/div/input',dish)


        self.clickDelay('//*[@id="sampleRetentionDetail"]/form/div[1]/div[5]/div/div/div[1]/input')
        person_li1 = self.listElementXPathAndClass('/html/body/div[4]/div[1]/div[1]/ul','el-select-dropdown__item')
        num1 = random.randint(0,len(person_li1)-1)
        self.driver.execute_script("arguments[0].click();",person_li1[num1])


        # self.clickDelay('/html/body/div[4]/div[1]/div[1]/ul/li[1]/span')


        self.clickDelay('//*[@id="sampleRetentionDetail"]/form/div[1]/div[7]/div/div/div/input')
        person_li2 = self.listElementXPathAndClass('/html/body/div[5]/div[1]/div[1]/ul','el-select-dropdown__item')
        num2 = random.randint(0,len(person_li2)-1)
        self.driver.execute_script("arguments[0].click();",person_li2[num2])

        # self.clickDelay('/html/body/div[5]/div[1]/div[1]/ul/li[1]/span')
        self.clickDelay('//*[@id="sampleRetentionDetail"]/form/div[2]/button')
        result = u"新增菜品留样完成"
        print(u"新增菜品留样完成")
        return  result


    def addDineRecord(self,person,indentity,evaluate):

        a = self.listElementXPathAndClass('/html/body/div/div/div[1]/header/ul','nav')
        self.driver.execute_script("arguments[0].click();",a[2])

        time.sleep(2)
        li = self.listElementXPathAndClass('/html/body/div/div/div[2]/div[1]/div[1]/ul','el-menu-item')
        self.driver.execute_script("arguments[0].click();",li[6])

        time.sleep(2)
        self.clickDelay('//*[@id="accompanyMealRecord"]/div[1]/div[2]/button[1]/span')
        self.clickDelay('//*[@id="personnelMsgDetail"]/form/div[1]/div[2]/div/div/div/input')
        self.clickDelay('/html/body/div[2]/div[1]/div[1]/ul/li[1]')

        self.clickDelay('//*[@id="personnelMsgDetail"]/form/div[1]/div[3]/div/div/div[1]/input')

        dish_li = self.listElementXPathAndClass('/html/body/div[3]/div[1]/div[1]/ul','el-select-dropdown__item')
        self.driver.execute_script("arguments[0].click();",dish_li[9])
        self.driver.execute_script("arguments[0].click();",dish_li[10])

        self.findItemInputViewt('//*[@id="personnelMsgDetail"]/form/div[1]/div[4]/div/div/input',person)
        self.findItemInputViewt('//*[@id="personnelMsgDetail"]/form/div[1]/div[5]/div/div/input',indentity)
        self.findItemInputViewt('//*[@id="personnelMsgDetail"]/form/div[1]/div[6]/div/div/input',evaluate)
        self.findItemInputViewt('//*[@id="personnelMsgDetail"]/form/div[2]/div/div[1]/div/input',r'C:\Users\Administrator\Desktop\QQ截图20200628150848.png')
        self.clickDelay('//*[@id="personnelMsgDetail"]/form/div[3]/button/span')
        print(u"新增陪餐完成")
        result = u"新增陪餐完成"
        return result
if __name__ == '__main__':
    driver = webdriver.Chrome()
    lg = LoginPage(driver)
    fg = FoodPage(driver)
    lg.login('tests','123456')
    fg.updateFood(u"小酥肉")
    # fg.addFood(u"老腊肉")
    # fg.addReserveSample(u"卤猪蹄")
    # fg.addDineRecord(u"小当家","特级厨师","好吃，还不错")
    # driver.close()
    # driver.quit()