import datetime
import os
from time import sleep

import pytest
import allure

from selenium import webdriver
from page.DisinfectionManage import DisinfectionPage
from page.FoodManage import FoodPage
from page.LoginOperate import LoginPage
from page.PersonnalManage import PersonPage
from ddt import ddt


# from mailreport.send_email.SendEmail import

@ddt
class Test_py(object):

    def setup_class(self):
        # self.browser = webdriver.ChromeOptions()
        # self.browser.add_argument('--headless')
        # self.browser.add_argument('--disable-gpu')
        driver = webdriver.Chrome()
        self.lg = LoginPage(driver,"登录测试日志")
        self.fg = FoodPage(driver,"食材管理日志")
        # self.dg = DisinfectionPage(driver)
        # self.pg = PersonPage(driver)
        print("open broswer")

    def teardown_class(self):
        self.lg.quitBrowse()
        print("close broswer")



    # @file_data('../python/data/login_data.yaml')
    # def test_s1_login(self,**kwargs):
    #     result = self.lg.login(username=kwargs['username'],password=kwargs['password'])
    #     # print(login_info[0]['username']+login_info[0]['password'])
    #     assert  result == u"登录成功","通过"
    # @pytest.mark.logintest
    # @pytest.mark.parametrize("username,password",[("guanli","2022Standards"),("hhzx","123456")])
    # def test_login(self,username,password):
    #     result = self.lg.login(username,password)
    #     print(os.getcwd())
    #     assert result == u"登录成功"

    def test_login(self,userInfo):
        result = self.lg.login(userInfo['username'],userInfo['password'])
        assert result == u"登录成功"


    # # @pytest.mark.skip() 无理由跳过用例
    # # @pytest.mark.skipif() 中间为条件与reason 符合条件跳过并显示理由
    # def test_addFood(self):
    #     result = self.fg.addFood(u"茴香饺子")
    #     assert  result == u"新增台账完成"
    #
    # def test_updataFood(self):
    #     result = self.fg.updateFood(u"香肉")
    #     assert  result == u"修改成功！"
    #
    #
    # def test_addReserveSample(self):
    #     result = self.fg.addReserveSample(u"糖醋排骨")
    #     assert result ==u"新增菜品留样完成"
    #
    # # @pytest.mark.xfail (strict=True)
    # def test_addDineRecord(self):
    #     result = self.fg.addDineRecord(u"小当家",u"特级厨师",u"好吃，不错")
    #     assert  result ==u"新增陪餐完成"
    #
    # def test_addDisinfectionManual(self):
    #     result = self.dg.addDisinfectionManual(u"碗，汤匙","100","2")
    #     assert result ==  u"增加消毒记录成功"
    #
    # def test_addMorningCheck(self):
    #     result = self.pg.addMorningCheck()
    #     assert  result == u"新增晨检完成"



if __name__ == '__main__':
    # current_time1 = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    # # report = '--html=./report/'+'2021-06-03 18 03 15'+'\''report.html'
    # report = '--html=./report/'+current_time1+' report.html'
    # report_name = current_time1+' report.html'
    # # print(str(report))
    # # # pytest.main(['-s','-v','test_web.py',"--html=./re/res.html"])
    # pytest.main(["-m","-s","-v",report,"--self-contained-html"])
    # # 运行产出报告并发送至邮箱
    # # email = SendEmail().mail(report_name)
    # # if email:
    # #     print("邮件发送成功")
    # # else:
    # #     print("邮件发送失败")
    # print(os.getcwd())
    pytest.main()
    sleep(5)
    os.system("allure generate ./allure-results -o ./allure-reports --clean")