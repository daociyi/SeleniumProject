import random
import time
from python.base import BaseOperate
from python.operate import LoginOperate
from python.base.Config import driver

def  addMorningCheck():
    a = BaseOperate.listElementXPathAndClass('/html/body/div/div/div[1]/header/ul','nav')
    driver.execute_script("arguments[0].click();",a[5])
    time.sleep(2)
    left_li = BaseOperate.listElementXPathAndClass('//*[@id="index"]/div[2]/div[1]/div[4]/ul','el-menu-item')
    driver.execute_script("arguments[0].click();",left_li[1])
    time.sleep(2)
    BaseOperate.clickDelay('//*[@id="dailyMorningCheck"]/div[1]/div[2]/button[1]')
    BaseOperate.clickDelay('//*[@id="dailyMCheckModify"]/form/div[1]/div[1]/div/div/div[1]/input')

    person_li1 = BaseOperate.listElementXPathAndClass('/html/body/div[2]/div[1]/div[1]/ul','el-select-dropdown__item')
    num1 = random.randint(0,len(person_li1)-1)
    driver.execute_script("arguments[0].click();",person_li1[num1])

    BaseOperate.clickDelay('//*[@id="dailyMCheckModify"]/form/div[1]/div[8]/div/div/div[1]/input')
    person_li2 = BaseOperate.listElementXPathAndClass('/html/body/div[3]/div[1]/div[1]/ul','el-select-dropdown__item')
    num2 = random.randint(0,len(person_li2)-1)
    driver.execute_script("arguments[0].click();",person_li2[num2])

    BaseOperate.clickDelay('//*[@id="dailyMCheckModify"]/form/div[2]/button')
    print(u"新增晨检完成")
    result = u"新增晨检完成"
    return result

# LoginOperate.login('test','123456')
# addMorningCheck()
