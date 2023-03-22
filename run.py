import importlib
import sys

import pytest
import os
from time import sleep

# n = os.path.dirname('tests/test_two.py')
# print(n)

if __name__ == "__main__":
    # pytest.main(["tests/test_two.py"])
    #
    # pytest.main(["tests/test_case.py"])
    # sleep(3)
    mm = importlib.import_module(name='.test_two',package='tests')
    os.system("allure generate ./allure-results -o ./allure-reports --clean")

