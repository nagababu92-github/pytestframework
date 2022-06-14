import time

from selenium.webdriver.common.by import By

from tests.BasicTest import BasicTest
from tests.conftest import Basef


class Rahulshetty(BasicTest):

    def __init__(self, driver):
        self.driver = driver

    # phoneI = (By.XPATH, "//a[contains(text(),'iphone X')]")
    # iphone_add_cart = (By.XPATH, "//div[@class='card-footer']//button")
    # # self.driver.find_element_by_xpath("//a[@class ='nav-link btn btn-primary']").click()
    cli_e = (By.XPATH, "//a[contains(text(),'Checkout')]")
    empty = (By.XPATH, "//tbody//tr//td//button[@class ='btn btn-success']")
    click_btn = (By.XPATH, "//div[@class='checkbox checkbox-primary']//label")
    click_agree = (By.XPATH, "//input[@value='Purchase']")

    def clickiphonebutton(self):
        self.driver.find_element(*Rahulshetty.cli_e).click()
        self.driver.find_element(*Rahulshetty.empty).click()
        self.driver.find_element(*Rahulshetty.click_btn).click()
        time.sleep(10)
        self.driver.find_element(*Rahulshetty.click_agree).click()

        time.sleep(10)

