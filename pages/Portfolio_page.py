import time
from selenium.webdriver.common.by import By
from base.Basedriver import BaseDriver

class Portfolio(BaseDriver):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.wait = wait
        self.driver = driver

    # Locator
    portfolio_editprofile = "//*[text()='Portfolio']"

    add_another_portfolio = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div//button"

    portfolio_title = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[1]//input"
    portfolio_description = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[2]//p"

    image = "document.getElementsByTagName('u')[0]"

    portfolio_link = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[4]//input"
    add_button = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[4]//button"

    save = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[4]/div[2]//button[2]"

    """GETTER"""
    def get_portfolio_editprofile(self):
        return self.element_to_click(By.XPATH, self.portfolio_editprofile)

    def get_add_another_portfolio(self):
        return self.element_to_click(By.XPATH, self.add_another_portfolio)

    def get_portfolio_title(self):
        return self.element_to_click(By.XPATH, self.portfolio_title)

    def get_portfolio_description(self):
        return self.element_to_click(By.XPATH, self.portfolio_description)

    def get_portfolio_link(self):
        return self.element_to_click(By.XPATH, self.portfolio_link)

    def get_add_button(self):
        return self.element_to_click(By.XPATH, self.add_button)

    def get_save_button(self):
        return self.element_to_click(By.XPATH, self.save)

    def get_image(self):
        return self.javascript_link(self.image)

    """SETTER"""
    def click_portfolio_editprofile(self):
        self.get_portfolio_editprofile().click()

    def click_add_another_portfolio(self):
        self.get_add_another_portfolio().click()

    def enter_portfolio_title(self, title):
        self.get_portfolio_title().send_keys(title)

    def enter_portfolio_description(self, description):
        self.get_portfolio_description().send_keys(description)

    def add_image(self):
        self.get_image()

    def enter_portfolio_link(self, link):
        self.get_portfolio_link().send_keys(link)

    def click_add_button(self):
        self.get_add_button().click()

    def click_save_button(self):
        self.get_save_button().click()
        time.sleep(2)

    def portfolio(self, i, user, portfolio_title, portfolio_description, portfolio_link):
        self.click_portfolio_editprofile()

        if user == "new":
            if i == 0:
                self.enter_portfolio_title(portfolio_title)
                self.enter_portfolio_description(portfolio_description)
                self.add_image()
                self.enter_portfolio_link(portfolio_link)
                self.click_add_button()
                self.click_save_button()
            else:
                self.click_add_another_portfolio()
                self.enter_portfolio_title(portfolio_title)
                self.enter_portfolio_description(portfolio_description)
                self.add_image()
                self.enter_portfolio_link(portfolio_link)
                self.click_add_button()
                self.click_save_button()

        elif user == "old":
            self.click_add_another_portfolio()
            self.click_portfolio_editprofile()
            self.enter_portfolio_title(portfolio_title)
            self.enter_portfolio_description(portfolio_description)
            self.add_image()
            self.enter_portfolio_link(portfolio_link)
            self.click_add_button()
            self.click_save_button()
