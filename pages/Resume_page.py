import time
from base.Basedriver import BaseDriver
from selenium.webdriver.common.by import By


class Resume(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.wait = wait
        self.driver = driver

    # Locators
    RESUME_DASHBOARD = "//p[text()='Resumes']"
    RESUME_CLICK = "//*[@id='root']/div[2]/div[2]/div/div/div[2]/div[{i}]/div"
    NEXT = "//body/div[4]/div[3]/div//div//button[2]"
    BACK = "//body/div[4]/div[3]/div//div//button[1]"
    DOWNLOAD = "Download"
    POP_UP = "//body/div[4]/div[3]/div//button[1]"
    UPGRADE_BUTTON = "//body/div[4]/div[3]/div//div/div/div[2]//div//button"

    """GETTERS"""
    def get_resumedashboard(self):
        return self.element_to_click(By.XPATH, self.RESUME_DASHBOARD)

    def get_resumeclick(self, i):
        return self.element_to_click(By.XPATH, f"//*[@id='root']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[{i}]/div")

    def get_next(self):
        return self.element_to_click(By.XPATH, self.NEXT)

    def get_back(self):
        return self.element_to_click(By.XPATH, self.BACK)

    def get_download(self):
        return self.element_to_click(By.LINK_TEXT, self.DOWNLOAD)

    def get_closepop_up(self):
        return self.element_to_click(By.XPATH, self.POP_UP)

    def get_upgradebutton(self):
         return self.element_to_click(By.XPATH, self.UPGRADE_BUTTON)

    """SETTERS"""
    def click_resumedashboard(self):
        self.get_resumedashboard().click()

    def click_resumeclick(self, i):
        self.get_resumeclick(i).click()

    def click_next(self):
        self.get_next().click()

    def click_back(self):
        self.get_back().click()

    def click_download(self):
        self.get_download().click()

    def click_upgradebutton(self):
        self.get_upgradebutton().click()

    def click_pop_up(self):
        self.get_closepop_up().click()

    def resume(self, i, plan):
        self.click_resumedashboard()
        time.sleep(4)
        self.click_resumeclick(i)
        # self.click_next()
        # self.click_back()
        if plan == "Trail" or "Monthly":
            if plan == "Trail":
                if i <= 2:
                    self.click_download()
                    self.click_pop_up()
                else:
                    self.click_upgradebutton()
                    time.sleep(1)
            elif plan == "Monthly":
                if i <= 5:
                    self.click_download()
                    self.click_pop_up()
                else:
                    self.click_upgradebutton()
                    time.sleep(1)
        else:
            self.click_download()
            self.click_pop_up()
            time.sleep(1)



