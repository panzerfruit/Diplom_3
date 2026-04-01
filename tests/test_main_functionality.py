import allure
from pages.main_page import MainPage

@allure.suite("UI: Основной функционал")
class TestMainFunctionality:

    @allure.title("Переход по клику на «Лента заказов»")
    def test_navigation_to_order_feed(self, driver): # тест перехода в ленту
        main_page = MainPage(driver) # инициализируем объект страницы
        main_page.open() # открываем главную
        main_page.go_to_order_feed() # кликаем на переход в ленту
        assert "feed" in main_page.get_current_url() # проверяем URL через метод BasePage (без driver.current_url)

    @allure.title("Переход по клику на «Конструктор»")
    def test_navigation_to_constructor(self, driver): # тест перехода в конструктор
        main_page = MainPage(driver) # инициализируем страницу
        main_page.open("/feed") # сразу открываем ленту заказов
        main_page.go_to_constructor() # кликаем на Конструктор
        assert main_page.get_current_url() == f"{main_page.base_url}/" # проверяем URL через метод BasePage

    @allure.title("Модалка ингредиента: открытие")
    def test_open_ingredient_modal(self, driver): # метод атомарного теста на открытие
        main_page = MainPage(driver) # инициализируем страницу
        main_page.open() # открываем главную
        main_page.click_first_ingredient() # кликаем на ингредиент
        assert main_page.is_ingredient_modal_displayed() # убеждаемся, что окно открыто

    @allure.title("Модалка ингредиента: закрытие")
    def test_close_ingredient_modal(self, driver): # метод атомарного теста на закрытие
        main_page = MainPage(driver) # инициализируем страницу
        main_page.open() # открываем главную
        main_page.click_first_ingredient() # кликаем на ингредиент
        main_page.close_modal() # закрываем модальное окно
        assert not main_page.is_ingredient_modal_displayed() # проверяем, что окно скрыто