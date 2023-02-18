from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def clickOnSignUpLoginButton(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Signup / Login']").click()

    def setName(self, name):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys(name)

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(email)
        print(email)

    def clickSignUpButton(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Signup']").click()

    def setGender(self, gender):
        if gender == "Mr.":
            self.driver.find_element(By.ID, "id_gender1").click()
        elif gender == "Mrs.":
            self.driver.find_element(By.ID, "id_gender2").click()
        else:
            self.driver.find_element(By.ID, "id_gender2").click()

    def setPassword(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)
        print(password)

    def setDay(self, day):
        days = Select(self.driver.find_element(By.ID, "days"))
        days.select_by_visible_text(day)

    def setMonth(self, month):
        months = Select(self.driver.find_element(By.ID, "months"))
        months.select_by_visible_text(month)

    def setYear(self, year):
        years = Select(self.driver.find_element(By.ID, "years"))
        years.select_by_visible_text(year)

    def setCheckbox1(self):
        self.driver.find_element(By.ID, "newsletter").click()

    def setCheckbox2(self):
        self.driver.find_element(By.ID, "optin").click()

    def setFirstName(self, first_name):
        self.driver.find_element(By.ID, "first_name").send_keys(first_name)

    def setLastName(self, last_name):
        self.driver.find_element(By.ID, "last_name").send_keys(last_name)

    def setAddress(self, address):
        self.driver.find_element(By.ID, "address1").send_keys(address)

    def setCountry(self, country):
        select_country = Select(self.driver.find_element(By.ID, "country"))
        select_country.select_by_visible_text(country)

    def setState(self, state):
        self.driver.find_element(By.ID, "state").send_keys(state)

    def setCity(self, city):
        self.driver.find_element(By.ID, "city").send_keys(city)

    def setZipcode(self, zipcode):
        self.driver.find_element(By.ID, "zipcode").send_keys(zipcode)

    def setMobileNumber(self, mobile_number):
        self.driver.find_element(By.ID, "mobile_number").send_keys(mobile_number)

    def clickCreateAccount(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Create Account']").click()
        
    def clickContinue(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Continue']").click()

    def clickDeleteAccount(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Delete Account']").click()


