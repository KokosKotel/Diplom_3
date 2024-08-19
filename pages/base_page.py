import allure
from seletools.actions import drag_and_drop
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url

    def wait_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def check_element(self, locator):
        self.wait_element(locator)
        return self.driver.find_element(*locator)

    def send_keys(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    def click_button(self, locator):
        element = self.wait_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def get_text_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def get_text_locator(self, locator):
        element = self.wait_element(locator)
        return element.text

    def drag_drop(self, element_first, element_second):
        ingredient = self.check_element(element_first)
        basket = self.check_element(element_second)
        drag_and_drop(self.driver, ingredient, basket)

    def check_element_not_visible(self, locator):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_after_wait(self, locator):
        target_to_click = self.wait_element(locator)
        target_to_click.click()
