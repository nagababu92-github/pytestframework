# Fixture for Chrome

import pytest
from selenium import webdriver
import json

# command line argument to pick brwser addopts in conftest onLy
##above 60 wont wont

# https://stackoverflow.com/questions/58957699/how-to-pass-firefox-chrome-headless-mode-via-command-line-to-pytest
#
# def pytest_addoption(parser):
#     parser.addoption("--browser_name", action="store", default="chrome")


class Basef():

    @pytest.fixture(autouse=True)
    def setup(self, request):

        global driver

#        browser_name = config.getoption("--browser_name")
#        if browser_name == "chrome":

        self.driver = webdriver

        self.driver = webdriver.Chrome(executable_path="C:\\Users\\nagababu.endla\\pythonProject1\\Drivers\\chromedriver.exe")
        # elif browser_name == "firefox":
        #     self.driver = webdriver
        #
        #     self.driver = webdriver.Firefox(
        #         executable_path="C:\\Users\\nagababu.endla\\pythonProject1\\Drivers\\geckodriver.exe")
        # config.cls.driver = self.driver

        yield
        self.driver.close()


#     # @pytest.hookimpl(tryfirst=True)
#     # def pytest_configure(config):
#     #     if not os.path.exists('reports'):
#     #         os.makedirs('reports')
#     #
#     #     config.option.htmlpath = 'reports/'+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"
#
#
#
#
#
#
#
#
#
#
#     @pytest.mark.hookwrapper
#     def pytest_runtest_makereport(self,item):
#
#         """
#             Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#             :param item:
#         """
#
#         pytest_html = item.config.pluginmanager.getplugin('html')
#         outcome = yield
#         report = outcome.get_result()
#         extra = getattr(report, 'extra', [])
#
#         if report.when == 'call' or report.when == "setup":
#             xfail = hasattr(report, 'wasxfail')
#             if (report.skipped and xfail) or (report.failed and not xfail):
#                 file_name = report.nodeid.replace("::", "_") + ".png"
#                 item._capture_screenshot(file_name)
#                 if file_name:
#                     html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                            'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                     extra.append(pytest_html.extras.html(html))
#             report.extra = extra
#
#     def _capture_screenshot(self, name):
#
#         driver.get_screenshot_as_file(name)
#


#######################################------------

CONFIG_PATH = "config.json"
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ["chrome", "firefox", "edge"]
DEFAULT_URL = "https://www.msn.com/en-in/weather/"


@pytest.fixture(scope='session')
def config():
    #config_file = open(r"config.json")
    #
    config_file = open(r'C:\Users\nagababu.endla\pythonProject1\config.json')
    return json.load(config_file)


# @pytest.fixture(scope="session")
# def browser_setup(config):
#     if "browser" not in config:
#         raise Exception('The config file does not contain "browser"')
#     elif config["browser"] not in SUPPORTED_BROWSERS:
#         raise Exception(f'"{config["browser"]}" is not a supported browser')
#     return config["browser"]


@pytest.fixture(scope='session')
def wait_time_setup(config):
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture(scope='session')
def url_setup(config):
    return config["base_url"] if "base_url" in config else DEFAULT_URL

#
# @pytest.fixture()
# def setup(request, config):
#     driver = DriverFactory.get_driver(config)
#     driver.implicitly_wait(config["timeout"])
#     request.cls.driver = driver
#     before_failed = request.session.testsfailed
#     if config["browser"] == "chrome":
#         driver.maximize_window()
#     yield
#     if request.session.testsfailed != before_failed:
#         allure.attach(driver.get_screenshot_as_png(),
#                       name="Test failed", attachment_type=AttachmentType.PNG)
#     driver.quit()
