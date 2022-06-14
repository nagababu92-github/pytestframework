import time

from page_Objects import basePage
from tests.conftest import Basef
from utilities.BaseClass import logger


class Test(Basef):
    def test_e2e(self):

        base = basePage.Rahulshetty(self.driver)
        self.driver.get("https://rahulshettyacademy.com/angularpractice/shop/")
        self.driver.maximize_window()
        time.sleep(6)


        # self.driver.implicitly_wait(10)
        # print(self.driver.title)
        # print(self.driver.current_url)


        # self.driver.get_screenshot_as_file("file.png")

        base.clickiphonebutton()
        logger.info("added page object and cicked on checked out b")
    #
    #
    # def test_another(self):
    #     a = 10
    #     b = 100
    #     print(a==b)
