import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.login_page import LoginPage

@allure.suite("UI: Лента заказов")
class TestOrderFeed: # Проверяем, что после создания заказа он сначала появляется в "В работе:", а затем переходит в "Готовы:" и счетчики обновляются
    
    @allure.title("Проверка появления созданного заказа в 'В работе'") # Атомарный тест статуса
    def test_order_appears_in_progress(self, driver, user_client): # Метод теста
        main_page = MainPage(driver) # Инициализируем главную
        feed_page = FeedPage(driver) # Инициализируем ленту
        login_page = LoginPage(driver) # Инициализируем страницу входа
        main_page.open() # Открываем сайт
        main_page.click_login_button_main() # Идем на авторизацию
        login_page.login(user_client["user_data"]["email"], user_client["user_data"]["password"]) # Логинимся в профиль
        main_page.wait_for_main_page_after_login() # Ждем загрузки
        order_number = main_page.make_order() # Создаем заказ
        feed_page.go_to_order_feed() # Идем в ленту
        feed_page.wait_for_order_in_progress(order_number) # Явно ждем появления заказа в списке
        assert feed_page.is_order_in_progress(order_number) is True # Окончательный ассерт

    @allure.title("Проверка увеличения счетчиков заказов") # Атомарный тест счетчиков
    def test_order_feed_counters_increase(self, driver, user_client): # Метод теста
        main_page = MainPage(driver) # Инициализируем главную
        feed_page = FeedPage(driver) # Инициализируем ленту
        login_page = LoginPage(driver) # Инициализируем страницу входа
        feed_page.open("/feed") # Открываем ленту сразу
        initial_total = feed_page.get_total_completed() # Запоминаем счетчик "за все время"
        initial_today = feed_page.get_today_completed() # Запоминаем счетчик "за сегодня"
        main_page.open() # Переходим на главную
        main_page.click_login_button_main() # Идем логиниться
        login_page.login(user_client["user_data"]["email"], user_client["user_data"]["password"]) # Логинимся в профиль
        main_page.wait_for_main_page_after_login() # Ждем
        main_page.make_order() # Оформляем заказ
        feed_page.go_to_order_feed() # Переходим в ленту
        feed_page.wait_for_total_counter_to_increase(initial_total) # Ждем, пока бекенд обновит счетчик
        assert feed_page.get_total_completed() > initial_total # Проверяем общее колво заказов
        assert feed_page.get_today_completed() > initial_today # Проверяем "за сегодня"