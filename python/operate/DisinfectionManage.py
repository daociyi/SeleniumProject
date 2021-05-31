import random
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from python.base.BaseOperate import BaseOperate
from python.operate.LoginOperate import LoginPage
# from python.base.Config import driver


class DisinfectionPage(BaseOperate):
    def addDisinfectionManual(self,tableware,num,hour):
        BaseOperate.clickDelay(self,'//*[@id="header"]/ul/a[6]')
        BaseOperate.clickDelay(self,'//*[@id="index"]/div[2]/div[1]/div[3]/ul/li[2]/ul/li/ul/li[3]')
        BaseOperate.clickDelay(self,'//*[@id="tablewareDf"]/div[1]/div[2]/button[1]/span')
        # driver.find_element_by_xpath(self,'//*[@id="tablewareDf"]/div[1]/div[2]/button[1]/span')
        BaseOperate.findItemInputViewt(self,'//*[@id="tablewareDfDetail"]/form/div[1]/div[2]/div/div/input',tableware)
        BaseOperate.findItemInputViewt(self,'//*[@id="tablewareDfDetail"]/form/div[1]/div[3]/div/div/input',num)
        BaseOperate.findItemInputViewt(self,'//*[@id="tablewareDfDetail"]/form/div[1]/div[6]/div/div/input',hour)
        BaseOperate.clickDelay(self,'//*[@id="tablewareDfDetail"]/form/div[1]/div[7]/div/div/div[1]/input')
        person_li = BaseOperate.listElementXPathAndClass(self,'/html/body/div[2]/div[1]/div[1]/ul','el-select-dropdown__item')
        person_num = random.randint(0,len(person_li)-1)

        self.driver.execute_script("arguments[0].click();",person_li[person_num])
        BaseOperate.clickDelay(self,'//*[@id="tablewareDfDetail"]/form/div[2]/button/span')
        print(u"增加消毒记录成功")
        result = u"增加消毒记录成功"
        return result

# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     lg = LoginPage(driver)
#     dg = DisinfectionPage(driver)
#     lg.login('test','123456')
#     dg.addDisinfectionManual(u"碗，筷子，汤匙",'100','2')
#     driver.close()