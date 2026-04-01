import pytest
import requests
from selenium import webdriver
from urls import Urls
from helpers import Helpers

@pytest.fixture(params=["chrome", "firefox"]) # параметризуем фикстуру для двух браузеров
def driver(request): # параметризация для запуска тестов в разных браузерах
    browser_name = request.param # получаем имя браузера из параметров
    if browser_name == "chrome": # инициализация драйвера для Chrome
        options = webdriver.ChromeOptions() # настройки для Chrome
        _driver = webdriver.Chrome(options=options) # инициализация драйвера Chrome с указанными настройками
    else:
        options = webdriver.FirefoxOptions() # настройки для Firefox
        _driver = webdriver.Firefox(options=options) # инициализация драйвера Firefox с указанными настройками
    _driver.maximize_window() # максимизация окна браузера
    yield _driver # передача драйвера тестам
    _driver.quit() # закрытие браузера после выполнения тестов

@pytest.fixture
def generate_user_data(): # фикстура для генерации данных пользователя
    return Helpers.generate_user_data() # вызываем метод из хелпера и возвращаем результат

@pytest.fixture
def user_client(generate_user_data): # фикстура для создания пользователя и получения токена доступа
    user_data = generate_user_data # получаем сгенерированные данные пользователя
    response = requests.post(f"{Urls.BASE_URL}/api/auth/register", json=user_data) # отправляем POST-запрос для регистрации пользователя
    token = response.json().get("accessToken") # получаем токен доступа из ответа на регистрацию
    yield {"user_data": user_data, "token": token} # передаем данные пользователя и токен тестам
    if token: # если токен существует, удаляем пользователя после выполнения тестов
        requests.delete(f"{Urls.BASE_URL}/api/auth/user", headers={"Authorization": token}) # отправляем DELETE-запрос для удаления пользователя с использованием токена доступа