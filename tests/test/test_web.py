import pytest
from pytest import assume
# from python.base.Config import driver
from selenium import webdriver
from python.operate.DisinfectionManage import DisinfectionPage
from python.operate.FoodManage import FoodPage
from python.operate.LoginOperate import LoginPage
from python.operate.PersonnalManage import PersonPage


class Test_py:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.lg = LoginPage(self.driver)
        self.fg = FoodPage(self.driver)
        self.dg = DisinfectionPage(self.driver)
        self.pg = PersonPage(self.driver)
        print("open broswer")

    def teardown_class(self):
        self.driver.close()
        self.driver.quit()
        print("close broswer")

    @pytest.fixture()
    def username(self):
        username = 'dtzxqp'
        return username
    @pytest.fixture()
    def password(self):
        password = 123456
        return password

    def test_login(self,username,password):
        result = self.lg.login(username=username,password=password)
        assert  result == u"登录成功","通过"
    # @pytest.mark.skip() 无理由跳过用例
    # @pytest.mark.skipif() 中间为条件与reason 符合条件跳过并显示理由
    def test_addFood(self):
        result = self.fg.addFood(u"香肉")
        assert  result == u"新增台账完成"
    def test_addReserveSample(self):
        result = self.fg.addReserveSample(u"糖醋排骨")
        assert result ==u"新增菜品留样完成"

    # @pytest.mark.xfail (strict=True)
    def test_addDineRecord(self):
        result = self.fg.addDineRecord(u"小当家",u"特级厨师",u"好吃，不错")
        assert  result ==u"新增陪餐完成"

    def test_addDisinfectionManual(self):
        result = self.dg.addDisinfectionManual(u"碗，汤匙","100","2")
        assert result ==  u"增加消毒记录成功"

    def test_addMorningCheck(self):
        result = self.pg.addMorningCheck()
        assert  result == u"新增晨检完成"




if __name__ == '__main__':
    pytest.main(['-s -v','test_web.py'])

