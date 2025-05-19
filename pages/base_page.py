import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.conftest import driver

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Подождать видимости элемента')
    def wait_for_element(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=30):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=30):
        element = self.wait_for_element(locator, timeout)
        element.click()

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=20):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=20):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step('Перейти на новую вкладку и получить урл')
    def switch_and_get_url(self, expected_url, timeout=40):
        try:
            WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(2))
            self.driver.switch_to.window(self.driver.window_handles[-1])
            WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url))
            current_url = self.driver.current_url
            return current_url
        except:
            return None

    @allure.step("Получение текущего урл")
    def get_current_url(self):
        return self.driver.current_url
