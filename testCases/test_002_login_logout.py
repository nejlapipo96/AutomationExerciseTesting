from pageObject.LoginPage import LoginPage
from selenium.webdriver.common.by import By

class Test_002_Login:
    baseUrl = "https://automationexercise.com/"
    email = "zreyes@example.org"
    wrong_email = "reyes@example.org"
    password = "K8J(n)d$qpFQ"

    def test_login_valid_email(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        act_title = self.driver.title
        assert "Automation Exercise" in act_title
        self.login = LoginPage(self.driver)
        self.login.clickOnSignupLogin()
        login_title = self.driver.find_element(By.XPATH, "//body").text
        assert "Login to your account" in login_title
        self.login.setEmail(self.email)
        self.login.setPassword(self.password)
        self.login.clickLoginButton()
        # self.login.clickDeleteAccount()
        # account_deleted_title = self.driver.find_element(By.XPATH, "//body").text
        # assert "ACCOUNT DELETED!" in account_deleted_title
        self.login.clickLogout()
        assert "Login to your account" in login_title
        self.driver.close()

    def test_login_invalid_email(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        act_title = self.driver.title
        assert "Automation Exercise" in act_title
        self.login = LoginPage(self.driver)
        self.login.clickOnSignupLogin()
        login_title = self.driver.find_element(By.XPATH, "//body").text
        assert "Login to your account" in login_title
        self.login.setEmail(self.wrong_email)
        self.login.setPassword(self.password)
        self.login.clickLoginButton()
        error_msg = self.driver.find_element(By.XPATH, "//body").text
        assert "Your email or password is incorrect!" in error_msg
        self.driver.close()