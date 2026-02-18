from selenium.webdriver.common.by import By


class OrderPageLocators:
   
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
 
    METRO_DROPDOWN_OPTION = (By.XPATH, "//div[contains(@class, 'select-search__select')]//li[1]")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
 
    NEXT_BTN = (By.XPATH, "//button[text()='Далее']")

    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_FIELD = (By.XPATH, "//div[text()='* Срок аренды']")
    RENT_OPTION_1_DAY = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
    RENT_OPTION_3_DAYS = (By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']")
    BLACK_COLOR = (By.ID, "black")
    GREY_COLOR = (By.ID, "grey")
    COMMENTS = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    
    ORDER_BTN = (By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[text()='Заказать']")
    YES_BTN = (By.XPATH, "//button[text()='Да']")
    ORDER_SUCCESS_WINDOW = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")
