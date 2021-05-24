import pytest

from python.base.Config import driver
from python.operate import LoginOperate, FoodManage, DisinfectionManage, PersonnalManage

class py_test:
    @classmethod
    def setup_class(self):
        url = 'http://218.6.70.66:25046/#/login'
        driver.get(url)
        driver.maximize_window()
        driver.execute_script("document.body.style.zoom='0.8'")
        print("open broswer")

    def test_login(self):
        result = LoginOperate.login('test','123456')
        assert result == u"登录成功"
    # @pytest.mark.skip() 无理由跳过用例
    # @pytest.mark.skipif() 中间为条件与reason 符合条件跳过并显示理由
    def test_addFood(self):
        result = FoodManage.addFood(u"香肉")
        assert  result == u"新增台账完成"
    def test_addReserveSample(self):
        result = FoodManage.addReserveSample(u"糖醋排骨")
        assert result ==u"新增菜品留样完成"

    # @pytest.mark.xfail (strict=True)
    def test_addDineRecord(self):
        result = FoodManage.addDineRecord(u"小当家",u"特级厨师",u"好吃，不错")
        assert  result ==u"新增陪餐完成"

    def test_addDisinfectionManual(self):
        result = DisinfectionManage.addDisinfectionManual(u"碗，汤匙","100","2")
        assert result ==  u"增加消毒记录成功"

    def test_addMorningCheck(self):
        result = PersonnalManage.addMorningCheck()
        assert  result == u"新增晨检完成"

    def teardown_class(self):
        driver.close()
        driver.quit()
        print("close broswer")


if __name__ == '__main__':
    pytest.main(["-s","test_web.py"])
