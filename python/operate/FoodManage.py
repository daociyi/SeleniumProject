import random
import time

from selenium import webdriver

from python.base.BaseOperate import BaseOperate

from python.operate.LoginOperate import LoginPage
# from python.base.Config import driver
class FoodPage(BaseOperate):
    def addFood(self,product):
        print(self.driver.current_window_handle)
        url = 'http://218.6.70.66:25046/#/foodManage'
        driver.implicitly_wait(2)
        # a = BaseOperate.listElementXPathAndClass(self,'//*[@id="header"]/div[2]/div','nav')
        # self.driver.execute_script("arguments[0].click();",a[2])

        # print(a[2])
        # driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/a[3]').click()

        # BaseOperate.clickDelay(self,'//*[@id="header"]/div[2]/div/a[3]')
        BaseOperate.open_url(self,url=url)
        BaseOperate.clickDelay(self,'/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/button[1]')
        num = random.randint(1,150)
        BaseOperate.findItemInputViewt(self,'//*[@id="accountRecordDetail"]/form/div[1]/div[3]/div/div[1]/input',num)

        BaseOperate.clickDelay(self,'//*[@id="accountRecordDetail"]/form/div[1]/div[4]/div/div/div/input')
        sup_li = BaseOperate.listElementXPathAndClass(self,'/html/body/div[3]/div[1]/div[1]/ul','el-select-dropdown__item')

        sup_num = random.randint(0,len(sup_li)-1)
        self.driver.execute_script("arguments[0].click();",sup_li[sup_num])

        BaseOperate.clickDelay(self,'//*[@id="accountRecordDetail"]/form/div[1]/div[5]/div/div/div/input')
        checkPerson_li = BaseOperate.listElementXPathAndClass(self,'/html/body/div[4]/div[1]/div[1]/ul','el-select-dropdown__item')
        checkPerson_num = random.randint(0,len(checkPerson_li)-1)
        self.driver.execute_script("arguments[0].click();",checkPerson_li[checkPerson_num])



        BaseOperate.findItemInputViewt(self,'//*[@id="accountRecordDetail"]/form/div[1]/div[1]/div/div/div/input',product)
        BaseOperate.findItemInputViewt(self,'//*[@id="accountRecordDetail"]/form/div[4]/div[2]/div[1]/div/input',r"C:\Users\Administrator\Desktop\QQ截图20200616163201.png")
        BaseOperate.clickDelay(self,'//*[@id="accountRecordDetail"]/form/div[5]/button')
        result = u"新增台账完成"
        print(u"新增台账完成")
        return result

    def addReserveSample(self,dish):
        # a = BaseOperate.listElementXPathAndClass(self,'/html/body/div/div/div[1]/header/ul','nav')
        # self.driver.execute_script("arguments[0].click();",a[2])
        BaseOperate.open_url(self,url='http://218.6.70.66:25046/#/foodManage/sampleRetention')
        time.sleep(2)
        # li = BaseOperate.listElementXPathAndClass(self,'/html/body/div/div/div[2]/div[1]/div[1]/ul','el-menu-item')
        # self.driver.execute_script("arguments[0].click();",li[3])
        # time.sleep(2)
        # BaseOperate.clickDelay('//*[@id="header"]/ul/a[3]')
        #
        # BaseOperate.clickDelay('//*[@id="index"]/div[2]/div[1]/div[1]/ul/li[4]/span')
        BaseOperate.clickDelay(self,'//*[@id="sampleRetention"]/div[1]/div[2]/button[1]/span')
        BaseOperate.clickDelay(self,'//*[@id="sampleRetentionDetail"]/form/div[1]/div[2]/div/div/div/input')
        meal = BaseOperate.listElementXPathAndClass(self,'/html/body/div[3]/div[1]/div[1]/ul','el-select-dropdown__item')
        meal_num = random.randint(0,len(meal)-1)
        self.driver.execute_script("arguments[0].click();",meal[meal_num])

        # BaseOperate.clickDelay('/html/body/div[2]/div[1]/div[1]/ul/li[1]/span')
        BaseOperate.findItemInputViewt(self,'//*[@id="sampleRetentionDetail"]/form/div[1]/div[3]/div/div/div/input',dish)


        BaseOperate.clickDelay(self,'//*[@id="sampleRetentionDetail"]/form/div[1]/div[5]/div/div/div[1]/input')
        person_li1 = BaseOperate.listElementXPathAndClass(self,'/html/body/div[4]/div[1]/div[1]/ul','el-select-dropdown__item')
        num1 = random.randint(0,len(person_li1)-1)
        self.driver.execute_script("arguments[0].click();",person_li1[num1])


        # BaseOperate.clickDelay('/html/body/div[4]/div[1]/div[1]/ul/li[1]/span')


        BaseOperate.clickDelay(self,'//*[@id="sampleRetentionDetail"]/form/div[1]/div[7]/div/div/div/input')
        person_li2 = BaseOperate.listElementXPathAndClass(self,'/html/body/div[5]/div[1]/div[1]/ul','el-select-dropdown__item')
        num2 = random.randint(0,len(person_li2)-1)
        self.driver.execute_script("arguments[0].click();",person_li2[num2])

        # BaseOperate.clickDelay('/html/body/div[5]/div[1]/div[1]/ul/li[1]/span')
        BaseOperate.clickDelay(self,'//*[@id="sampleRetentionDetail"]/form/div[2]/button')
        result = u"新增菜品留样完成"
        print(u"新增菜品留样完成")
        return  result


    def addDineRecord(self,person,indentity,evaluate):

        a = BaseOperate.listElementXPathAndClass(self,'/html/body/div/div/div[1]/header/ul','nav')
        self.driver.execute_script("arguments[0].click();",a[2])

        time.sleep(2)
        li = BaseOperate.listElementXPathAndClass(self,'/html/body/div/div/div[2]/div[1]/div[1]/ul','el-menu-item')
        self.driver.execute_script("arguments[0].click();",li[6])

        time.sleep(2)
        BaseOperate.clickDelay(self,'//*[@id="accompanyMealRecord"]/div[1]/div[2]/button[1]/span')
        BaseOperate.clickDelay(self,'//*[@id="personnelMsgDetail"]/form/div[1]/div[2]/div/div/div/input')
        BaseOperate.clickDelay(self,'/html/body/div[2]/div[1]/div[1]/ul/li[1]')

        BaseOperate.clickDelay(self,'//*[@id="personnelMsgDetail"]/form/div[1]/div[3]/div/div/div[1]/input')

        dish_li = BaseOperate.listElementXPathAndClass(self,'/html/body/div[3]/div[1]/div[1]/ul','el-select-dropdown__item')
        self.driver.execute_script("arguments[0].click();",dish_li[9])
        self.driver.execute_script("arguments[0].click();",dish_li[10])

        BaseOperate.findItemInputViewt(self,'//*[@id="personnelMsgDetail"]/form/div[1]/div[4]/div/div/input',person)
        BaseOperate.findItemInputViewt(self,'//*[@id="personnelMsgDetail"]/form/div[1]/div[5]/div/div/input',indentity)
        BaseOperate.findItemInputViewt(self,'//*[@id="personnelMsgDetail"]/form/div[1]/div[6]/div/div/input',evaluate)
        BaseOperate.findItemInputViewt(self,'//*[@id="personnelMsgDetail"]/form/div[2]/div/div[1]/div/input',r'C:\Users\Administrator\Desktop\QQ截图20200628150848.png')
        BaseOperate.clickDelay(self,'//*[@id="personnelMsgDetail"]/form/div[3]/button/span')
        print(u"新增陪餐完成")
        result = u"新增陪餐完成"
        return result
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     lg = LoginPage(driver)
#     fg = FoodPage(driver)
#     lg.login('dtzxqp','123456')
#     # fg.addFood(u"老腊肉")
#     fg.addReserveSample(u"卤猪蹄")
#     # fg.addDineRecord(u"小当家","特级厨师","好吃，还不错")
#     driver.close()
#     driver.quit()