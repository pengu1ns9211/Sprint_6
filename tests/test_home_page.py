import allure

from pages.home_page import HomePage
from utils.urls import Urls


class TestHomePage:
    
    @allure.title('Клик на логотип "Самокат" возвращает на главную страницу')
    def test_samokat_logo_redirect(self, driver):
        home_page = HomePage(driver)
        
        home_page.open_home_page()
        home_page.click_samokat_logo()
        home_page.wait_navigating_url(Urls.HOME_PAGE)
        current_url = home_page.get_current_url()
        
        assert current_url == Urls.HOME_PAGE, \
            f'Ожидался URL: {Urls.HOME_PAGE}, но получен: {current_url}'

    @allure.title('Клик на логотип "Яндекс" открывает страницу Дзена')
    def test_yandex_logo_redirect(self, driver):
        home_page = HomePage(driver)
        
        home_page.open_home_page()
        home_page.click_yandex_logo()
        home_page.switch_to_new_tab()
        home_page.wait_url_contains(Urls.DZEN_DOMAIN)
        current_url = home_page.get_current_url()
        
        assert Urls.DZEN_DOMAIN in current_url, \
            f'Ожидался редирект на Dzen, но получен URL: {current_url}'
