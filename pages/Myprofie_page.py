import time
from base.Basedriver import BaseDriver
from selenium.webdriver.common.by import By


class MyProfile(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.wait = wait
        self.driver = driver

    # Locators
    MYPROFILE_DASHBOARD = "//p[text()='My Profile']"
    PENCIL_MARK = "//*[@id = 'root']/div/div[1]/div/div[2]/div[1]//button[1]"
    RESUME_DOWNLOAD = "//*[@id = 'root']/div/div[1]/div/div[2]/div[1]//button[2]"
    SHARE_PROFILE = "//*[@id = 'root']/div/div[1]/div/div[2]/div[1]//button[3]"
    SHARE_INDIFFERENT = "//body/div[4]//button[{i}]"

    """GETTERS"""
    def get_myprofile_editprofile(self):
        return self.element_to_click(By.XPATH, self.MYPROFILE_DASHBOARD)

    def get_editprofile(self):
        return self.element_to_click(By.XPATH, self.PENCIL_MARK)

    def get_download(self):
        return self.element_to_click(By.XPATH, self.RESUME_DOWNLOAD)

    def get_shareprofile(self):
        return self.element_to_click(By.XPATH, self.SHARE_PROFILE)

    def get_shareprofile_socialmedia(self, i):
        return self.element_to_click(By.XPATH, f"//*[@class='css-1jc4bnu']/button[{i}]")

    """SETTERS"""
    def click_myprofile_editprofile(self):
        self.get_myprofile_editprofile().click()

    def click_editprofile(self):
        self.get_editprofile().click()
        self.driver.back()

    def click_download(self,):
        self.get_download().click()

    def click_shareprofile(self):
        self.get_shareprofile().click()
        time.sleep(2)
        my_profile_window = self.driver.current_window_handle
        for i in range(1, 5):
            self.get_shareprofile_socialmedia(i).click()
            time.sleep(4)
            all_handle = self.driver.window_handles
            for handle in all_handle:
                if handle != my_profile_window:
                    self.driver.switch_to.window(handle)
                    self.driver.close()
                    time.sleep(1)
                    break
            self.driver.switch_to.window(my_profile_window)

    def myprofile(self, user):
        self.click_myprofile_editprofile()

        if user == "shareprofile":
            self.click_shareprofile()
        elif user == "downloadresume":
            self.click_download()
        elif user == "editprofile":
            self.click_editprofile()
