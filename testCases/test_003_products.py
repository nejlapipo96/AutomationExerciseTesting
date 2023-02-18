from pageObject.AllProductsPage import AllProductsPage
from selenium.webdriver.common.by import By

class Test_003_Products:
    baseUrl = "https://automationexercise.com/"

    def test_allProducts(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        homepage_title = self.driver.title
        assert "Automation Exercise" in homepage_title
        self.products = AllProductsPage(self.driver)
        self.products.clickOnProducts()
        self.driver.implicitly_wait(10)
        products_title = self.driver.find_element(By.XPATH, "//h2[normalize-space()='All Products']").text
        assert "ALL PRODUCTS" in products_title
        self.products.firstProduct()
        product_details = self.driver.find_element(By.XPATH, "//div[@class='product-information']")
        assert product_details.is_displayed()
        self.driver.close()