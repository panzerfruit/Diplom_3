import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, driver): # Добавляем конструктор для инициализации локаторов
        super().__init__(driver) # Инициализация локаторов для главной страницы
        self.locators = MainPageLocators # Инициализация локаторов для главной страницы

    @allure.step("Клик по кнопке входа на главной")
    def click_login_button_main(self): # Клик по кнопке входа на главной странице
        self.click_element(self.locators.LOGIN_BUTTON_MAIN) # Клик по кнопке входа на главной странице

    @allure.step("Ожидание главной страницы")
    def wait_for_main_page_after_login(self): # Ожидание главной страницы после входа
        self.wait.until(EC.visibility_of_element_located(self.locators.PLACE_ORDER_BUTTON)) # Ожидание видимости кнопки "Оформить заказ" на главной странице после входа

    @allure.step("Создание заказа и получение его номера")
    def make_order(self): # создание заказа
        self.drag_and_drop_js(self.locators.FIRST_INGREDIENT, self.locators.BASKET_AREA) # drag-and-drop первой булки в корзину через JS
        self.wait.until(lambda d: self.get_text(self.locators.INGREDIENT_COUNTER) not in ["", "0"]) # явное ожидание: счётчик ингредиента должен обновиться (корзина не пуста)
        self.click_element(self.locators.PLACE_ORDER_BUTTON) # клик по кнопке "Оформить заказ"
        self.wait.until(EC.visibility_of_element_located(self.locators.ORDER_NUMBER_IN_MODAL)) # ждём модалку по локатору
        self.wait.until(lambda d: self.get_text(self.locators.ORDER_NUMBER_IN_MODAL) != "9999") # ждём, пока заглушка "9999" сменится на реальный номер заказа от бэкенда
        order_number = self.get_text(self.locators.ORDER_NUMBER_IN_MODAL) # сохраняем реальный номер заказа из h2
        self.click_element(self.locators.MODAL_CLOSE_BUTTON) # закрываем модальное окно с номером заказа
        self.wait_for_overlay_to_disappear() # ждём полного исчезновения оверлея и анимации
        return order_number # возврат номера для теста

    @allure.step("Клик по первому ингредиенту")
    def click_first_ingredient(self): # Клик по первому ингредиенту в списке
        self.click_element(self.locators.FIRST_INGREDIENT) # Клик по первому ингредиенту в списке

    @allure.step("Проверка видимости модального окна деталей")
    def is_ingredient_modal_displayed(self): # проверка модалки ингредиента
        return self.is_element_displayed(self.locators.INGREDIENT_MODAL) # используем  метод BasePage (без прямого driver)

    @allure.step("Закрытие модального окна")
    def close_modal(self): # метод для принудительного закрытия модального окна
        self.click_element(self.locators.MODAL_CLOSE_BUTTON) # клик по обновлённому локатору закрытия
        self.wait_for_overlay_to_disappear() # ожидание исчезновения оверлея

    @allure.step("Перетаскивание ингредиента в корзину")
    def add_ingredient_to_basket(self): # Метод для перетаскивания ингредиента в корзину
        self.drag_and_drop_js(self.locators.FIRST_INGREDIENT, self.locators.BASKET_AREA) # Перетаскивание первого ингредиента в корзину

    @allure.step("Получение значения счетчика ингредиента")
    def get_ingredient_counter(self): # Метод для получения значения счетчика ингредиента
        return self.get_text(self.locators.INGREDIENT_COUNTER) # Считываем и возвращаем текст из бейджика счетчика ингредиента