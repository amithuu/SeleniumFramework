import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_path = Service(ChromeDriverManager("116.0.5845.96").install())
# chrome_path = Service("/home/chiku/webdriver_manager")
chromOptions = Options()
@pytest.fixture(scope="class")
def setup(url, browser, request):
    if browser == "chrome":
        driver = webdriver.Chrome(service=chrome_path, options=chromOptions)
    else:
        driver = webdriver.Chrome(service=chrome_path, options=chromOptions)

    # driver.get("https://test-talentplace.vercel.app/login")
    # driver.get("https://tp-prettified.vercel.app/")
    # driver.get("https://www.talentplace.ai/login")

    driver.get(url)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()

    """ Login Page"""
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))).click()
    # wait.until(ec.element_to_be_clickable((By.NAME, "email"))).send_keys("autotest50@g.co")
    wait.until(ec.element_to_be_clickable((By.NAME, "email"))).send_keys("prod10@g.co")
    wait.until(ec.element_to_be_clickable((By.NAME, "password"))).send_keys("New@1234")
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Log In']"))).click()
    # time.sleep(5)

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
