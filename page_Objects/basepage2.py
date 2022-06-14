
import time

from selenium.webdriver.common.by import By


class whethe():

    def __init__(self, driver):
        self.driver = driver

    cli_e = (By.XPATH, "//*[contains(text(),'Air Quality')]")

    #Air_Quality = (By.Xpath("//*[contains(text(),'Air Quality')]").click()
    #(By.Xpath("//div[@id='AqiQualityStationTypeId']").text
    #("//span[contains(text(),'Hyderabad')]

    def clickairpollution(self):
        self.driver.find_element(*whethe.cli_e).click()

        time.sleep(10)

#---












#self.driver.find_element_by_xpath("//*[contains(text(),'Air Quality')]").click()
#
# #self.driver.switch_to.alert()
# text = self.driver.find_element_by_xpath("//div[@id='AqiQualityStationTypeId']").text
# print("Air Quality : "+text)
# self.driver.find_element_by_xpath("//div//*[contains(text(), 'Air Quality')]").click()

# self.driver.find_element_by_xpath("//span[contains(text(),'Hyderabad')]").click()

