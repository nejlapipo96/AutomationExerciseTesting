from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def clickOnSignupLogin(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Signup / Login']").click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

    def clickDeleteAccount(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Delete Account']").click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()