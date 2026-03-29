import allure
from pages.main_page import MainPage

@allure.suite("UI: Основной функционал")
class TestMainFunctionality:

    @allure.title("Переход по клику на «Конструктор» и «Лента заказов»")
    def test_navigation(self, driver): # Проверяем, что при клике на «Конструктор» и «Лента заказов» происходит переход на соответствующие страницы
        main_page = MainPage(driver) # Инициализируем объект главной страницы
        main_page.open() # Открываем главную страницу
        main_page.go_to_order_feed() # Переходим на страницу ленты заказов
        assert "feed" in driver.current_url # Проверяем, что URL содержит "feed"
        main_page.go_to_constructor() # Переходим на страницу конструктора
        assert driver.current_url == f"{main_page.base_url}/" # Проверяем, что URL соответствует главной странице конструктора

    @allure.title("Модалка ингредиента: открытие и закрытие")
    def test_ingredient_modal(self, driver): # Проверяем, что при клике на ингредиент открывается модальное окно с его подробной информацией, и что его можно закрыть
        main_page = MainPage(driver) # Инициализируем объект главной страницы
        main_page.open() # Открываем главную страницу
        main_page.click_first_ingredient() # Кликаем на первый ингредиент в списке
        assert main_page.is_ingredient_modal_displayed() # Проверяем, что модальное окно отображается
        main_page.close_modal() # Закрываем модальное окно

    @allure.title("Увеличение счетчика при добавлении ингредиента")
    def test_ingredient_counter_increases(self, driver): # Проверяем, что при добавлении ингредиента в конструктор счетчик ингредиентов увеличивается
        main_page = MainPage(driver) # Инициализируем объект главной страницы
        main_page.open() # Открываем главную страницу
        main_page.add_ingredient_to_basket() # Добавляем ингредиент в корзину
        counter = main_page.get_ingredient_counter() # Получаем значение счетчика ингредиентов
        assert counter > 0 # Проверяем, что счетчик увеличился (больше 0)