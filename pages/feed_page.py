import allure
from pages.base_page import BasePage
from locators import FeedPageLocators, BaseLocators

class FeedPage(BasePage): # класс страницы ленты заказов, наследуется от базового класса
    def __init__(self, driver): # конструктор класса, принимает драйвер и инициализирует базовый класс
        super().__init__(driver) # вызов конструктора базового класса
        self.locators = FeedPageLocators # инициализация локаторов для страницы ленты заказов

    @allure.step("Получение счетчика 'Выполнено за все время'")
    def get_total_completed(self): # метод для получения счетчика "Выполнено за все время:", возвращает целое число
        element = self.find_element(self.locators.TOTAL_COMPLETED) # ищем элемент счетчика через метод BasePage
        return int(element.text) # возвращаем текст элемента в виде числа

    @allure.step("Получение счетчика 'Выполнено за сегодня'")
    def get_today_completed(self): # получение счётчика "за сегодня"
        element = self.find_element(self.locators.TODAY_COMPLETED) # поиск через BasePage
        return int(element.text) # возвращаем текст элемента в виде числа

    @allure.step("Проверка наличия заказа в списке 'В работе:'")
    def is_order_in_progress(self, order_number): # проверка заказа в "В работе"
        elements = self.get_elements(self.locators.IN_PROGRESS_LIST) # используем get_elements (без ожидания) чтобы избежать TimeoutException при пустом списке
        return any(str(order_number) in el.text for el in elements) # проверка наличия номера в любом элементе списка

    @allure.step("Ожидание появления заказа в колонке 'В работе:'")
    def wait_for_order_in_progress(self, order_number): # явное ожидание появления в "В работе"
        self.wait.until(lambda d: self.is_order_in_progress(order_number)) # ждем пока метод вернет True

    @allure.step("Ожидание увеличения счетчика 'Выполнено за все время:'")
    def wait_for_total_counter_to_increase(self, initial_value): # метод явного ожидания счетчика
        self.wait.until(lambda d: self.get_total_completed() > initial_value) # ждем, пока текущее значение станет больше изначального

    @allure.step("Проверка наличия заказа в списке 'Готовы:'")
    def is_order_in_ready_list(self, order_number): # метод проверки заказа в "Готовы:"
        elements = self.get_elements(self.locators.READY_LIST) # используем get_elements (без ожидания) - список может быть пустым
        return any(str(order_number) in el.text for el in elements) # проверка наличия номера заказа в текстах элементов