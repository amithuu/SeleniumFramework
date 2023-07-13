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
    CLICK_RESUME = "//*[@id='root']/div/div[2]/div/div[2]/div[2]/div/div[{i}]/div"  # WE HAVE 21 RESUMES
    CHOOSE_TEMPLATE = "//button[text()='Choose Template']"
    CLOSE_POPUP = "//button[@aria-label='Close']"

    HIRE_RESUME_WRITER = "//body/div[5]/div[2]/div/div/div/div/a[2]"                    # in templates[4], in writer [5]
    GET_STARTED = "//*[@id='root']/div/div[2]/div/div/div/div/div[1]//button[1]"
    ENTRY_LEVEL_FEATURES = "//*[@id='root']/div/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div[3]//button"
    ENTRY_LEVEL_ORDERNOW_BUTTON = "//*[@id='root']/div/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div[4]//button"
    MID_LEVEL_FEATURES = "//*[@id='root']/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[3]//button"
    MID_LEVEL_ORDERNOW_BUTTON = "//*[@id='root']/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[4]//button"
    PROFESSIONALS_LEVEL_FEATURES = "//*[@id='root']/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/div[3]//button"
    PROFESSIONALS_LEVEL_ORDERNOW_BUTTON = "//*[@id='root']/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/div[4]//button"

    RESUME_REVIEW = "//*[@id='root']/div/div[2]/div/div[3]//button"

    EXPLORE_RESUME_TEMPLATES = "//*[@id='root']/div/div[2]/div/div[7]//button"
    CLOSE_POPUP_RESUME_EXPLORE = "//button[@aria-label='Close']"
    CLOSE_POPUP_BILLING_EXPLORE = "//body/div[6]//section/button"
    PRIME_RESUME_ENTRY_LEVEL_FEATURES = "//body/div[5]/div/div/div/div/div/div[2]/div/div/div[1]/div[3]//button"
    PRIME_RESUME_ENTRY_LEVEL_ORDERNOW_BUTTON = "//body/div[5]/div/div/div/div/div/div[2]/div/div/div[1]/div[4]//button"
    PRIME_RESUME_MID_LEVEL_FEATURES = "//body/div[5]/div/div/div/div/div/div[2]/div/div/div[2]/div[3]//button"
    PRIME_RESUME_MID_LEVEL_ORDERNOW_BUTTON = "//body/div[5]/div/div/div/div/div/div[2]/div/div/div[2]/div[4]//button"
    PRIME_RESUME_PROFESSIONALS_LEVEL_FEATURES = "//body/div[5]/div/div/div/div/div/div[2]/div/div/div[3]/div[3]//button"
    PRIME_RESUME_PROFESSIONALS_LEVEL_ORDERNOW_BUTTON = "//body/div[5]/div/div/div/div/div/div[2]/div/div/div[3]/div[4]//button"

    BILLING_NAME = f"//body/div[5/6]//section//form/div/div/div[1]//input"
    BILLING_COUNTRY = f"//body/div[5/6]//section//form/div/div/div[2]//input"
    BILLING_STATE = f"//body/div[5/6]//section//form/div/div/div[3]//input"
    BILLING_CITY = f"//body/div[5/6]//section//form/div/div/div[4]//input"
    BILLING_STREET = f"//body/div[5/6]//section//form/div/div/div[5]//input"
    BILLING_ZIPCODE = f"//body/div[5/6]//section//form/div/div/div[6]//input"
    PROCEED_BUTTON = f"//body/div[5/6]//section//form/div/button"
    BILLINGFORM_CLOSE_POPUP = f"//body/div[5/6]//section/button[1]"
    SUCCESS_LANDING_PAGE = "//a[text()='Success']"

    FORM_NAME = "//body/div[5]/div[3]/div/section/div/div/div[1]//input"  # same above content for forms as well
    FORM_EMAIL = "//body/div[5]/div[3]/div/section/div/div/div[2]//input"
    FORM_NUMBER = "//body/div[5]/div[3]/div/section/div/div/div[3]//input"
    UPLOAD_RESUME = "//body/div[5]/div[3]/div/section/div/div/div[4]//u"
    SUBMIT_BUTTON = "//button[text()='Submit']"

    PERSONALITY_ASSESSMENT = "//body/div[5]/div[2]/div/div/div/div/a[3]"

    LINKDIN_OPTIMIZATION = "//body/div[5]/div[2]/div/div/div/div/a[4]"

    """GETTERS"""

    def get_products(self):
        return self.element_to_click(By.XPATH, self.PRODUCTS)

    def get_resumebuilder(self):
        return self.element_to_click(By.XPATH, self.RESUME_BUILDER)

    def get_hireresumewriter(self):
        return self.element_to_click(By.XPATH, self.HIRE_RESUME_WRITER)

    def get_getstarted(self):
        return self.element_to_click(By.XPATH, self.GET_STARTED)

    def get_entrylevelfeatures(self):
        return self.element_to_click(By.XPATH, self.ENTRY_LEVEL_FEATURES)

    def get_entrylevelbutton(self):
        return self.element_to_click(By.XPATH, self.ENTRY_LEVEL_ORDERNOW_BUTTON)

    def get_midlevelfeatures(self):
        return self.element_to_click(By.XPATH, self.MID_LEVEL_FEATURES)

    def get_midlevelbutton(self):
        return self.element_to_click(By.XPATH, self.MID_LEVEL_ORDERNOW_BUTTON)

    def get_professionallevelfeatures(self):
        return self.element_to_click(By.XPATH, self.PROFESSIONALS_LEVEL_FEATURES)

    def get_professionallevelbutton(self):
        return self.element_to_click(By.XPATH, self.PROFESSIONALS_LEVEL_ORDERNOW_BUTTON)

    def get_resumereview(self):
        return self.element_to_click(By.XPATH, self.RESUME_REVIEW)

    def get_exploreresumetemplatesbutton(self):
        return self.element_to_click(By.XPATH, self.EXPLORE_RESUME_TEMPLATES)

    def get_prime_entrylevelfeatures(self):
        return self.element_to_click(By.XPATH, self.PRIME_RESUME_ENTRY_LEVEL_FEATURES)

    def get_prime_entrylevelbutton(self):
        return self.element_to_click(By.XPATH, self.PRIME_RESUME_ENTRY_LEVEL_ORDERNOW_BUTTON)

    def get_prime_midlevelfeatures(self):
        return self.element_to_click(By.XPATH, self.PRIME_RESUME_MID_LEVEL_FEATURES)

    def get_prime_midlevelbutton(self):
        return self.element_to_click(By.XPATH, self.PRIME_RESUME_MID_LEVEL_ORDERNOW_BUTTON)

    def get_prime_professionallevelfeatures(self):
        return self.element_to_click(By.XPATH, self.PRIME_RESUME_PROFESSIONALS_LEVEL_FEATURES)

    def get_prime_professionallevelbutton(self):
        return self.element_to_click(By.XPATH, self.PRIME_RESUME_PROFESSIONALS_LEVEL_ORDERNOW_BUTTON)

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

    def get_uploadresume(self):
        return self.element_to_click(By.XPATH, self.UPLOAD_RESUME)

    def get_submitbutton(self):
        return self.element_to_click(By.XPATH, self.SUBMIT_BUTTON)

    def get_billingname(self, i):
        return self.element_to_click(By.XPATH, f"//body/div[{i}]//section//form/div/div/div[1]//input")

    def get_billingcountry(self, i):
        return self.element_to_click(By.XPATH, f"//body/div[{i}]//section//form/div/div/div[2]//input")

    def get_billingstate(self, i):
        return self.element_to_click(By.XPATH, f"//body/div[{i}]//section//form/div/div/div[3]//input")

    def get_billingcity(self, i):
        return self.element_to_click(By.XPATH, f"//body/div[{i}]//section//form/div/div/div[4]//input")

    def get_billingstreet(self, i):
        return self.element_to_click(By.XPATH, f"//body/div[{i}]//section//form/div/div/div[5]//input")

    def get_billingzipcode(self, i):
        return self.element_to_click(By.XPATH, f"//body/div[{i}]//section//form/div/div/div[6]//input")

    def get_proceedbuttonlandingpage(self, i):
        return self.element_to_click(By.XPATH, f"//body/div[{i}]//section//form/div/button")

    def get_billingformclosepopup(self, i):
        return self.element_to_click(By.XPATH, f"//body/div[{i}]//section/button[1]")

    def get_successlinklandingpage(self):
        return self.element_to_click(By.XPATH, self.SUCCESS_LANDING_PAGE)

    """SETTERS"""

    def click_productslink(self):
        self.get_products().click()

    def click_resumebuilder(self):
        self.get_resumebuilder().click()

    def click_hireresumewriter(self):
        self.get_hireresumewriter().click()

    def click_getstarted(self):
        self.get_getstarted().click()

    def click_entrylevel(self):
        self.get_entrylevelfeatures().click()
        time.sleep(1)
        self.get_entrylevelfeatures().click()
        self.get_entrylevelbutton().click()

    def click_midlevel(self):
        time.sleep(25)
        self.get_midlevelfeatures().click()
        time.sleep(1)
        self.get_midlevelfeatures().click()
        self.get_midlevelbutton().click()

    def click_professionallevel(self):
        self.get_professionallevelfeatures().click()
        time.sleep(1)
        self.get_professionallevelfeatures().click()
        self.get_professionallevelbutton().click()

    def click_exploreresumetemplates(self):
        self.get_exploreresumetemplatesbutton().click()

    def click_prime_entrylevel(self):
        self.get_prime_entrylevelfeatures().click()
        time.sleep(1)
        self.get_prime_entrylevelfeatures().click()
        self.get_prime_entrylevelbutton().click()

    def click_prime_midlevel(self):
        self.get_prime_midlevelfeatures().click()
        time.sleep(1)
        self.get_prime_midlevelfeatures().click()
        self.get_prime_midlevelbutton().click()

    def click_prime_professionallevel(self):
        self.get_prime_professionallevelfeatures().click()
        time.sleep(1)
        self.get_prime_professionallevelfeatures().click()
        self.get_prime_professionallevelbutton().click()

    def click_resumereview(self):
        self.get_resumereview().click()

    def enter_formname(self, name):
        self.get_formname().click()
        self.get_formname().send_keys(name)

    def enter_formemail(self, email):
        self.get_formemail().click()
        self.get_formemail().send_keys(email)

    def enter_formnumber(self, number):
        self.get_formnumber().click()
        self.get_formnumber().send_keys(number)

    def click_uploadresume(self):
        self.get_uploadresume().click()

    def click_submitbutton(self):
        self.get_submitbutton().click()

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

    def click_successlinklandingpage(self):
        self.get_successlinklandingpage().click()

    def enter_billingname(self, name, i):
        self.get_billingname(i).click()
        self.get_billingname(i).send_keys(name)
        self.get_billingname(i).send_keys(Keys.TAB)

    def enter_billingcountry(self, country, i):
        self.get_billingcountry(i).click()
        self.get_billingcountry(i).send_keys(country)
        self.get_billingcountry(i).send_keys(Keys.ARROW_DOWN)
        self.get_billingcountry(i).send_keys(Keys.ENTER)

    def enter_billingstate(self, state, i):
        self.get_billingstate(i).click()
        self.get_billingstate(i).send_keys(state)
        self.get_billingstate(i).send_keys(Keys.ARROW_DOWN)
        self.get_billingstate(i).send_keys(Keys.ENTER)

    def enter_billingcity(self, city, i):
        self.get_billingcity(i).click()
        self.get_billingcity(i).send_keys(city)
        self.get_billingcity(i).send_keys(Keys.TAB)

    def enter_billingstreet(self, street, i):
        self.get_billingstreet(i).click()
        self.get_billingstreet(i).send_keys(street)
        self.get_billingstreet(i).send_keys(Keys.TAB)

    def enter_billingzipcode(self, zipcode, i):
        self.get_billingzipcode(i).click()
        self.get_billingzipcode(i).send_keys(zipcode)
        self.get_billingzipcode(i).send_keys(Keys.TAB)

    def click_proceedbutton(self, i):
        self.get_proceedbuttonlandingpage(i).click()

    def click_billingfromclosepopup(self, i):
        self.get_billingformclosepopup(i).click()

    def enter_billingform(self, name, country, state, city, street, zipcode, i):
        parent_wind = self.driver.current_window_handle
        time.sleep(2)
        self.enter_billingname(name, i)
        self.enter_billingcountry(country, i)
        self.enter_billingstate(state, i)
        self.enter_billingcity(city, i)
        self.enter_billingstreet(street, i)
        self.enter_billingzipcode(zipcode, i)
        self.click_proceedbutton(i)
        time.sleep(3)
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != parent_wind:
                self.driver.switch_to.window(handle)
                self.page_end()
                time.sleep(5)
                self.click_successlinklandingpage()
                time.sleep(2)
                self.click_subscribe()
                time.sleep(2)
                self.click_closetab()
                time.sleep(2)
                break
        self.driver.switch_to.window(parent_wind)

    def landingpage(self, name, email, number, country, state, city, street, zipcode):
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
        # self.click_productslink()
        # time.sleep(2)
        # self.click_hireresumewriter()
        # self.click_getstarted()
        # time.sleep(3)
        # self.click_entrylevel()
        # time.sleep(2)
        # # self.login()
        # # time.sleep(2)
        # # self.enter_billingform(name, country, state, city, street, zipcode, 5)
        # # self.click_billingfromclosepopup(5)
        # self.page_down()
        # time.sleep(5)

        self.click_productslink()
        time.sleep(2)
        self.click_hireresumewriter()
        self.click_midlevel()
        time.sleep(2)
        self.login()
        time.sleep(1)
        self.enter_billingform(name, country, state, city, street, zipcode, 5)
        self.click_billingfromclosepopup(5)
        time.sleep(2)
        self.page_down()

        self.click_productslink()
        self.click_hireresumewriter()
        self.page_down()
        self.click_professionallevel()
        time.sleep(1)
        self.enter_billingform(name, country, state, city, street, zipcode, 5)
        self.click_billingfromclosepopup(5)
        time.sleep(2)
        self.page_down()
        self.page_down()

        #  Free Resume Review
        self.click_resumereview()
        self.enter_formname(name)
        self.enter_formemail(email)
        self.enter_formnumber(number)
        self.click_uploadresume()
        self.click_submitbutton()
        self.page_down()
        self.page_down()

        self.click_exploreresumetemplates()
        self.page_down()
        for j in range(1, 22):
            self.click_clickresume(j)
            time.sleep(2)
            if j == 1:
                self.click_prime_entrylevel()
                # self.enter_billingform(name, country, state, city, street, zipcode, 6)
                self.click_billingfromclosepopup(6)
                time.sleep(2)
                self.click_closepopup()
            elif j == 2:
                self.click_prime_midlevel()
                # self.enter_billingform(name, country, state, city, street, zipcode, 6)
                self.click_billingfromclosepopup(6)
                time.sleep(2)
                self.click_closepopup()
            elif j == 3:
                self.click_prime_professionallevel()
                # self.enter_billingform(name, country, state, city, street, zipcode, 6)
                self.click_billingfromclosepopup(6)
                time.sleep(2)
                self.click_closepopup()
            else:
                self.click_closepopup()
        time.sleep(2)

        # Personality assessment
        self.click_productslink()
        time.sleep(2)
        self.click_personalityassessment()
        time.sleep(2)
        self.driver.back()
        self.driver.back()
        self.driver.back()

        # Linkdin optimization
        self.click_productslink()
        time.sleep(2)
        self.click_linkdinoptimization()
        self.page_end()
        self.page_up()
        time.sleep(3)
        # THANK-YOU
