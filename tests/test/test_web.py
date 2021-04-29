import pytest

from python.base.Config import driver
from python.operate import LoginOperate, FoodManage, DisinfectionManage, PersonnalManage

def setup():
    url = 'http://218.6.70.66:25046/#/login'
    driver.get(url)
    driver.maximize_window()
    driver.execute_script("document.body.style.zoom='0.8'")
    print("open broswer")

def test_login():
    result = LoginOperate.login('test','123456')
    assert result == u"登录成功"

def test_addFood():
    result = FoodManage.addFood(u"香肉")
    assert  result == u"新增台账完成"
def test_addReserveSample():
    result = FoodManage.addReserveSample(u"糖醋排骨")
    assert result ==u"新增菜品留样完成"
@pytest.mark.xfail
# (strict=True)
def test_addDineRecord():
    result = FoodManage.addDineRecord(u"小当家",u"特级厨师",u"好吃，不错")
    assert  result ==u"新增陪餐完成"

def test_addDisinfectionManual():
    result = DisinfectionManage.addDisinfectionManual(u"碗，汤匙","100","2")
    assert result ==  u"增加消毒记录成功"

def test_addMorningCheck():
    result = PersonnalManage.addMorningCheck()
    assert  result == u"新增晨检完成"

def teardown():
    driver.close()
    driver.quit()
    print("close broswer")