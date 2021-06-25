from locators import MainPageLocators, PassInput, NewLetterLoc, DestinationAddress
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver

    def wait_element_loc(self, path, time=20):
        WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((By.XPATH, path)), message=f"Can't find element: {path}")


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    def domain_select(self, login, domain):
        self.driver.find_element_by_xpath(MainPageLocators.email_account).send_keys(login)
        self.driver.find_element_by_xpath(MainPageLocators.domain_option).send_keys(domain)
        self.driver.find_element_by_xpath(MainPageLocators.button_enter).click()


class PassPage(BasePage):

    def password_login(self, password):
        self.driver.set_page_load_timeout(10)
        self.driver.find_element_by_xpath(PassInput.password_input).send_keys(password)
        self.driver.find_element_by_xpath(PassInput.pass_button).click()


class InboxMain(BasePage):

    def open_letter_blank(self):
        # open mail form
        self.driver.set_page_load_timeout(10)
        self.wait_element_loc(path=NewLetterLoc.letter_blank)
        self.driver.find_element_by_xpath(NewLetterLoc.letter_blank).click()


class NewLetter(BasePage):

    def fill_letter_with_content(self, address_email, subj, text):
        self.wait_element_loc(path=DestinationAddress.contact)
        self.driver.find_element_by_xpath(DestinationAddress.contact).send_keys(address_email)
        self.driver.find_element_by_name(DestinationAddress.topic).click()
        self.driver.find_element_by_name(DestinationAddress.topic).clear()
        self.driver.find_element_by_name(DestinationAddress.topic).send_keys(subj)
        self.driver.find_element_by_xpath(DestinationAddress.letter_content).send_keys(text)
        self.driver.find_element_by_xpath(DestinationAddress.send_button).click()
