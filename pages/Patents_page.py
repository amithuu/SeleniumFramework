import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.Basedriver import BaseDriver


class Patent (BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.wait = wait
        self.driver = driver

    # Locator
    patent_editprofile = "//*[text()='Patents']"

    add_another_patent = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div//button"

    patent_title = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]//form/div/div[1]/div[1]//input"
    patent_id = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]//form/div/div[1]/div[2]//input"
    patent_date = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]//form/div/div[1]/div[3]//input"
    patent_url = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]//form/div/div[1]/div[4]//input"
    
    add_author = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]//form/div/div[2]//button"
    
    author_title = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]//form/div/div[2]/form/div/div[1]/div[1]//select"
    author_name = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]//form/div/div[2]/form/div/div[1]/div[2]//input"
    link = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]//form/div/div[2]/form/div/div[2]//input"
    description = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]//form/div/div[3]//p"
    
    save = "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]//form/div/div[4]//button[2]"

    """GETTERS"""

    def get_patent_editprofile(self):
        return self.element_to_click(By.XPATH, self.patent_editprofile)

    def get_add_another_patent(self):
        return self.element_to_click(By.XPATH, self.add_another_patent)

    def get_patent_title(self):
        return self.element_to_click(By.XPATH, self.patent_title)

    def get_patent_id(self):
        return self.element_to_click(By.XPATH, self.patent_id)

    def get_patent_date(self):
        return self.element_to_click(By.XPATH, self.patent_date)

    def get_patent_url(self):
        return self.element_to_click(By.XPATH, self.patent_url)

    def get_add_author(self):
        return self.element_to_click(By.XPATH, self.add_author)

    def get_author_title(self):
        return self.element_to_click(By.XPATH, self.author_title)

    def get_author_name(self):
        return self.element_to_click(By.XPATH, self.author_name)

    def get_link(self):
        return self.element_to_click(By.XPATH, self.link)

    def get_description(self):
        return self.element_to_click(By.XPATH, self.description)

    def get_save_button(self):
        return self.element_to_click(By.XPATH, self.save)

    """SETTERS"""

    def click_patent_editprofile(self):
        self.get_patent_editprofile().click()

    def enter_patent_title(self, title):
        self.get_patent_title().send_keys(title)

    def click_add_another_patent(self):
        self.get_add_another_patent().click()

    def enter_patent_id(self, id):
        self.get_patent_id().send_keys(id)

    def enter_patent_date(self, date):
        self.get_patent_date().send_keys(date)

    def enter_patent_url(self, url):
        self.get_patent_url().send_keys(url)

    def click_add_author(self):
        time.sleep(2)
        self.get_add_author().click()
        time.sleep(1)

    def enter_author_title(self, author_title):
        # self.get_author_title().click()
        self.get_author_title().send_keys(Keys.ARROW_DOWN)
        self.select_options(self.get_author_title(), author_title)

    def enter_author_name(self, name):
        self.get_author_name().send_keys(name)

    def enter_link(self, link):
        self.get_link().send_keys(link)

    def enter_description(self, description):
        self.get_description().send_keys(description)

    def click_save_button(self):
        self.get_save_button().click()
        time.sleep(2)

    def patent(self, i, user, patent_title, patent_id, patent_issue_date, patent_url,  author_title, author_name, author_link, patents_description):
        self.click_patent_editprofile()

        if user == "new":
            if i == 0:
                self.enter_patent_title(patent_title)
                self.enter_patent_id(patent_id)
                self.enter_patent_date(patent_issue_date)
                self.enter_patent_url(patent_url)
                self.click_add_author()
                self.enter_author_title(author_title)
                self.enter_author_name(author_name)
                self.enter_link(author_link)
                self.enter_description(patents_description)
                self.click_save_button()
            else:
                self.click_add_another_patent()
                self.enter_patent_title(patent_title)
                self.enter_patent_id(patent_id)
                self.enter_patent_date(patent_issue_date)
                self.enter_patent_url(patent_url)
                self.click_add_author()
                self.enter_author_title(author_title)
                self.enter_author_name(author_name)
                self.enter_link(author_link)
                self.enter_description(patents_description)
                self.click_save_button()

        elif user == "old":
            self.click_add_another_patent()
            self.enter_patent_title(patent_title)
            self.enter_patent_id(patent_id)
            self.enter_patent_date(patent_issue_date)
            self.enter_patent_url(patent_url)
            self.click_add_author()
            self.enter_author_title(author_title)
            self.enter_author_name(author_name)
            self.enter_link(author_link)
            self.enter_description(patents_description)
            self.click_save_button()
