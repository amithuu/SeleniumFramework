import time
from selenium.webdriver.common.by import By
from base.Basedriver import BaseDriver


class Landing_page(BaseDriver):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.wait = wait
        self.driver = driver

    # Locators
    SIGN_UP = "//button[text()='Sign Up']"
    PRODUCTS = "//button[text()='Products']"

    RESUME_BUILDER = "//body/div[5]/div[2]/div/div/div/div/a[1]"
    OPEN_FILTER = "//*[@id='root']/div/div[2]/div/div[2]/div[1]/div[1]//button"
    CLOSE_FILTER = "//*[@id='root']/div/div[2]/div/div[2]/div[1]//button"
    CHOOSE_COLOR = "//*[@id='root']/div/div[2]/div/div[2]/div[1]/div[2]//span[1]"   # WE HAVE 12 COLORS

    HIRE_RESUME_WRITER = "//body/div[5]/div[2]/div/div/div/div/a[2]"
    GET_STARTED = "//*[@id='root']/div/div[2]/div/div/div/div/div[1]//button[1]"
    BUY_NOW = "//*[@id='root']/div/div[2]/div/div/div/div/div[1]//button[2]"
    BUY_NOW_FRESHER = "//*[@id='root']/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[1]//button[1]"
    ENQUIRY_NOW_FRESHER = "//*[@id='root']/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[1]//button[2]"
    BUY_NOW_EXPERIENCE = "//*[@id='root']/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]//button[1]"
    ENQUIRY_NOW_EXPERIENCE = "//*[@id='root']/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]//button[2]"
    FORM_NAME = "//body/div[5]/div[3]/div/section/div/div/div[1]//input"
    FORM_EMAIL = "//body/div[5]/div[3]/div/section/div/div/div[2]//input"
    FORM_NUMBER = "//body/div[5]/div[3]/div/section/div/div/div[3]//input"
    FORM_TEXT = "//body/div[5]/div[3]/div/section/div/div/div[4]//textarea"
    SUBMIT_BUTTON = "//button[text()='Submit']"

    PERSONALITY_ASSESSMENT = "//body/div[5]/div[2]/div/div/div/div/a[3]"

    LINKDIN_OPTIMIZATION = "//body/div[5]/div[2]/div/div/div/div/a[1]"

    CLICK_RESUME = "//*[@id='root']/div/div[2]/div/div[2]/div[2]/div/div[{i}]/div"  # WE HAVE 21 RESUMES
    CHOOSE_TEMPLATE = "//button[text()='Choose Template']"
    CLOSE_POPUP = "//button[@aria-label='Close']"

    """GETTERS"""

    def get_products(self):
        return self.element_to_click(By.XPATH, self.PRODUCTS)

    def get_resumebuilder(self):
        return self.element_to_click(By.XPATH, self.RESUME_BUILDER)

    def get_hireresumewriter(self):
        return self.element_to_click(By.XPATH, self.HIRE_RESUME_WRITER)

    def get_getstarted(self):
        return self.element_to_click(By.XPATH, self.GET_STARTED)

    def get_buynowfresher(self):
        return self.element_to_click(By.XPATH, self.BUY_NOW_FRESHER)

    def get_enquirynowfresher(self):
        return self.element_to_click(By.XPATH, self.ENQUIRY_NOW_FRESHER)

    def get_buynowexperience(self):
        return self.element_to_click(By.XPATH, self.BUY_NOW_EXPERIENCE)

    def get_enquirynowexperience(self):
        return self.element_to_click(By.XPATH, self.ENQUIRY_NOW_EXPERIENCE)

    def get_personlaityassessment(self):
        return self.element_to_click(By.XPATH, self.PERSONALITY_ASSESSMENT)

    def get_lindinoptimization(self):
        return self.element_to_click(By.XPATH, self.LINKDIN_OPTIMIZATION)

    def get_signup(self):
        return self.element_to_click(By.XPATH, self.SIGN_UP)

    def get_openfiletr(self):
        return self.element_to_click(By.XPATH, self.OPEN_FILTER)

    def get_closefilter(self):
        return self.element_to_click(By.XPATH, self.CLOSE_FILTER)

    def get_choosecolor(self, i):
        return self.element_to_click(By.XPATH, f"//*[@id='root']/div/div[2]/div/div[2]/div[1]/div[2]/div/label[{i}]//span")

    def get_clickresume(self, j):
        return self.element_to_click(By.XPATH, f"//*[@id='root']/div/div[2]/div/div[2]/div[2]/div/div[{j}]/div")

    def get_choosetemplate(self):
        return self.element_to_click(By.XPATH, self.CHOOSE_TEMPLATE)

    def get_closepopup(self):
        return self.element_to_click(By.XPATH, self.CLOSE_POPUP)

    def get_formname(self):
        return self.element_to_click(By.XPATH, self.FORM_NAME)

    def get_formemail(self):
        return self.element_to_click(By.XPATH, self.FORM_EMAIL)

    def get_formnumber(self):
        return self.element_to_click(By.XPATH, self.FORM_NUMBER)

    def get_formtext(self):
        return self.element_to_click(By.XPATH, self.FORM_TEXT)

    def get_submitbutton(self):
        return self.element_to_click(By.XPATH, self.SUBMIT_BUTTON)

    """SETTERS"""

    def click_productslink(self):
        self.get_products().click()

    def click_resumebuilder(self):
        self.get_resumebuilder().click()

    def click_hireresumewriter(self):
        self.get_hireresumewriter().click()

    def click_getstarted(self):
        self.get_getstarted().click()

    def click_buynowfresher(self):
        self.get_buynowfresher().click()

    def click_enquirynowfresher(self):
        self.get_enquirynowfresher().click()

    def enter_formname(self, name):
        self.get_formname().click()
        self.get_formname().send_keys(name)

    def enter_formemail(self, email):
        self.get_formemail().click()
        self.get_formemail().send_keys(email)

    def enter_formnumber(self, number):
        self.get_formnumber().click()
        self.get_formnumber().send_keys(number)

    def enter_formtext(self, text):
        self.get_formtext().click()
        self.get_formtext().send_keys(text)

    def click_submitbutton(self):
        self.get_submitbutton().click()

    def click_buynowexperience(self):
        self.get_buynowexperience().click()

    def click_enquirynowexperience(self):
        self.get_enquirynowexperience().click()

    def click_personalityassessment(self):
        self.get_personlaityassessment().click()

    def click_linkdinoptimization(self):
        self.get_lindinoptimization().click()

    def click_signup(self):
        self.get_signup().click()

    def click_openfilter(self):
        self.get_openfiletr().click()

    def click_closefilter(self):
        self.get_closefilter().click()

    def click_choosecolor(self, i):
        self.get_choosecolor(i).click()

    def click_clickresume(self, j):
        self.get_clickresume(j).click()

    def click_chossetemplate(self):
        self.get_choosetemplate().click()

    def click_closepopup(self):
        self.get_closepopup().click()

    def landingpage(self, name, email, number, text):
        self.click_signup()
        time.sleep(2)
        self.driver.back()

        # Resume Builder
        self.click_productslink()
        time.sleep(2)
        self.click_resumebuilder()
        time.sleep(1)
        self.click_closefilter()
        time.sleep(2)
        self.click_openfilter()
        for i in range(1, 12):
            self.click_choosecolor(i)
            time.sleep(2)
            self.click_choosecolor(i)
        for j in range(1, 22):
            self.click_clickresume(j)
            time.sleep(2)
            if j <= 11:
                self.click_chossetemplate()
                time.sleep(2)
                self.driver.back()
            else:
                self.click_closepopup()
        time.sleep(2)

        # Hire Resume writer
        self.click_productslink()
        time.sleep(2)
        self.click_hireresumewriter()
        self.click_getstarted()
        self.click_buynowfresher()
        time.sleep(2)
        self.driver.back()
        self.click_enquirynowfresher()
        self.enter_formname(name)
        self.enter_formemail(email)
        self.enter_formnumber(number)
        self.enter_formtext(text)
        self.click_submitbutton()
        time.sleep(2)

        self.click_buynowexperience()
        time.sleep(2)
        self.driver.back()
        self.click_enquirynowexperience()
        self.enter_formname(name)
        self.enter_formemail(email)
        self.enter_formnumber(number)
        self.enter_formtext(text)
        self.click_submitbutton()
        time.sleep(2)

        # Personality assessment
        self.click_productslink()
        time.sleep(2)
        self.click_personalityassessment()
        time.sleep(2)
        self.driver.back()

        # Linkdin optimization
        self.click_productslink()
        time.sleep(2)
        self.page_down()
        time.sleep(3)








