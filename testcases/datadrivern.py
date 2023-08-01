import pytest
from base.Basedriver import BaseDriver
# from selenium.webdriver.common.by import By
from ddt import ddt

# @pytest.mark.usefixtures("setup")
@ddt
class Data_driven(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # Locators
    experience_editprofiles = "//*[text()='Experience']"

    addcompany_button = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]//button"

    company_name = "//div[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[1]//input"
    companyname_list = "//div[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]//li/div"

    nature_work = "//div[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]//input"
    naturework_list = "//div[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div[2]//div/div/li/div"

    industry = "//div[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]//input"
    industry_list = "//div[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]//div/div/li/div"

    organization_type = "//div[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div[1]//input"
    organization_list = "//div[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div[1]/div/div/div[2]//div/div/li/div"

    based = "//div[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div[2]//input"
    based_list = "//div[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div[2]//div/div/li/div"

    save_next = "//*[@id ='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[4]//button[2]"

    # def test_data(self):


