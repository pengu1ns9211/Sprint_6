import allure
import pytest

from pages.home_page import HomePage
from pages.order_page import OrderPage
from utils.test_data import YaScooterOrderData


class TestOrderCreation:
    
    @allure.title('Оформление заказа через кнопку в шапке')
    @pytest.mark.parametrize('order_data', [
        YaScooterOrderData.order_set_1,
        YaScooterOrderData.order_set_2
    ])
    def test_create_order_via_header_button(self, driver, order_data):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        
        home_page.open_home_page()
        home_page.accept_cookies()
        home_page.click_order_button_header()
        
        success_message = order_page.create_order(order_data, order_data)
        
        assert 'Заказ оформлен' in success_message, 'Сообщение об успешном заказе не появилось'

    @allure.title('Оформление заказа через кнопку внизу страницы')
    @pytest.mark.parametrize('order_data', [
        YaScooterOrderData.order_set_1,
        YaScooterOrderData.order_set_2
    ])
    def test_create_order_via_bottom_button(self, driver, order_data):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        
        home_page.open_home_page()
        home_page.accept_cookies()
        home_page.scroll_to_last_question()
        home_page.click_order_button_bottom()
        
        success_message = order_page.create_order(order_data, order_data)
        
        assert 'Заказ оформлен' in success_message, 'Сообщение об успешном заказе не появилось'


  class TestHeaderLogo:

    @allure.title('Клик на логотип "Самокат" на странице заказа возвращает на главную')
    def test_samokat_logo_redirect_from_order(self, driver):
        order_page = OrderPage(driver)
        home_page = HomePage(driver)

        order_page.open_order_page()
        order_page.click_samokat_logo()  # Этот метод нужно добавить!

        assert home_page.get_current_url() == Urls.HOME_PAGE

    @allure.title('Клик на логотип "Яндекс" на странице заказа открывает Дзен')
    def test_yandex_logo_redirect_from_order(self, driver):
        order_page = OrderPage(driver)

        order_page.open_order_page()
        order_page.click_yandex_logo()  # Этот метод нужно добавить!
        order_page.switch_to_new_tab()

        assert Urls.DZEN_DOMAIN in order_page.get_current_url()