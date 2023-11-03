import time

import yaml
# from module import Site
import pytest

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
# site = Site(testdata["address"])

def test_step1(site, selector_login, selector_passwd, selector_button_check, selector_error):
    input1 = site.find_element("xpath", selector_login)
    input1.send_keys("test")

    input2 = site.find_element("xpath", selector_passwd)
    input2.send_keys("test")

    btn = site.find_element("css", selector_button_check)
    btn.click()

    error_text3 = site.find_element("xpath", selector_error)
    assert error_text3.text == "401"
    # site.close()

def test_step2(site, selector_login, selector_passwd, selector_button_check, selector_error, selector_home):
    input1 = site.find_element("xpath", selector_login)
    input1.send_keys(testdata.get("username"))

    input2 = site.find_element("xpath", selector_passwd)
    input2.send_keys(testdata.get("passwd"))

    btn = site.find_element("css", selector_button_check)
    btn.click()

    valid_text3 = site.find_element("xpath", selector_home)
    assert valid_text3.text == "Home"


def test_step3(site, selector_login, selector_passwd, selector_button_post, selector_error, selector_home, selector_button_check, selector_title, selector_description, selector_button_save):
    input1 = site.find_element("xpath", selector_login)
    input1.send_keys(testdata.get("username"))

    input2 = site.find_element("xpath", selector_passwd)
    input2.send_keys(testdata.get("passwd"))

    btn = site.find_element("css", selector_button_check)
    btn.click()

    valid_text3 = site.find_element("xpath", selector_home)
    assert valid_text3.text == "Home", "Test Fail"

    btn = site.find_element("xpath", selector_button_post)
    btn.click()

    input1 = site.find_element("xpath", selector_title)
    input1.send_keys(testdata.get("title"))

    input1 = site.find_element("xpath", selector_description)
    input1.send_keys(testdata.get("description"))
    time.sleep(3)

    btn = site.find_element("xpath", selector_button_save)
    btn.click()
    time.sleep(2)