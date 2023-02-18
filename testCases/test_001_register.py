from pageObject.RegisterPage import RegisterPage
from selenium.webdriver.common.by import By
from faker import Faker

fake = Faker()

class Test_001_Register:
    baseURL = "https://automationexercise.com/"
    name = "Kim"
    email = fake.email()
    gender = "Mrs."
    password = fake.password(length=12, digits=True, upper_case=True, lower_case=True)
    day = "12"
    month = "March"
    year = "2000"
    first_name = "Kim"
    last_name = "Brown"
    address = "Private Drive 15"
    country = "Canada"
    state = "Canada"
    city = "Ontario"
    zipcode = fake.zipcode()
    mobile_number = f"{fake.random_number(digits=3)}-{fake.random_number(digits=3)}-{fake.random_number(digits=4)}"


    def test_homePageVisibility(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        act_title = self.driver.title
        assert "Automation Exercise" in act_title
        self.driver.close()

    def test_register(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.register = RegisterPage(self.driver)
        self.register.clickOnSignUpLoginButton()
        new_user_title = self.driver.find_element(By.XPATH, "//body").text
        assert "New User Signup!" in new_user_title

        self.register.setName(self.name)
        self.register.setEmail(self.email)
        self.register.clickSignUpButton()
        enter_info_title = self.driver.find_element(By.XPATH, "//body").text
        assert "ENTER ACCOUNT INFORMATION" in enter_info_title

        self.register.setGender(self.gender)
        self.register.setPassword(self.password)
        self.register.setDay(self.day)
        self.register.setMonth(self.month)
        self.register.setYear(self.year)
        self.register.setCheckbox1()
        self.register.setCheckbox2()
        self.register.setFirstName(self.first_name)
        self.register.setLastName(self.last_name)
        self.register.setAddress(self.address)
        self.register.setCountry(self.country)
        self.register.setState(self.state)
        self.register.setCity(self.city)
        self.register.setZipcode(self.zipcode)
        self.register.setMobileNumber(self.mobile_number)
        self.register.clickCreateAccount()
        account_created_title = self.driver.find_element(By.XPATH, "//body").text
        assert "ACCOUNT CREATED!" in account_created_title
        self.register.clickContinue()
        self.driver.implicitly_wait(10)
        # self.register.clickDeleteAccount()
        # account_deleted_title = self.driver.find_element(By.XPATH, "//body").text
        # assert "ACCOUNT DELETED!" in account_deleted_title
        # self.register.clickContinue()
        # act_title = self.driver.title
        # if act_title == "Automation Exercise":
        #     assert True
        #     self.driver.close()
        # else:
        #     self.driver.close()
        #     assert False
        self.driver.close()


