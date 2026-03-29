import pytest
import requests
import random
import string
from selenium import webdriver
from urls import Urls

@pytest.fixture(params=["chrome", "firefox"])
def driver(request): # Параметризация для запуска тестов в разных браузерах
    browser_name = request.param # Получаем имя браузера из параметров
    if browser_name == "chrome": # Инициализация драйвера для Chrome
        options = webdriver.ChromeOptions() # Настройки для Chrome
        _driver = webdriver.Chrome(options=options) # Инициализация драйвера Chrome с указанными настройками
    else:
        options = webdriver.FirefoxOptions() # Настройки для Firefox
        _driver = webdriver.Firefox(options=options) # Инициализация драйвера Firefox с указанными настройками
    _driver.maximize_window() # Максимизация окна браузера
    yield _driver # Передача драйвера тестам
    _driver.quit() # Закрытие браузера после выполнения тестов

@pytest.fixture
def generate_user_data(): # Фикстура для генерации данных пользователя
    rand = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) # Генерация случайной строки для уникальности данных пользователя
    return {
        "email": f"qa_test_{rand}@yandex.ru",
        "password": "password123",
        "name": f"Tester_{rand}"
    } # Данные пользователя включают уникальный email, пароль и имя

@pytest.fixture
def user_client(generate_user_data): # Фикстура для создания пользователя и получения токена доступа
    user_data = generate_user_data # Получаем сгенерированные данные пользователя
    response = requests.post(f"{Urls.BASE_URL}/api/auth/register", json=user_data) # Отправляем POST-запрос для регистрации пользователя
    token = response.json().get("accessToken") # Получаем токен доступа из ответа на регистрацию
    yield {"user_data": user_data, "token": token} # Передаем данные пользователя и токен тестам
    if token: # Если токен существует, удаляем пользователя после выполнения тестов
        requests.delete(f"{Urls.BASE_URL}/api/auth/user", headers={"Authorization": token}) # Отправляем DELETE-запрос для удаления пользователя с использованием токена доступа