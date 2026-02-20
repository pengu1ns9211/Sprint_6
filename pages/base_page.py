import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидание содержания URL")
    def wait_url_contains(self, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(text))

    @allure.step("Открытие URL")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Найти элемент по локатору")
    def find_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Клик по элементу")
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step("Ожидание видимости элемента")
    def wait_element_visibility(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator)).text

    @allure.step("Ввести текст")
    def set_text(self, locator, text):
        element = WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        element.send_keys(text)

    @allure.step("Проскроллить к элементу")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    @allure.step("Ожидание перехода по URL")
    def wait_navigating_url(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

    @allure.step("Ожидание содержания URL")
    def wait_url_contains(self, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(text))

    @allure.step("Переключение на новую вкладку")
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
