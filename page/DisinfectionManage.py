import random

from selenium import webdriver

from base.BaseOperate import BaseOperate
from page.LoginOperate import LoginPage


class DisinfectionPage(BaseOperate):
    def addDisinfectionManual(self,tableware,num,hour):
        self.clickDelay('//*[@id="header"]/ul/a[6]')
        self.clickDelay('//*[@id="index"]/div[2]/div[1]/div[3]/ul/li[2]/ul/li/ul/li[3]')
        self.clickDelay('//*[@id="tablewareDf"]/div[1]/div[2]/button[1]/span')
        # driver.find_element_by_xpath('//*[@id="tablewareDf"]/div[1]/div[2]/button[1]/span')
        self.findItemInputViewt('//*[@id="tablewareDfDetail"]/form/div[1]/div[2]/div/div/input',tableware)
        self.findItemInputViewt('//*[@id="tablewareDfDetail"]/form/div[1]/div[3]/div/div/input',num)
        self.findItemInputViewt('//*[@id="tablewareDfDetail"]/form/div[1]/div[6]/div/div/input',hour)
        self.clickDelay('//*[@id="tablewareDfDetail"]/form/div[1]/div[7]/div/div/div[1]/input')
        person_li = self.listElementXPathAndClass('/html/body/div[2]/div[1]/div[1]/ul','el-select-dropdown__item')
        person_num = random.randint(0,len(person_li)-1)

        self.driver.execute_script("arguments[0].click();",person_li[person_num])
        self.clickDelay('//*[@id="tablewareDfDetail"]/form/div[2]/button/span')
        print(u"增加消毒记录成功")
        result = u"增加消毒记录成功"
        return result

if __name__ == '__main__':
    driver = webdriver.Chrome()
    lg = LoginPage(driver)
    dg = DisinfectionPage(driver)
    lg.login('tests','123456')
    dg.addDisinfectionManual(u"碗，筷子，汤匙",'100','2')
    driver.close()