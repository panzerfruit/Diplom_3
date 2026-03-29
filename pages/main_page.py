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

    @allure.step("Создание заказа")
    def make_order(self): # Метод для создания заказа
        self.drag_and_drop_js(self.locators.FIRST_INGREDIENT, self.locators.BASKET_AREA) # Перетаскивание первого ингредиента в корзину
        self.click_element(self.locators.PLACE_ORDER_BUTTON) # Клик по кнопке "Оформить заказ"
        self.wait.until(lambda d: d.find_element(*self.locators.ORDER_NUMBER_IN_MODAL).text.strip() not in ["9999", ""]) # Ожидание появления номера заказа в модальном окне
        order_num = self.get_text(self.locators.ORDER_NUMBER_IN_MODAL).strip() # Получение текста номера заказа из модального окна и удаление лишних пробелов
        self.click_element(self.locators.MODAL_CLOSE_BUTTON) # Клик по кнопке закрытия модального окна
        self.wait_for_overlay_to_disappear() # Ожидание исчезновения оверлея после закрытия модального окна
        return order_num # Возвращение номера заказа для дальнейшей проверки в тесте

    @allure.step("Клик по первому ингредиенту")
    def click_first_ingredient(self): # Клик по первому ингредиенту в списке
        self.click_element(self.locators.FIRST_INGREDIENT) # Клик по первому ингредиенту в списке

    @allure.step("Проверка видимости модального окна деталей")
    def is_ingredient_modal_displayed(self): # Проверка видимости модального окна с деталями ингредиента
        return self.find_element(self.locators.INGREDIENT_MODAL).is_displayed() # Возвращение True, если модальное окно с деталями ингредиента отображается, иначе False

    @allure.step("Закрытие модального окна")
    def close_modal(self): # Метод для закрытия модального окна
        self.click_element(self.locators.MODAL_CLOSE_BUTTON) # Клик по кнопке закрытия модального окна
        self.wait_for_overlay_to_disappear() # Ожидание исчезновения оверлея после закрытия модального окна

    @allure.step("Перетаскивание ингредиента в корзину")
    def add_ingredient_to_basket(self): # Метод для перетаскивания ингредиента в корзину
        self.drag_and_drop_js(self.locators.FIRST_INGREDIENT, self.locators.BASKET_AREA) # Перетаскивание первого ингредиента в корзину

    @allure.step("Получение значения счетчика ингредиента")
    def get_ingredient_counter(self): # Метод для получения значения счетчика ингредиента
        text = self.get_text(self.locators.INGREDIENT_COUNTER) # Получение текста счетчика ингредиента
        return int(text) if text.isdigit() else 0 # Возвращение числового значения счетчика ингредиента, если текст является числом, иначе возвращение 0