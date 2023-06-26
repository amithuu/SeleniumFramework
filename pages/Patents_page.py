import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.Basedriver import BaseDriver


class Patent(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.wait = wait
        self.driver = driver

    # Locator
    patent_dashboard = "//*[text()='Patents']"
    patent_title = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[1]/div[1]//input"
    add_patent = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]//button"
    patent_id = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[1]/div[2]//input"
    patent_date = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[2]/div[1]//input"
    patent_url = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[2]/div[2]//input"
    add_author = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[3]//button"
    author_title = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[3]/form/div/div[1]/div[1]//select"
    author_name = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[3]/form/div/div[1]/div[2]//input"
    link = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[3]/form/div/div[2]//input"
    description = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/div[4]//p"
    save_patent = "//*[@id='root']/div[2]/div[2]/div/div/div/div/div[2]/div/div/form/div/button"

    """GETTERS"""

    def get_patentdashboard(self):
        return self.element_to_click(By.XPATH, self.patent_dashboard)

    def get_addpatent(self):
        return self.element_to_click(By.XPATH, self.add_patent)

    def get_patenttitle(self):
        return self.element_to_click(By.XPATH, self.patent_title)

    def get_patentid(self):
        return self.element_to_click(By.XPATH, self.patent_id)

    def get_patentdate(self):
        return self.element_to_click(By.XPATH, self.patent_date)

    def get_patenturl(self):
        return self.element_to_click(By.XPATH, self.patent_url)

    def get_addauthor(self):
        return self.element_to_click(By.XPATH, self.add_author)

    def get_authortitle(self):
        return self.element_to_click(By.XPATH, self.author_title)

    def get_author_name(self):
        return self.element_to_click(By.XPATH, self.author_name)

    def get_link(self):
        return self.element_to_click(By.XPATH, self.link)

    def get_description(self):
        return self.element_to_click(By.XPATH, self.description)

    def get_savepatent(self):
        return self.element_to_click(By.XPATH, self.save_patent)

    """SETTERS"""

    def click_patentdashboard(self):
        self.get_patentdashboard().click()

    def enter_patenttitle(self, title):
        self.get_patenttitle().click()
        self.get_patenttitle().send_keys(title)
        self.get_patenttitle().send_keys(Keys.TAB)

    def click_addpatent(self):
        self.get_addpatent().click()

    def enter_patentid(self, id):
        self.get_patentid().click()
        self.get_patentid().send_keys(id)
        self.get_patentid().send_keys(Keys.TAB)

    def enter_patentdate(self, date):
        self.get_patentdate().click()
        self.get_patentdate().send_keys(date)
        self.get_patentdate().send_keys(Keys.TAB)

    def enter_patenturl(self, url):
        self.get_patenturl().click()
        self.get_patenturl().send_keys(url)
        self.get_patenturl().send_keys(Keys.TAB)

    def click_addauthor(self):
        self.get_addauthor().click()

    def enter_authortitle(self):
        self.get_authortitle().click()
        self.get_authortitle().send_keys(Keys.ARROW_DOWN)
        self.get_authortitle().send_keys(Keys.ENTER)
        self.get_authortitle().send_keys(Keys.TAB)

    def enter_authorname(self, name):
        self.get_author_name().click()
        self.get_author_name().send_keys(name)
        self.get_author_name().send_keys(Keys.TAB)

    def enter_link(self, link):
        self.get_link().click()
        self.get_link().send_keys(link)

    def enter_description(self, description):
        self.get_description().click()
        self.get_description().send_keys(description)

    def click_savepatent(self):
        self.get_savepatent().click()

    def patent(self, i, title, id, date, url, name, link, description):
        self.click_addpatent()
        self.enter_patenttitle(title)
        self.enter_patentid(id)
        self.enter_patentdate(date)
        self.enter_patenturl(url)
        self.click_addauthor()
        self.page_down()
        self.enter_authortitle()
        self.enter_authorname(name)
        self.enter_link(link)
        self.enter_description(description)
        self.click_savepatent()
        time.sleep(5)
        if i == 0:
            self.next()
            self.back()
        elif i == 1:
            self.next()
            self.discrad()
            self.back()
        else:
            self.next()



