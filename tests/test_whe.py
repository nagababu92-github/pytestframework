import time

from page_Objects import basePage
from tests.BasicTest import BasicTest
from tests.conftest import Basef
from utilities.BaseClass import logger


class Test(BasicTest):

    def test_we2e(self):
        base = basePage.Rahulshetty(self.driver)
        # logg = logger()
        self.driver.get(Basef.URL)
        self.driver.maximize_window()

        self.driver.implicitly_wait(60)
        # time.sleep(60)

        print(self.driver.title)
        print(self.driver.current_url)
        #
        self.driver.find_element_by_xpath("//*[contains(text(),'Air Quality')]").click()
        # time.sleep(10)
        #
        # #self.driver.switch_to.alert()
        # text = self.driver.find_element_by_xpath("//div[@id='AqiQualityStationTypeId']").text
        # print("Air Quality : "+text)
        #
        # self.driver.find_element_by_xpath("//div//*[contains(text(), 'Air Quality')]").click()
        # #time.sleep(60)

        # self.driver.find_element_by_xpath("//span[contains(text(),'Hyderabad')]").click()
        # time.sleep(60)

        #def clickairpollution(self):

        text = self.driver.find_element_by_xpath("//div[@id='CurrentDetailLineWindValue']").text
        print("Air quality value" + text)
