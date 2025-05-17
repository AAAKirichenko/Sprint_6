import allure
import pytest
import data
from pages.main_page import MainPage


class TestMainPageAnswersAndLogo:
    @allure.title("Тест ответы в разделе Вопросы о важном")
    @pytest.mark.parametrize('question_number, expected_text', data.Data.answers_text)
    def test_answers_text(self, driver, question_number, expected_text):
        main_page = MainPage(driver)
        main_page.wait_for_questions_list()
        main_page.click_on_question(question_number)
        assert main_page.check_answer_text(expected_text, question_number)

    @allure.title('Тест переход на главную страницу по логотипу Самокат')
    def test_transfer_logo_samocat(self, driver):
        main_page = MainPage(driver)
        main_page.click_top_register_button()
        main_page.click_on_logo_samocat()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Тест переход на страницу Дзена по логотипу Яндекс')
    def test_trasfer_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.click_top_register_button()
        main_page.click_on_logo_yandex()
        expected_url = 'https://dzen.ru/?yredirect=true'
        result_url = main_page.switch_and_get_url(expected_url)
        assert result_url == expected_url