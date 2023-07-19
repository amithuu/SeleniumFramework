import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
chrome_path = Service(executable_path="/home/chiku/webdriver_manager")
options = webdriver.ChromeOptions()


@pytest.fixture(scope="class")
def setup(url, browser, request):
    if browser == "chrome":
        driver = webdriver.Chrome(service=chrome_path, options=options)
    else:
        driver = webdriver.Chrome(service=chrome_path, options=options)

    # driver.get("https://test-talentplace.vercel.app/login")
    # driver.get("https://www.talentplace.ai/login")

    driver.get(url)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()

    # """ Login Page"""
    # wait.until(ec.element_to_be_clickable((By.NAME, "email"))).send_keys("amithtalentplace@gmail.com")
    # wait.until(ec.element_to_be_clickable((By.NAME, "password"))).send_keys("New@1234")
    # wait.until(ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()
    time.sleep(3)

    request.cls.driver = driver
    request.cls.wait = wait

    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")


@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session", autouse=True)
def url(request):
    return request.config.getoption("--url")
