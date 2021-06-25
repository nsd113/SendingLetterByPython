import unittest
from selenium.common.exceptions import TimeoutException
import os
from selenium import webdriver
import pages

# Test Variables
login = 'test4203'
domain = '@mail.ru'
user_password = 'OTi~eRBuer13'
address_email = 'test4203@mail.ru'
topic = 'I\'m testing you'
body = 'Hello World'


class MailRuSendingLetter(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):  # move setup to reusable class?
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(os.getcwd() + '/chromedriver', options=self.chrome_options)
        self.driver.implicitly_wait(10)
        # self.driver.set_page_load_timeout(20)
        try:
            self.driver.get("https://mail.ru/")
            print("URL successfully Accessed")
            self.driver.maximize_window()
        except TimeoutException:
            print("Page load Timeout Occurred. Quiting !!!")
            self.driver.quit()

    def test_sending_email(self):
        """Sends the letter from test account on mail.ru."""
        # login to main page
        main_page = pages.MainPage(self.driver)
        main_page.domain_select(login=login, domain=domain)

        # Password input on a second page
        password_input = pages.PassPage(self.driver)
        password_input.password_login(password=user_password)

        #
        blank_email_button = pages.InboxMain(self.driver)
        blank_email_button.open_letter_blank()

        #
        email_content = pages.NewLetter(self.driver)
        email_content.fill_letter_with_content(address_email, topic, body)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
