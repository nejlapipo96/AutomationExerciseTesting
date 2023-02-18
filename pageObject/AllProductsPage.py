from selenium.webdriver.common.by import By

class AllProductsPage:

    def __init__(self, driver):
        self.driver = driver

    def clickOnProducts(self):
        self.driver.find_element(By.XPATH, "//a[@href='/products']").click()

    def firstProduct(self):
        self.driver.find_element(By.XPATH, "//div[@class='col-sm-9 padding-right']//div[2]//div[1]//div[2]//ul[1]//li[1]//a[1]").click()


