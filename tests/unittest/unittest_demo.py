import unittest

from python.base.Config import driver
from python.operate import LoginOperate


class UnitTest_Demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        url = 'http://218.6.70.66:25046/#/login'
        driver.get(url)
        driver.maximize_window()
        driver.execute_script("document.body.style.zoom='0.8'")
        print("open broswer")

    def test_login(self):
        result = LoginOperate.login('test','123456')
        self.assertEquals(result,"登录成功",msg="断言成功")

    @classmethod
    def tearDownClass(cls) -> None:
        driver.close()
        driver.quit()
        print('浏览器关')

if __name__ == "__main__":
    unittest.main()