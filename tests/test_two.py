import os
from time import sleep

import pytest
import allure

n = os.path.dirname('.')
print(n)
# @pytest.mark.slow
# def test_demo():
#     a = 3
#     print(str(a))
# @allure.story("suibianceshi ")
# def test_one():
#     p =2
#     print(str(p))
# if __name__ == '__main__':
#     pytest.main()
#     sleep(5)
#     os.system("allure generate ./allure-results -o ./allure-reports --clean")
