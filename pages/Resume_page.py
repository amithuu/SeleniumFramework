import time
from base.Basedriver import BaseDriver
from selenium.webdriver.common.by import By


class Resume(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.wait = wait
        self.driver = driver

    # Locators
    RESUME_EDITPROFILE = "//p[text()='Resumes']"
    RESUME_CLICK = "//*[@id='root']/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[{i}]/div"

    NEXT = "//body/div[4]/div[3]/div//div//button[2]"
    BACK = "//body/div[4]/div[3]/div//div//button[1]"

    DOWNLOAD = "//button[text() ='Download']"
    DOWNLOAD_POPUP = "//a[text() = 'Download']"
    POP_UP = "//body/div[4]/div[3]/div//button[1]"
    UPGRADE_BUTTON = "//body/div[4]/div[3]/div//div/div/div[2]//div//button"

    FILTER = "//*[@id='root']/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/button"

    COUNTRY_FILTER = "//*[@id='root']/div/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div/label[{i}]/span[1]"
    COMPANY_FILTER = "//*[@id='root']/div/div[2]/div[2]/div/div/div[2]/div[1]/div[3]/div/label[{i}]/span[1]"
    COLOR_FILTER = "//*[@id='root']/div/div[2]/div[2]/div/div/div[2]/div[1]/div[4]/div/label[{i}]/span[1]"

    """GETTERS"""

    def get_resume_editprofile(self):
        return self.element_to_click(By.XPATH, self.RESUME_EDITPROFILE)

    def get_click_resume(self, i):
        return self.element_to_click(By.XPATH, f"//*[@id='root']/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[{i}]/div")

    def get_next(self):
        return self.element_to_click(By.XPATH, self.NEXT)

    def get_back(self):
        return self.element_to_click(By.XPATH, self.BACK)

    def get_download(self):
        return self.element_to_click(By.XPATH, self.DOWNLOAD)

    def get_download_popup(self):
        return self.element_to_click(By.XPATH, self.DOWNLOAD_POPUP)

    def get_close_popup(self):
        return self.element_to_click(By.XPATH, self.POP_UP)

    def get_upgrade_button(self):
        return self.element_to_click(By.XPATH, self.UPGRADE_BUTTON)

    def get_filter(self):
        return self.element_to_click(By.XPATH, self.FILTER)

    def get_company_filter(self, i):
        return self.element_to_click(By.XPATH, f"//*[@id='root']/div/div[2]/div[2]/div/div/div[2]/div[1]/div[3]/div/label[{i}]/span[1]")

    def get_country_filter(self, i):
        return self.element_to_click(By.XPATH, f"//*[@id='root']/div/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div/label[{i}]/span[1]")

    def get_filter_color(self, i):
        return self.element_to_click(By.XPATH, f"//*[@id='root']/div/div[2]/div[2]/div/div/div[2]/div[1]/div[4]/div/label[{i}]/span[1]")

    """SETTERS"""

    def resume_editprofile(self):
        self.get_resume_editprofile().click()

    def click_resume(self, i):
        self.get_click_resume(i).click()

    def click_next(self):
        self.get_next().click()

    def click_back(self):
        self.get_back().click()

    def click_download(self):
        self.get_download().click()
        time.sleep(2)

    def click_download_popup(self):
        self.get_download_popup().click()
        time.sleep(2)

    def click_upgrade_button(self):
        self.get_upgrade_button().click()

    def click_pop_up(self):
        self.get_close_popup().click()

    def choose_filter(self):
        self.get_filter().click()
        time.sleep(2)
        self.get_filter().click()

    def choose_country_filter(self):
        for i in range(1, 4):
            self.get_country_filter(i).click()
            time.sleep(2)
            self.get_country_filter(i).click()

    def choose_company_filter(self):
        for i in range(1, 5):
            self.get_company_filter(i).click()
            time.sleep(2)
            self.get_company_filter(i).click()

    def choose_color_filter(self):
        for i in range(1, 10):
            self.get_filter_color(i).click()
            time.sleep(2)
            self.get_filter_color(i).click()

    def filter(self):
        self.resume_editprofile()
        time.sleep(4)
        self.choose_filter()
        self.choose_country_filter()
        self.choose_company_filter()
        self.choose_color_filter()

    def resume(self, i, plan):
        self.click_resume(i)
        time.sleep(3)
        if plan == "Trail" or "Monthly":
            if plan == "Trail":
                if i <= 2:
                    if i == 1:
                        self.click_download()
                        self.click_download_popup()
                        self.click_pop_up()
                    else:
                        self.click_download()
                        self.click_pop_up()
                else:
                    self.click_upgrade_button()
                    time.sleep(3)
                    self.driver.back()
                    time.sleep(1)
            elif plan == "Monthly":
                if i <= 5:
                    self.click_download()
                    self.click_pop_up()
                else:
                    self.click_upgrade_button()
                    time.sleep(1)
        else:
            self.click_download()
            self.click_pop_up()
            time.sleep(1)
