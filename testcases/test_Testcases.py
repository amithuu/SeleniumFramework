import pytest
from ddt import ddt
from pages.Assessment_page import Assessment
from pages.Carriersummary_page import Carrier
from pages.Causes_page import Causes
from pages.Certificate_page import Certificate
from pages.Cognitiveskills_page import CognitiveSkills
from pages.Education_page import Education
from pages.Hobbies_page import Hobbies
from pages.HonorAwards_page import HonorAwards
from pages.Jobrole_page import JobRole
from pages.Landing_Page import Landing_page
from pages.Languages_page import Language
from pages.Membership_page import Membership
from pages.Myprofie_page import MyProfile
from pages.Patents_page import Patent
from pages.Personaldetails_page import Personaldetails
from pages.Portfolio_page import Portfolio
from pages.Profile_picture import Profile_picture
from pages.Project_page import Projects
from pages.Publication_page import Publication
from pages.Resume_page import Resume
from pages.Settings_page import Setting
from pages.SignUp_page import Signup
from pages.EditProfiles_page import EditProfiles
from pages.VoluntaryRoles_page import VoluntaryRoles
from pages.Welcome_page import Welcome

# Variables
user = ["new", "old", "Renew"]
companyname = ["ibm", "google", "cognizant"]
jobtype = ["full time", "intern", "part time", "freelancing", "contract"]
industry = ["advanced", "automation", "agri"]
organization = ["startup", "small", "medium", "large", "mnc"]
based = ["product", "service", "both"]
month = ["month", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
year = ["1900", "1910", "1920", "1930", "1940", "2000", "2001", "2002", "2020", "2023"]
designation = ["developer", "automation", "manualtester", "frontend", "backend"]
managementlevel = ["cxo", "jun", "sen", "mid", "owner"]
functionalarea = ["administ", "customer", "development", "distribution", "finance", "human", "ict", "management", "marketing", "production"]
skill = ["java", "python", "c prog", "automation", "php"]
expertise = ["beg", "average", "skil", "expert", "advanced"]
startsalary = ["12", "3213", "214", "213", "543"]
endsalary = ["21433", "2136832", "812765", "323544", "435345546"]

degree = ["10th", "12th", "bsc", "mca", "phd"]
university = ["mabl high school", "reva university", "delhi university", "odisha university", "archarya"]
cgpa = ["7.89", "9.65", "5.98", "8.66", "9.59"]
description = ["Listing projects on your resume allows hiring managers", " It's important to list your most relevant projects on your resume.", "List the skills you want to highlight", "Think of the specific projects you want to include.", "Think of the specific projects you want to include."]

project_name = ["talentplace.ai", "face recogniztion system", "line follower robot"]

author_title = ["Mr", "Ms", "Mrs", "Mx"]

category = ["entertainment", "music", "sports", "leisure", "adventure", "travel", "books", "others"]
hobbies = ["Watching cricket", "Motivational songs", "Cricket", " Watching Cricket highlights", "Hill Climbing", "Goa", "The King Virat Kohli", "hanging with friends"]

language = ["kannada", "english", "hindi", "telugu", "european", "bengali", "bihari", "nepali", "german", "zuni"]
proficiency = ["beg", "adv", "inter", "beg", "adv", "inter", "beg", "adv", "inter", "beg"]

plan = ["Trail", "Monthly", "Quarterly", "Year"]
professionalservice = ["Fresher Resume Writing", "Experience Resume Writing", "Linkdin Optimization", "What Job Fits Me"]
servicetype = ["Buynow", "Enquire Now"]
membership_type = ["Resume Builder", "Professional Service"]
user_settings = ["editprofile", "changepassword", "changemobile", "cancelsubsription"]
user_myprofile = ["shareprofile", "downloadresume", "editprofile"]

firstname = "Amith"
lastname = "talentPlace"
location = ["bangalore", "delhi", "sydney", "new york", "oval"]
date = "03251999"
currency = ["inr", "usd"]
gender = ["male", "female", "not mention"]
social_media = ["twitter", "linkdin", "instagram", "facebook", "github", "dribble"]
social_medialink = ["https://twitter.com/AmithKulkarni18", "https://www.linkedin.com/in/amith-kulkarni-1326241b4", "https://instagram.com/AmithKulkarni18", "https://facebook.com/AmithKulkarni18", "https://github.com/amithuu", "https://dribble.com/AmithKulkarni18"]

headline = "Automation Developer"

choose = ["carrier", "assessment"]

k = 77
email = f"autotest{k}@g.co"
phone_no = f"{k}1489921018"
countryname = ["India", "Australia", "Indonesia", "United States"]
password = "New@1234"
confirm_password = "New@1234"


@pytest.mark.usefixtures("setup")
@ddt
class TestCases:
    # Login happens automatically using fixtures!!![for all the forms]
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lang = Language(self.driver, self.wait)
        self.cog = CognitiveSkills(self.driver, self.wait)
        self.tass = Assessment(self.driver, self.wait)
        self.cas = Carrier(self.driver, self.wait)
        self.sup = Signup(self.driver, self.wait)
        self.wcl = Welcome(self.driver, self.wait)
        self.per = Personaldetails(self.driver, self.wait)
        self.job = JobRole(self.driver, self.wait)
        self.prj = Projects(self.driver, self.wait)
        self.edu = Education(self.driver, self.wait)
        self.cert = Certificate(self.driver, self.wait)
        self.pub = Publication(self.driver, self.wait)
        self.pat = Patent(self.driver, self.wait)
        self.port = Portfolio(self.driver, self.wait)
        self.vol = VoluntaryRoles(self.driver, self.wait)
        self.hon = HonorAwards(self.driver, self.wait)
        self.cau = Causes(self.driver, self.wait)
        self.hob = Hobbies(self.driver, self.wait)
        self.edi = EditProfiles(self.driver, self.wait)
        self.res = Resume(self.driver, self.wait)
        self.mem = Membership(self.driver, self.wait)
        self.set = Setting(self.driver, self.wait)
        self.myp = MyProfile(self.driver, self.wait)
        self.lan = Landing_page(self.driver, self.wait)
        self.pic = Profile_picture(self.driver, self.wait)

    # @pytest.mark.signup
    # def test_signUp(self):
    #     self.sup.sign_up(firstname, lastname, email, countryname[1], phone_no, password, confirm_password)

    @pytest.mark.personaldetails
    def test_personal_details(self):
        for i in range(1):
            self.per.personaldetails(user[1], firstname, lastname, location[1], gender[1], date, currency[1], month[4], "2022", social_media[4], social_medialink[4])

    @pytest.mark.profilepicture
    def test_profilepicture(self):
        self.pic.picturestatus(user[1], headline)

    @pytest.mark.editprofiles
    def test_editprofiles(self):
        self.edi.editprofiles(user[1])
        # self.edi.discard()

    @pytest.mark.jobrole
    def test_jobrole(self):
        # self.job.edit_profile()
        self.job.click_experience_editprofile()
        for i in range(3):
            self.job.addcompany(i, user[1], companyname[i], jobtype[i], industry[i], organization[i], based[i], designation[i], managementlevel[i], location[i], functionalarea[i], skill[i], expertise[i], month[i+1], year[i], month[i+1], year[i+1], startsalary[i], endsalary[i])
        self.job.backto_menu()

    @pytest.mark.projects
    def test_projects(self):
        # self.prj.edit_profile()
        for j in range(2):
            self.prj.project(user[1], project_name[j], month[j+1], year[j], month[j+2], year[j+1], companyname[j], social_medialink[j], description[j], skill[j], j, description[j])
        self.prj.backto_menu()

    @pytest.mark.education
    def test_education(self):
        # self.edu.edit_profile()
        for i in range(2):
            self.edu.education(i, user[1], degree[i], university[i], location[i], cgpa[i], month[i+1], year[i], month[i+3], year[i+1], description[i], description[i+1])
        self.edu.backto_menu()

    @pytest.mark.certificate
    def test_certificate(self):
        # self.cert.edit_profile()
        for i in range(2):
            self.cert.certificate(i, user[1], project_name[i], university[i], month[i+1], year[i], month[i+2], year[i+1], skill[i], description[i])
        self.cert.backto_menu()

    @pytest.mark.publication
    def test_publication(self):
        # self.pub.edit_profile()
        for i in range(2):
            self.pub.publication(i, user[1], project_name[i], year[i], date, social_medialink[1], author_title[i], firstname, social_medialink[1], description[i])
        self.pub.backto_menu()

    @pytest.mark.patent
    def test_patent(self):
        # self.pat.edit_profile()
        for i in range(2):
            self.pat.patent(i, user[1], project_name[i], year[i], date, social_medialink[1], author_title[i], firstname, social_medialink[1], description[i])
        self.pat.backto_menu()

    @pytest.mark.portfolio
    def test_portfolio(self):
        # self.port.edit_profile()
        for i in range(2):
            self.port.portfolio(i, user[1], project_name[i], description[i], social_medialink[i])
        self.port.backto_menu()

    @pytest.mark.voluntaryrole
    def test_voluntary_roles(self):
        # self.vol.edit_profile()
        for i in range(2):
            self.vol.voluntaryroles(i, user[1], designation[i], companyname[i], month[i+1], year[i],  month[i+3], year[i+3], description[i])
        self.vol.backto_menu()

    @pytest.mark.honorawards
    def test_honorawards(self):
        # self.hon.edit_profile()
        for i in range(2):
            self.hon.honorawards(i, user[1], designation[i], companyname[i], month[i+6], year[i], companyname[i], description[i])
        self.hon.backto_menu()

    @pytest.mark.causes
    def test_causes(self):
        # self.cau.edit_profile()
        self.cau.causes()
        self.cau.backto_menu()

    @pytest.mark.hobbies
    def test_hobbies(self):
        self.hob.edit_profile()
        for i in range(8):
            self.hob.hobbies(category[i], hobbies[i])

    # @data(("kannada", "adv"), ("english", "beg"))
    # @unpack
    @pytest.mark.language
    def test_languages(self):
        # self.lang.edit_profile()
        for i in range(len(language)):
            self.lang.language(language[i], proficiency[i])

    @pytest.mark.cognitiveskill
    def test_cognitive_skills(self):
        # self.cog.edit_profile()
        self.cog.cognitive()
        self.cog.backto_menu()

    # @pytest.mark.carriersummary
    # def test_carrier(self):
    #     # self.cas.edit_profile()
    #     self.cas.carrier()
    #     self.cas.backto_menu()

    # @pytest.mark.assessment
    # def test_assessment(self):
    #     self.tass.assessment()

    @pytest.mark.resume
    def test_resume(self):
        self.res.filter()
        # for i in range(1, 52):
        #     self.res.resume(i, plan[1])

    # @pytest.mark.membership
    # def test_membership(self):
    #     self.mem.membership("Quarterly", "old", firstname, "india", "karnataka", "bangalore", "15th cross jp nagar", "560078", "Resume Builder", "Fresher Resume Writing", "Buynow")

    @pytest.mark.setting
    def test_setting(self):
        self.set.setting(user_settings[2], "New@12345", "New@1234", "New@1234", countryname[2], phone_no+f"{k+1}")

    # @pytest.mark.myprofile
    # def test_myprofile(self):
    #     self.myp.myprofile(user_myprofile[0])

    # @pytest.mark.welcomepage
    # def test_welcome_page(self):
    #     self.wcl.welcomepage(choose[0])

    # @pytest.mark.landingpage
    # def test_landingpage(self):
    #     self.lan.landingpage(firstname, "autotest61@g.co", date, "india", "karnataka", "bangalore", "15th cross jp nagar", "560078")
