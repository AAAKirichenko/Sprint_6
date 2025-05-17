import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class MainPage(BasePage):
    @allure.step("Подождать загрузки раздела Вопросы о важном")
    def wait_for_questions_list(self):
        self.wait_for_element(MainPageLocators.QUESTIONS)

    @allure.step("Открыть вопрос")
    def click_on_question(self, question_number):
        question_locator = MainPageLocators.question(question_number)
        self.scroll_to_element(question_locator)
        self.click_on_element(question_locator)

    @allure.step("Сравнить ответ на вопрос")
    def check_answer_text(self, expected_text, question_number):
        answer_locator = MainPageLocators.answer(question_number)
        actual_text = self.get_text_on_element(answer_locator)
        return actual_text == expected_text

    @allure.step("Нажать на верхнюю кнопку Заказать")
    def click_top_register_button(self):
        register_locator = MainPageLocators.TOP_REGISTER_BUTTON
        self.wait_for_element(register_locator)
        self.click_on_element(register_locator)

    @allure.step('Нажать на нижнюю кнопку Заказать')
    def click_mid_register_button(self):
        reg_locator = MainPageLocators.MID_REGISTER_BUTTON
        self.wait_for_element(reg_locator)
        self.click_on_element(reg_locator)

    @allure.step('Скролл до нижней кнопки Заказать')
    def scroll_to_mid_register_button(self):
        self.scroll_to_element(MainPageLocators.MID_REGISTER_BUTTON)

    @allure.step('Нажать на логотип Самокат')
    def click_on_logo_samocat(self):
        self.click_on_element(MainPageLocators.LOGO_SAMOCAT)

    @allure.step('Нажать на логотип Яндекс')
    def click_on_logo_yandex(self):
        self.click_on_element(MainPageLocators.LOGO_YANDEX)

    @allure.step('Перейти на вкладку Дзен и получить урл')
    def switch_and_get_url(self, expected_url, timeout=40):
        try:
            WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(2))
            self.driver.switch_to.window(self.driver.window_handles[-1])
            WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url))
            current_url = self.driver.current_url
            return current_url
        except:
            return None
