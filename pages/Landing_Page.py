import time
from pages.Membership_page import Membership
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Landing_page(Membership):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.wait = wait
        self.driver = driver

    # Locators
    SIGN_UP = "//button[text()='Sign Up']"
    PRODUCTS = "//button[text()='Products']"

    RESUME_BUILDER = "//body/div[4]/div[2]/div/div/div/div/a[1]"

    # div[5] for talent-place.ai, as we are not using zoho, zoho chat takes 3 div in middle.[for all 4 links.]
    # div[5] from resume-writer. div[4] in templates. for links products..

    OPEN_FILTER = "//*[@id='root']/div/div[2]/div/div[2]/div[1]/div[1]//button"
    CLOSE_FILTER = "//*[@id='root']/div/div[2]/div/div[2]/div[1]//button"
    CHOOSE_COLOR = "//*[@id='root']/div/div[2]/div/div[2]/div[1]/div[2]//span[1]"  # WE HAVE 12 COLORS

    HIRE_RESUME_WRITER = "//body/div[5]/div[2]/div/div/div/div/a[2]"                    # in templates[4], in writer [5]
    GET_STARTED = "//*[@id='root']/div/div[2]/div/div/div/div/div[1]//button[1]"
    BUY_NOW_PROFESSIONAL = "//*[@id='root']/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[1]//button[1]"

    BILLING_NAME = "//body/div[5]//section//form/div/div/div[1]//input"
    BILLING_COUNTRY = "//body/div[5]//section//form/div/div/div[2]//input"
    BILLING_STATE = "//body/div[5]//section//form/div/div/div[3]//input"
    BILLING_CITY = "//body/div[5]//section//form/div/div/div[4]//input"
    BILLING_STREET = "//body/div[5]//section//form/div/div/div[5]//input"
    BILLING_ZIPCODE = "//body/div[5]//section//form/div/div/div[6]//input"
    PROCEED_BUTTON = "//body/div[5]//section//form/div/button"
    BILLINGFORM_CLOSE_POPUP = "//body/div[5]//section/button[1]"
    ENQUIRY_NOW_PROFESSIONAL = "//*[@id='root']/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[1]//button[2]"
    BUY_NOW_FRESHER = "//*[@id='root']/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]//button[1]"
    ENQUIRY_NOW_FRESHER = "//*[@id='root']/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]//button[2]"

    FORM_NAME = "//body/div[5]/div[3]/div/section/div/div/div[1]//input"  # same above content for forms as well
    FORM_EMAIL = "//body/div[5]/div[3]/div/section/div/div/div[2]//input"
    FORM_NUMBER = "//body/div[5]/div[3]/div/section/div/div/div[3]//input"
    FORM_TEXT = "//body/div[5]/div[3]/div/section/div/div/div[4]//textarea"
    SUBMIT_BUTTON = "//button[text()='Submit']"

    PERSONALITY_ASSESSMENT = "//body/div[5]/div[2]/div/div/div/div/a[3]"

    LINKDIN_OPTIMIZATION = "//body/div[5]/div[2]/div/div/div/div/a[4]"

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

    def get_buynowprofessional(self):
        return self.element_to_click(By.XPATH, self.BUY_NOW_PROFESSIONAL)

    def get_enquirynowprofessional(self):
        return self.element_to_click(By.XPATH, self.ENQUIRY_NOW_PROFESSIONAL)

    def get_buynowfresher(self):
        return self.element_to_click(By.XPATH, self.BUY_NOW_FRESHER)

    def get_enquirynowfresher(self):
        return self.element_to_click(By.XPATH, self.ENQUIRY_NOW_FRESHER)

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
        return self.element_to_click(By.XPATH,
                                     f"//*[@id='root']/div/div[2]/div/div[2]/div[1]/div[2]/div/label[{i}]//span")

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

    def get_billingname(self):
        return self.element_to_click(By.XPATH, self.BILLING_NAME)

    def get_billingcountry(self):
        return self.element_to_click(By.XPATH, self.BILLING_COUNTRY)

    def get_billingcity(self):
        return self.element_to_click(By.XPATH, self.BILLING_CITY)

    def get_billingstate(self):
        return self.element_to_click(By.XPATH, self.BILLING_STATE)

    def get_billingstreet(self):
        return self.element_to_click(By.XPATH, self.BILLING_STREET)

    def get_billingzipcode(self):
        return self.element_to_click(By.XPATH, self.BILLING_ZIPCODE)

    def get_proceedbutton(self):
        return self.element_to_click(By.XPATH, self.PROCEED_BUTTON)

    def get_billingformclosepopup(self):
        return self.element_to_click(By.XPATH, self.BILLINGFORM_CLOSE_POPUP)

    """SETTERS"""

    def click_productslink(self):
        self.get_products().click()

    def click_resumebuilder(self):
        self.get_resumebuilder().click()

    def click_hireresumewriter(self):
        self.get_hireresumewriter().click()

    def click_getstarted(self):
        self.get_getstarted().click()

    def click_buynowprofessional(self):
        self.get_buynowprofessional().click()

    def click_enquirynowprofessional(self):
        self.get_enquirynowprofessional().click()

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

    def click_buynowfresher(self):
        self.get_buynowfresher().click()

    def click_enquirynowfresher(self):
        self.get_enquirynowfresher().click()

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

    def enter_billingname(self, name):
        self.get_billingname().click()
        self.get_billingname().send_keys(name)
        self.get_billingname().send_keys(Keys.TAB)

    def enter_billingcountry(self, country):
        self.get_billingcountry().click()
        self.get_billingcountry().send_keys(country)
        self.get_billingcountry().send_keys(Keys.ARROW_DOWN)
        self.get_billingcountry().send_keys(Keys.ENTER)

    def enter_billingstate(self, state):
        self.get_billingstate().click()
        self.get_billingstate().send_keys(state)
        self.get_billingstate().send_keys(Keys.ARROW_DOWN)
        self.get_billingstate().send_keys(Keys.ENTER)

    def enter_billingcity(self, city):
        self.get_billingcity().click()
        self.get_billingcity().send_keys(city)
        self.get_billingcity().send_keys(Keys.TAB)

    def enter_billingstreet(self, street):
        self.get_billingstreet().click()
        self.get_billingstreet().send_keys(street)
        self.get_billingstreet().send_keys(Keys.TAB)

    def enter_billingzipcode(self, zipcode):
        self.get_billingzipcode().click()
        self.get_billingzipcode().send_keys(zipcode)
        self.get_billingzipcode().send_keys(Keys.TAB)

    def click_proceedbutton(self):
        self.get_proceedbutton().click()

    def click_billingfromclosepopup(self):
        self.get_billingformclosepopup().click()

    def enter_billingform(self, name, country, city, state, street, zipcode):
        parent_wind = self.driver.current_window_handle
        time.sleep(2)
        self.enter_billingname(name)
        self.enter_billingcountry(country)
        self.enter_billingcity(city)
        self.enter_billingstate(state)
        self.enter_billingstreet(street)
        self.enter_billingzipcode(zipcode)
        self.click_proceedbutton()
        time.sleep(3)
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != parent_wind:
                self.driver.switch_to.window(handle)
                self.page_end()
                self.click_subscribe()
                time.sleep(2)
                self.click_closetab()
                time.sleep(2)
                break
        self.driver.switch_to.window(parent_wind)

    def landingpage(self, name, email, number, text, country, state, city, street, zipcode):
        self.click_signup()
        time.sleep(2)
        self.driver.back()

        # # # Resume Builder
        self.click_productslink()
        time.sleep(2)
        self.click_resumebuilder()
        time.sleep(1)
        self.click_closefilter()
        time.sleep(2)
        self.click_openfilter()
        self.page_down()
        for i in range(1, 8):
            self.click_choosecolor(i)
            time.sleep(2)
            self.click_choosecolor(i)
        for j in range(1, 22):
            self.click_clickresume(j)
            time.sleep(2)
            if j <= 11:
                self.click_chossetemplate()
                time.sleep(2)
                self.page_back()
            else:
                self.click_closepopup()
        time.sleep(2)

        # Hire Resume writer
        self.click_productslink()
        time.sleep(2)
        self.click_hireresumewriter()
        self.click_getstarted()
        self.click_buynowprofessional()
        time.sleep(2)
        self.login()
        time.sleep(2)
        self.enter_billingform(name, country, city, state, street, zipcode)
        self.click_billingfromclosepopup()
        self.page_down()
        time.sleep(5)
        self.click_enquirynowprofessional()
        self.enter_formname(name)
        self.enter_formemail(email)
        self.enter_formnumber(number)
        self.enter_formtext(text)
        self.click_submitbutton()
        time.sleep(2)

        self.click_productslink()
        time.sleep(2)
        self.click_hireresumewriter()
        self.click_buynowfresher()
        self.enter_billingform(name, country, city, state, street, zipcode)
        self.click_billingfromclosepopup()
        time.sleep(2)
        self.page_down()
        self.click_enquirynowfresher()
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
        self.click_linkdinoptimization()
        self.page_end()
        self.page_up()
        time.sleep(3)
        # THANK-YOU
