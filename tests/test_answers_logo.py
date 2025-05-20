import allure
import pytest
import data
from pages.main_page import MainPage
from curl import *


class TestMainPageAnswersAndLogo:
    @allure.title("Тест ответы в разделе Вопросы о важном")
    @pytest.mark.parametrize('question_number, expected_text', data.Data.answers_text)
    def test_answers_text(self, driver, question_number, expected_text):
        main_page = MainPage(driver)
        main_page.scroll_to_mid_register_button()
        main_page.wait_for_questions_list()
        main_page.click_on_question(question_number)
        assert main_page.check_answer_text(expected_text, question_number)

    @allure.title('Тест переход на главную страницу по логотипу Самокат')
    def test_transfer_logo_samocat(self, driver):
        main_page = MainPage(driver)
        main_page.click_top_register_button()
        main_page.click_on_logo_samocat()
        assert main_page.get_current_url() == main_site

    @allure.title('Тест переход на страницу Дзена по логотипу Яндекс')
    def test_trasfer_logo_yandex(self, driver):
        main_page = MainPage(driver)
        result_url = main_page.click_on_logo_yandex(dzen_site)
        assert result_url == dzen_site

