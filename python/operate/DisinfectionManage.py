import random
import time
from python.base import BaseOperate
from python.operate import LoginOperate
from python.base.Config import driver



def addDisinfectionManual(tableware,num,hour):
    BaseOperate.clickDelay('//*[@id="header"]/ul/a[6]')
    BaseOperate.clickDelay('//*[@id="index"]/div[2]/div[1]/div[3]/ul/li[2]/ul/li/ul/li[3]')
    BaseOperate.clickDelay('//*[@id="tablewareDf"]/div[1]/div[2]/button[1]/span')
    BaseOperate.findItemInputViewt('//*[@id="tablewareDfDetail"]/form/div[1]/div[2]/div/div/input',tableware)
    BaseOperate.findItemInputViewt('//*[@id="tablewareDfDetail"]/form/div[1]/div[3]/div/div/input',num)
    BaseOperate.findItemInputViewt('//*[@id="tablewareDfDetail"]/form/div[1]/div[6]/div/div/input',hour)
    BaseOperate.clickDelay('//*[@id="tablewareDfDetail"]/form/div[1]/div[7]/div/div/div[1]/input')
    person_li = BaseOperate.listElementXPathAndClass('/html/body/div[2]/div[1]/div[1]/ul','el-select-dropdown__item')
    person_num = random.randint(0,len(person_li)-1)

    driver.execute_script("arguments[0].click();",person_li[person_num])
    BaseOperate.clickDelay('//*[@id="tablewareDfDetail"]/form/div[2]/button/span')
    print(u"增加消毒记录成功")
    result = u"增加消毒记录成功"
    return result

# LoginOperate.login('test','123456')
#
# addDisinfectionManual(u"碗，筷子，汤匙",'100','2')
# driver.close()