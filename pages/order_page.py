import allure
from selenium.webdriver import Keys
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполнение формы "Для кого самокат"')
    def fill_customer_info(self, name, last_name, address, metro, phone):
        self.set_text(OrderPageLocators.NAME_FIELD, name)
        self.set_text(OrderPageLocators.LAST_NAME_FIELD, last_name)
        self.set_text(OrderPageLocators.ADDRESS_FIELD, address)
        self.set_text(OrderPageLocators.PHONE_FIELD, phone)
        
        # Выбор станции метро
        self.click_to_element(OrderPageLocators.METRO_FIELD)
        self.set_text(OrderPageLocators.METRO_FIELD, metro)
        self.click_to_element(OrderPageLocators.METRO_DROPDOWN_OPTION)

    @allure.step('Клик на кнопку "Далее"')
    def click_next_button(self):
        self.click_to_element(OrderPageLocators.NEXT_BTN)

    @allure.step('Заполнение формы "Про аренду"')
    def fill_rent_info(self, rent_day, colour, comment):
        # Выбор даты (текущая дата + 1 день)
        self.click_to_element(OrderPageLocators.DATE_FIELD)
        self.set_text(OrderPageLocators.DATE_FIELD, Keys.ENTER)
        
        # Выбор срока аренды
        self.click_to_element(OrderPageLocators.RENT_FIELD)
        if rent_day == 'сутки':
            self.click_to_element(OrderPageLocators.RENT_OPTION_1_DAY)
        else:
            self.click_to_element(OrderPageLocators.RENT_OPTION_3_DAYS)
        
        # Выбор цвета самоката
        if colour == 'black':
            self.click_to_element(OrderPageLocators.BLACK_COLOR)
        else:
            self.click_to_element(OrderPageLocators.GREY_COLOR)
        
        # Ввод комментария
        self.set_text(OrderPageLocators.COMMENTS, comment)

    @allure.step('Клик на кнопку "Заказать" в форме заказа')
    def click_order_button(self):
        self.click_to_element(OrderPageLocators.ORDER_BTN)

    @allure.step('Подтверждение заказа кнопкой "Да"')
    def confirm_order(self):
        self.click_to_element(OrderPageLocators.YES_BTN)

    @allure.step('Проверка появления окна с сообщением об успешном заказе')
    def check_order_success(self):
        return self.get_text(OrderPageLocators.ORDER_SUCCESS_WINDOW)

    @allure.step('Полный флоу оформления заказа')
    def create_order(self, customer_data, rent_data):
        self.fill_customer_info(
            customer_data['name'],
            customer_data['last_name'],
            customer_data['address'],
            customer_data['metro'],
            customer_data['phone']
        )
        self.click_next_button()
        self.fill_rent_info(
            rent_data['rent_day'],
            rent_data['colour'],
            rent_data['comment']
        )
        self.click_order_button()
        self.confirm_order()
        return self.check_order_success()
