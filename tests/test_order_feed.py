import allure
import time
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.login_page import LoginPage

@allure.suite("UI: Лента заказов")
class TestOrderFeed: # Проверяем, что после создания заказа он сначала появляется в "В работе:", а затем переходит в "Готовы:" и счетчики обновляются
    
    @allure.title("Проверка движения заказа: из 'В работе' в 'Готовы'")
    def test_order_feed_counters_and_status_change(self, driver, user_client): # Проверяем, что после создания заказа он сначала появляется в "В работе:", а затем переходит в "Готовы:" и счетчики обновляются
        main_page = MainPage(driver) # Инициализация страниц
        feed_page = FeedPage(driver) # Инициализация страниц
        login_page = LoginPage(driver) # Инициализация страниц
        feed_page.open("/feed") # Открываем ленту заказов
        initial_total = feed_page.get_total_completed() # Получаем начальное значение счетчика "за все время"
        initial_today = feed_page.get_today_completed() # Получаем начальное значение счетчика "за сегодня"
        main_page.open() # Открываем главную страницу
        main_page.click_login_button_main() # Переходим на страницу логина
        login_page.login(user_client["user_data"]["email"], user_client["user_data"]["password"]) # Логинимся
        main_page.wait_for_main_page_after_login() # Ждем загрузки главной страницы после логина
        order_number = main_page.make_order() # Создаем заказ и сохраняем его номер
        feed_page.go_to_order_feed() # Переходим в ленту заказов
        feed_page.wait_for_order_in_progress(order_number) # Ждем появления заказа в "В работе:"
        assert feed_page.is_order_in_progress(order_number) is True, f"Заказ {order_number} не появился в 'В работе:'" # Проверяем, что заказ появился в "В работе:"
        time.sleep(4) # Ждем некоторое время, чтобы заказ успел перейти в "Готовы:"
        driver.refresh() # Обновляем страницу, чтобы увидеть изменения
        assert feed_page.get_total_completed() > initial_total, "Счетчик 'за все время' не увеличился" # Проверяем, что счетчик "за все время" увеличился
        assert feed_page.get_today_completed() > initial_today, "Счетчик 'за сегодня' не увеличился" # Проверяем, что счетчик "за сегодня" увеличился
        assert feed_page.is_order_in_ready_list(order_number) is True, f"Заказ {order_number} не перешел в 'Готовы:'" # Проверяем, что заказ перешел в "Готовы:"