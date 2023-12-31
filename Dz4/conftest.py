import yaml
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from report import send_email

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]

@pytest.fixture(scope="session")
def browser():
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        yield driver
        driver.quit()

@pytest.fixture(scope="session", autouse=True)
def send_email_at_end(request):
    yield

    test_results = request.session.testsfailed

    log_file_path = 'log.txt'
    subject = "Тесты завершены"
    body = f"Тесты завершены. Количество неудачных тестов: {test_results}"
    send_email(subject, body, attachment_path=log_file_path)



