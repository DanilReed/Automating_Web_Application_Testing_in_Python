from testpage import OperationHelper
import logging
import yaml
import time
from report import send_email


with open("testdata.yaml", encoding="utf-8") as f:
    testdata = yaml.safe_load(f)
    
def test_step1(browser):
    logging.info("Test1 Starting")
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"

def test_step2(browser):
    logging.info("Test2 Starting")
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata.get("username"))
    testpage.enter_pass(testdata.get("passwd"))
    testpage.click_login_button()
    assert testpage.get_home_text() == "Home"

def test_step3(browser):
    logging.info("Test3 Starting")
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata.get("username"))
    testpage.enter_pass(testdata.get("passwd"))
    testpage.click_login_button()
    testpage.click_contact_button()
    testpage.enter_name(testdata.get("name"))
    testpage.enter_email(testdata.get("email"))
    testpage.enter_content(testdata.get("content"))
    testpage.click_contact_us_button()
    time.sleep(2)
    assert testpage.get_alert_text() == "Form successfully submitted"
    browser.quit()

def test_step4(browser):
    logging.info("Test4 Starting")
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata.get("username"))
    testpage.enter_pass(testdata.get("passwd"))
    testpage.click_login_button()
    testpage.click_create_post_button()
    testpage.enter_title(testdata.get("title"))
    testpage.enter_description(testdata.get("description"))
    testpage.enter_post_content(testdata.get("content"))
    testpage.enter_data(testdata.get("data"))
    testpage.download_image()
    testpage.click_save()

def test_5(browser):
    logging.info("Test5 Starting")
    testpage = OperationHelper(browser)
    testpage.go_check_site()
    testpage.click_write_word_button()
    testpage.enter_write_word(testdata.get("word_check"))
    testpage.click_check_word_button()
    assert testpage.get_checking_res() == ""
    time.sleep(2)












