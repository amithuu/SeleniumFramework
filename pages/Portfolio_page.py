import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.Basedriver import BaseDriver

class Portfolio(BaseDriver):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.wait = wait
        self.driver = driver

    # Locator
    portfolio_dashboard = "//*[text()='Portfolio']"
    add_portfolio = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]//button"
    title = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[1]//input"
    description = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]//p"
    link = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[4]/div/div[2]//input"
    add_link = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[4]/div/div[2]//button"
    save_portfolio = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[4]/button"
    image = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[3]/div[1]/div[1]//u"

    """GETTER"""
    def get_portfoliodashboard(self):
        return self.element_to_click(By.XPATH, self.portfolio_dashboard)

    def get_addportfolio(self):
        return self.element_to_click(By.XPATH, self.add_portfolio)

    def get_title(self):
        return self.element_to_click(By.XPATH, self.title)

    def get_description(self):
        return self.element_to_click(By.XPATH, self.description)

    def get_link(self):
        return self.element_to_click(By.XPATH, self.link)

    def get_addlink(self):
        return self.element_to_click(By.XPATH, self.add_link)

    def get_saveportfolio(self):
        return self.element_to_click(By.XPATH, self.save_portfolio)

    """SETTER"""
    def click_portfoliodashboard(self):
        self.get_portfoliodashboard().click()

    def click_addportfolio(self):
        self.get_addportfolio().click()

    def enter_title(self, title):
        self.get_title().click()
        self.get_title().send_keys(title)
        self.get_title().send_keys(Keys.TAB)

    def enter_description(self, description):
        self.get_description().click()
        self.get_description().send_keys(description)

    def enter_link(self, link):
        self.get_link().click()
        self.get_link().send_keys(link)

    def click_addlink(self):
        self.get_addlink().click()

    def click_saveportfolio(self):
        self.get_saveportfolio().click()

    def portfolio(self, title, description, link):
        self.click_portfoliodashboard()
        self.click_addportfolio()
        self.enter_title(title)
        self.enter_description(description)
        self.enter_link(link)
        self.click_addlink()
        self.click_saveportfolio()
        self.next()
        self.back()






