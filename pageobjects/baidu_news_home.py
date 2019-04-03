from framework.base_page import BasePage

class NewsHomePage(BasePage):
    sports_link = "xpath=>//*[@id='channel-shanghai']/div/ul/li[7]/a"

    def click_sports(self):
        self.click(self.sports_link)
        self.sleep(2)
        