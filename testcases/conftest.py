import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture(scope="class")
def setup(url, browser, request):
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    # driver.get("https://test-talentplace.vercel.app/login")
    # driver.get("https://www.talentplace.ai/login")
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()

    """ Login Page"""
    wait.until(ec.element_to_be_clickable((By.NAME, "email"))).send_keys("autotest17@g.co")
    wait.until(ec.element_to_be_clickable((By.NAME, "password"))).send_keys("New@1234")
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()
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
