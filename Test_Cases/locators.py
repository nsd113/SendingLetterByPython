from selenium.webdriver.common.by import By


class MainPageLocators(object):
    # Input email address
    email_account = "//*[@id='mailbox']/form[1]/div[1]/div[2]/input"
    # Selecting domain
    domain_option = "//*[@id='mailbox']/form[1]/div[1]/div[1]/select"
    # Press button to continue
    button_enter = "//*[@id='mailbox']/form[1]/button[1]"


class PassInput(object):
    # input password
    password_input = "//*[@id='mailbox']/form[1]/div[2]/input"
    # enter the mail
    pass_button = "//*[@id='mailbox']/form[1]/button[2]"


class NewLetterLoc(object):
    # open mail form
    letter_blank = "//*[@id='app-canvas']/div/div[1]/div[1]/div/div[2]/span/div[1]/div[1]/div/div/div/div[1]/div/div/a/span/span"


class DestinationAddress(object):
    contact = "/html/body/div[16]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div/div[2]/div/div/label/div/div/input"
    topic = "Subject"
    letter_content = ".//div[starts-with(@class, 'editable-container')]/div/div"
    send_button = "//div[2]/div/span/span/span"
