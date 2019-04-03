import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage

class Baidu_Search(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        homepage = HomePage(cls.driver)
        homepage.quit_browser()

    def test_baidu_search1(self):
        homepage = HomePage(self.driver)
        homepage.type_search("selenium")
        homepage.send_submit_btn()
        homepage.sleep(2)
        homepage.get_windows_img()
        try:
            assert 'selenium' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))

    def test_baidu_search2(self):
        homepage = HomePage(self.driver)
        homepage.type_search("滑稽")
        homepage.send_submit_btn()
        homepage.sleep(2)
        homepage.get_windows_img()

