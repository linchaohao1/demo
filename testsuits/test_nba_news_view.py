import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage
from pageobjects.baidu_news_home import NewsHomePage
from pageobjects.news_sport_home import SportNewsHomePage


class ViewNBANews(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def tearDown(self):
        homepage = HomePage(self.driver)
        homepage.quit_browser()

    def test_view_nba_views(self):
        homepage = HomePage(self.driver)
        homepage.click_news()
        newspage = NewsHomePage(self.driver)
        newspage.click_sports()
        sportnewhome = SportNewsHomePage(self.driver)
        sportnewhome.click_nba_link()
        sportnewhome.get_windows_img()


if __name__ == '__main__':
    unittest.main()
