import random
import time
from python.base import BaseOperate
from python.operate import LoginOperate
from python.base.Config import driver

def addFood(product):
    a = BaseOperate.listElementXPathAndClass('/html/body/div/div/div[1]/header/ul','nav')
    driver.execute_script("arguments[0].click();",a[2])
    time.sleep(2)

    BaseOperate.clickDelay('/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/button[1]')
    num = random.randint(1,150)
    BaseOperate.findItemInputViewt('//*[@id="accountRecordDetail"]/form/div[1]/div[3]/div/div[1]/input',num)

    BaseOperate.clickDelay('//*[@id="accountRecordDetail"]/form/div[1]/div[4]/div/div/div/input')
    sup_li = BaseOperate.listElementXPathAndClass('/html/body/div[2]/div[1]/div[1]/ul','el-select-dropdown__item')
    sup_num = random.randint(0,len(sup_li)-1)
    driver.execute_script("arguments[0].click();",sup_li[sup_num])

    BaseOperate.clickDelay('//*[@id="accountRecordDetail"]/form/div[1]/div[5]/div/div/div/input')
    checkPerson_li = BaseOperate.listElementXPathAndClass('/html/body/div[3]/div[1]/div[1]/ul','el-select-dropdown__item')
    checkPerson_num = random.randint(0,len(checkPerson_li)-1)
    driver.execute_script("arguments[0].click();",checkPerson_li[checkPerson_num])



    BaseOperate.findItemInputViewt('//*[@id="accountRecordDetail"]/form/div[1]/div[1]/div/div/div/input',product)
    BaseOperate.findItemInputViewt('//*[@id="accountRecordDetail"]/form/div[4]/div[2]/div[1]/div/input',r"C:\Users\Administrator\Desktop\QQ截图20200616163201.png")
    BaseOperate.clickDelay('//*[@id="accountRecordDetail"]/form/div[5]/button')
    result = u"新增台账完成"
    print(u"新增台账完成")
    return result

def addReserveSample(dish):
    a = BaseOperate.listElementXPathAndClass('/html/body/div/div/div[1]/header/ul','nav')
    driver.execute_script("arguments[0].click();",a[2])

    time.sleep(2)
    li = BaseOperate.listElementXPathAndClass('/html/body/div/div/div[2]/div[1]/div[1]/ul','el-menu-item')
    driver.execute_script("arguments[0].click();",li[3])
    time.sleep(2)
    # BaseOperate.clickDelay('//*[@id="header"]/ul/a[3]')
    #
    # BaseOperate.clickDelay('//*[@id="index"]/div[2]/div[1]/div[1]/ul/li[4]/span')
    BaseOperate.clickDelay('//*[@id="sampleRetention"]/div[1]/div[2]/button[1]/span')
    BaseOperate.clickDelay('//*[@id="sampleRetentionDetail"]/form/div[1]/div[2]/div/div/div/input')
    meal = BaseOperate.listElementXPathAndClass('/html/body/div[2]/div[1]/div[1]/ul','el-select-dropdown__item')
    meal_num = random.randint(0,len(meal)-1)
    driver.execute_script("arguments[0].click();",meal[meal_num])

    # BaseOperate.clickDelay('/html/body/div[2]/div[1]/div[1]/ul/li[1]/span')
    BaseOperate.findItemInputViewt('//*[@id="sampleRetentionDetail"]/form/div[1]/div[3]/div/div/div/input',dish)


    BaseOperate.clickDelay('//*[@id="sampleRetentionDetail"]/form/div[1]/div[5]/div/div/div[1]/input')
    person_li1 = BaseOperate.listElementXPathAndClass('/html/body/div[3]/div[1]/div[1]/ul','el-select-dropdown__item')
    num1 = random.randint(0,len(person_li1)-1)
    driver.execute_script("arguments[0].click();",person_li1[num1])


    # BaseOperate.clickDelay('/html/body/div[4]/div[1]/div[1]/ul/li[1]/span')


    BaseOperate.clickDelay('//*[@id="sampleRetentionDetail"]/form/div[1]/div[7]/div/div/div/input')
    person_li2 = BaseOperate.listElementXPathAndClass('/html/body/div[4]/div[1]/div[1]/ul','el-select-dropdown__item')
    num2 = random.randint(0,len(person_li2)-1)
    driver.execute_script("arguments[0].click();",person_li2[num2])

    # BaseOperate.clickDelay('/html/body/div[5]/div[1]/div[1]/ul/li[1]/span')
    BaseOperate.clickDelay('//*[@id="sampleRetentionDetail"]/form/div[2]/button')
    result = u"新增菜品留样完成"
    print(u"新增菜品留样完成")
    return  result


def addDineRecord(person,indentity,evaluate):

    a = BaseOperate.listElementXPathAndClass('/html/body/div/div/div[1]/header/ul','nav')
    driver.execute_script("arguments[0].click();",a[2])

    time.sleep(2)
    li = BaseOperate.listElementXPathAndClass('/html/body/div/div/div[2]/div[1]/div[1]/ul','el-menu-item')
    driver.execute_script("arguments[0].click();",li[6])

    time.sleep(2)
    BaseOperate.clickDelay('//*[@id="accompanyMealRecord"]/div[1]/div[2]/button[1]/span')
    BaseOperate.clickDelay('//*[@id="personnelMsgDetail"]/form/div[1]/div[2]/div/div/div/input')
    BaseOperate.clickDelay('/html/body/div[2]/div[1]/div[1]/ul/li[1]')

    BaseOperate.clickDelay('//*[@id="personnelMsgDetail"]/form/div[1]/div[3]/div/div/div[1]/input')

    dish_li = BaseOperate.listElementXPathAndClass('/html/body/div[3]/div[1]/div[1]/ul','el-select-dropdown__item')
    driver.execute_script("arguments[0].click();",dish_li[9])
    driver.execute_script("arguments[0].click();",dish_li[10])

    BaseOperate.findItemInputViewt('//*[@id="personnelMsgDetail"]/form/div[1]/div[4]/div/div/input',person)
    BaseOperate.findItemInputViewt('//*[@id="personnelMsgDetail"]/form/div[1]/div[5]/div/div/input',indentity)
    BaseOperate.findItemInputViewt('//*[@id="personnelMsgDetail"]/form/div[1]/div[6]/div/div/input',evaluate)
    BaseOperate.findItemInputViewt('//*[@id="personnelMsgDetail"]/form/div[2]/div/div[1]/div/input',r'C:\Users\Administrator\Desktop\QQ截图20200628150848.png')
    BaseOperate.clickDelay('//*[@id="personnelMsgDetail"]/form/div[3]/button/span')
    print(u"新增陪餐完成")
    result = u"新增陪餐完成"
    return result
# LoginOperate.login('test','123456')
# addFood(u"老腊肉")
# addReserveSample(u"卤猪蹄")
# addDineRecord(u"小当家","特级厨师","好吃，还不错")