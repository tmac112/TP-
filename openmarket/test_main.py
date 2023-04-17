import unittest
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    test_run = unittest.defaultTestLoader.discover("./test_case","test_login.py")
    with open("./reports/result.html", "wb") as f:
        runner = HTMLTestRunner(f, verbosity=2)
        runner.run(test_run)
