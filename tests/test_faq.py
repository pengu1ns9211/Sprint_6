import allure
import pytest

from pages.home_page import HomePage
from utils.test_data import YaScooterHomePageFAQ


class TestQuestionsHomePage:
    
    @allure.title('Проверка ответов на вопросы из раздела "Вопросы о важном"')
    @allure.description('Тест проверяет, что при клике на вопрос открывается правильный ответ')
    @pytest.mark.parametrize('question_number, expected_answer', YaScooterHomePageFAQ.answers)
    def test_question_answers(self, driver, question_number, expected_answer):
        home_page = HomePage(driver)
        
        home_page.open_home_page()
        home_page.accept_cookies()
        home_page.scroll_to_last_question()
        home_page.click_question(question_number)
        actual_answer = home_page.get_answer(question_number)
        
        assert actual_answer == expected_answer, \
            (f'Для вопроса {question_number} ожидался ответ:\n'
             f'"{expected_answer}"\n'
             f'Получен:\n'
             f'"{actual_answer}"')
