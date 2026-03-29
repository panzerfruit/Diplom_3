import allure
from pages.base_page import BasePage
from locators import FeedPageLocators, BaseLocators

class FeedPage(BasePage): # класс страницы ленты заказов, наследуется от базового класса
    def __init__(self, driver): # конструктор класса, принимает драйвер и инициализирует базовый класс
        super().__init__(driver) # вызов конструктора базового класса
        self.locators = FeedPageLocators # инициализация локаторов для страницы ленты заказов

    @allure.step("Переход в ленту заказов")
    def go_to_order_feed(self): # метод для перехода в ленту заказов, кликает по соответствующей ссылке
        self.click_element(BaseLocators.ORDER_FEED_LINK) # клик по ссылке для перехода в ленту заказов

    @allure.step("Получение счетчика 'Выполнено за все время'")
    def get_total_completed(self): # метод для получения счетчика "Выполнено за все время", возвращает целое число
        return int(self.get_text(self.locators.TOTAL_COMPLETED)) # получение текста элемента с локатором TOTAL_COMPLETED, преобразование его в целое число и возврат

    @allure.step("Получение счетчика 'Выполнено за сегодня'")
    def get_today_completed(self): # метод для получения счетчика "Выполнено за сегодня", возвращает целое число
        return int(self.get_text(self.locators.TODAY_COMPLETED)) # получение текста элемента с локатором TODAY_COMPLETED, преобразование его в целое число и возврат

    @allure.step("Проверка наличия заказа в списке 'В работе:'")
    def is_order_in_progress(self, order_number): # метод для проверки наличия заказа в списке "В работе:", принимает номер заказа и возвращает булево значение
        elements = self.driver.find_elements(*self.locators.IN_PROGRESS_LIST) # поиск всех элементов в списке "В работе:" с помощью локатора IN_PROGRESS_LIST
        return any(str(order_number) in el.text for el in elements) # проверка наличия номера заказа в тексте любого из найденных элементов, возвращает True, если найдено, иначе False

    @allure.step("Проверка наличия заказа в списке 'Готовы:'")
    def is_order_in_ready_list(self, order_number): # метод для проверки наличия заказа в списке "Готовы:", принимает номер заказа и возвращает булево значение
        elements = self.driver.find_elements(*self.locators.READY_LIST) # поиск всех элементов в списке "Готовы:" с помощью локатора READY_LIST
        return any(str(order_number) in el.text for el in elements) # проверка наличия номера заказа в тексте любого из найденных элементов, возвращает True, если найдено, иначе False

    @allure.step("Ожидание появления заказа в колонке 'В работе:'")
    def wait_for_order_in_progress(self, order_number): # метод для ожидания появления заказа в колонке "В работе:", принимает номер заказа и не возвращает значение
        self.wait.until(lambda d: self.is_order_in_progress(order_number)) # использование метода wait для ожидания, пока заказ не появится в списке "В работе:"