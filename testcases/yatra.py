import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Keys,ActionChains

class Yatra:

    def yatra(self):

        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        oneway = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']")))
        oneway.click()
        time.sleep(2)
        # oneway.send_keys(Keys.CONTROL + "a")
        # time.sleep(2)
        oneway.send_keys("New York")
        list_way = WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='viewport']//div[1]/li")))
        time.sleep(5)

        for results in list_way:

            if "New York (LGA)" in results.text:
                print(results)
                results.click()
                time.sleep(5)
                break


ref = Yatra()
ref.yatra()