import allure
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
from utils.urls import Urls


class HomePage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_home_page(self):
        self.open_url(Urls.HOME_PAGE)
        self.wait_element_visibility(HomePageLocators.COOKIES_BTN)

    @allure.step('Принять cookies')
    def accept_cookies(self):
        self.click_to_element(HomePageLocators.COOKIES_BTN)

    @allure.step('Клик на вопрос с номером {number}')
    def click_question(self, number):
        method, locator = HomePageLocators.QUESTION
        formatted_locator = locator.format(number)
        self.click_to_element((method, formatted_locator))

    @allure.step('Получение ответа на вопрос с номером {number}')
    def get_answer(self, number):
        method, locator = HomePageLocators.ANSWER
        formatted_locator = locator.format(number)
        return self.get_text((method, formatted_locator))

    @allure.step('Клик на логотип Яндекса')
    def click_yandex_logo(self):
        self.click_to_element(HomePageLocators.YANDEX_LOGO)

    @allure.step('Клик на логотип Самоката')
    def click_samokat_logo(self):
        self.click_to_element(HomePageLocators.SAMOKAT_LOGO)

    @allure.step('Прокрутка к последнему вопросу в FAQ')
    def scroll_to_last_question(self):
        self.scroll_to_element(HomePageLocators.LAST_QUESTION)

    @allure.step('Клик на кнопку заказа в хедере')
    def click_order_button_header(self):
        self.click_to_element(HomePageLocators.ORDER_BTN_HEADER)

    @allure.step('Клик на кнопку заказа внизу страницы')
    def click_order_button_bottom(self):
        self.scroll_to_element(HomePageLocators.ORDER_BTN_BOTTOM)
        self.click_to_element(HomePageLocators.ORDER_BTN_BOTTOM)
