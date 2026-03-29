from selenium.webdriver.common.by import By

class BaseLocators: # локаторы, общие для всех страниц
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']") # локатор для ссылки "Конструктор" в шапке сайта
    ORDER_FEED_LINK = (By.XPATH, "//p[text()='Лента Заказов']") # локатор для ссылки "Лента Заказов" в шапке сайта
    MODAL_OVERLAY = (By.XPATH, "//*[contains(@class, 'Modal_modal_overlay')]") # локатор для оверлея модального окна, который появляется при открытии модальных окон на сайте
    LOGIN_BUTTON_HEADER = (By.XPATH, "//p[text()='Личный Кабинет']") # локатор для кнопки "Личный Кабинет" в шапке сайта

class MainPageLocators: # локаторы, специфичные для главной страницы
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']") # локатор для кнопки "Войти в аккаунт" на главной странице
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") # локатор для кнопки "Оформить заказ" на главной странице
    FIRST_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]") # локатор для первого ингредиента в списке ингредиентов на главной странице
    INGREDIENT_MODAL = (By.XPATH, "//h2[text()='Детали ингредиента']") # локатор для заголовка модального окна с деталями ингредиента, который появляется при клике на ингредиент на главной странице
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]") # локатор для кнопки закрытия модального окна, который появляется при открытии модальных окон на сайте
    INGREDIENT_COUNTER = (By.XPATH, "(//p[contains(@class, 'counter_counter')])[1]") # локатор для счетчика количества ингредиента, который появляется при добавлении ингредиента в конструктор на главной странице
    BASKET_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]") # локатор для области корзины, в которую можно перетаскивать ингредиенты на главной странице
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')]") # локатор для модального окна с информацией о заказе, который появляется после оформления заказа на главной странице
    ORDER_NUMBER_IN_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')]//h2") # локатор для заголовка с номером заказа в модальном окне с информацией о заказе, который появляется после оформления заказа на главной странице

class FeedPageLocators: # локаторы, специфичные для страницы ленты заказов
    TOTAL_COMPLETED = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p") # локатор для количества заказов, выполненных за все время, на странице ленты заказов
    TODAY_COMPLETED = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p") # локатор для количества заказов, выполненных за сегодня, на странице ленты заказов
    IN_PROGRESS_LIST = (By.XPATH, "//p[text()='В работе:']/parent::div//ul/li") # локатор для списка заказов в статусе "В работе:" на странице ленты заказов
    READY_LIST = (By.XPATH, "//p[text()='Готовы:']/parent::div//ul/li") # локатор для списка заказов в статусе "Готовы:" на странице ленты заказов

class LoginPageLocators: # локаторы, специфичные для страницы логина
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input") # локатор для поля ввода email на странице логина
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input") # локатор для поля ввода пароля на странице логина
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']") # локатор для кнопки "Войти" на странице логина