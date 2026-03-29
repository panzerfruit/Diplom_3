import allure
from pages.base_page import BasePage
from locators import LoginPageLocators

class LoginPage(BasePage):
    def __init__(self, driver): # Конструктор класса LoginPage, который принимает драйвер в качестве аргумента
        super().__init__(driver) # Инициализация базового класса
        self.locators = LoginPageLocators # Инициализация локаторов для страницы входа

    @allure.step("Ввод данных и авторизация")
    def login(self, email, password): # Метод для выполнения входа, который принимает email и пароль в качестве аргументов
        self.find_element(self.locators.EMAIL_INPUT).send_keys(email) # Находит элемент для ввода email и вводит переданный email
        self.find_element(self.locators.PASSWORD_INPUT).send_keys(password) # Находит элемент для ввода пароля и вводит переданный пароль
        self.click_element(self.locators.LOGIN_SUBMIT_BUTTON) # Находит кнопку отправки формы и кликает по ней для выполнения входа