from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml

class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])

class OperationHelper(BasePage):

#Enter text
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
            logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word)

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word)


    def enter_name(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_NAME_FIELD"], word)

    def enter_email(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_EMAIL_FIELD"], word)


    def enter_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT_FIELD"], word)

    def enter_write_word(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_WRITE_WORD"], word)

    def enter_title(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_TITLE"], word)

    def enter_description(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_DESCRIPTION"], word)

    def enter_post_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_POST_CONTENT"], word)

    def enter_data(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_DATA"], word)


    def download_image(self):
        try:
            download_img = self.find_element(TestSearchLocators.ids["LOCATOR_IMAGE_BTN"])
            if download_img:
                download_img.send_keys(r'C:\Users\kvarc\Desktop\test.jpg')
            else:
                logging.error("Element not found.")
        except Exception as e:
            logging.exception(f"An error occurred while downloading the image: {e}")


    # click

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login")


    def click_contact_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_GO_CONTACT_BTN"], description="contact")

    def click_contact_us_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_US_BTN"], description="contactUs")

    def click_write_word_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_WRITE_WORD_BTN"], description="writeText")

    def click_check_word_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CHECK_WORD_BTN"], description="checkText")

    def click_create_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CREATE_POST_BTN"], description="checkText")

    def click_image_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_IMAGE_BTN"], description="checkText")

    def click_save(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_SAVE_BTN"], description="checkText")

# get

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get test from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

    def get_alert_text(self):
        alert_field = self.driver.switch_to.alert
        text = alert_field.text
        logging.info(f"Alert text: {text}")
        return text

    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"])

    def get_home_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_HOME_FIELD"])

    def get_checking_res(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_CHECKING_RES"])

