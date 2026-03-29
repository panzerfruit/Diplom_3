from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from urls import Urls
from locators import BaseLocators

class BasePage:
    def __init__(self, driver): # Инициализация драйвера и базового URL
        self.driver = driver # Инициализация драйвера
        self.wait = WebDriverWait(driver, 15) # Инициализация WebDriverWait с таймаутом 15 секунд
        self.base_url = Urls.BASE_URL # Инициализация базового URL из класса Urls

    def open(self, url=""): # Метод для открытия страницы по заданному URL, по умолчанию открывает базовый URL
        self.driver.get(f"{self.base_url}{url}") # Открытие страницы по заданному URL, объединяя базовый URL и переданный URL

    def find_element(self, locator): # Метод для поиска элемента на странице по заданному локатору, ожидая его присутствия
        return self.wait.until(EC.presence_of_element_located(locator)) # Возвращает найденный элемент, ожидая его присутствия на странице

    def click_element(self, locator): # Метод для клика по элементу, ожидая его кликабельности, и обрабатывая возможные исключения при клике
        try: # Ожидание, пока элемент станет кликабельным, и попытка кликнуть по нему
            element = self.wait.until(EC.element_to_be_clickable(locator)) # Ожидание, пока элемент станет кликабельным
            element.click() # Клик по элементу
        except (ElementClickInterceptedException, TimeoutException): # Обработка исключений, если элемент не кликается из-за перекрытия или таймаута
            element = self.driver.find_element(*locator) # Поиск элемента без ожидания, если возникла ошибка при клике
            self.driver.execute_script("arguments[0].click();", element) # Выполнение клика через JavaScript, если обычный клик не сработал

    def get_text(self, locator): # Метод для получения текста элемента, ожидая его видимости
        return self.wait.until(EC.visibility_of_element_located(locator)).text # Возвращает текст элемента, ожидая его видимости на странице

    def wait_for_overlay_to_disappear(self): # Метод для ожидания исчезновения модального оверлея, обрабатывая возможные таймауты
        try: # Ожидание, пока элемент с локатором MODAL_OVERLAY станет невидимым
            self.wait.until(EC.invisibility_of_element_located(BaseLocators.MODAL_OVERLAY)) # Ожидание, пока элемент с локатором MODAL_OVERLAY станет невидимым
        except TimeoutException: # Обработка исключения, если элемент не исчезает в течение заданного времени ожидания
            pass # Если элемент не исчезает, просто продолжаем выполнение без прерывания теста

    def drag_and_drop_js(self, source_locator, target_locator): # Метод для выполнения drag-and-drop с помощью JavaScript, принимая локаторы источника и цели
        source = self.find_element(source_locator) # Поиск элемента-источника по заданному локатору
        target = self.find_element(target_locator) # Поиск элемента-цели по заданному локатору
        script = """
        var source = arguments[0];
        var target = arguments[1];
        var dataTransfer = new DataTransfer();
        source.dispatchEvent(new DragEvent('dragstart', { dataTransfer: dataTransfer, bubbles: true }));
        target.dispatchEvent(new DragEvent('dragenter', { dataTransfer: dataTransfer, bubbles: true }));
        target.dispatchEvent(new DragEvent('dragover', { dataTransfer: dataTransfer, bubbles: true }));
        target.dispatchEvent(new DragEvent('drop', { dataTransfer: dataTransfer, bubbles: true }));
        source.dispatchEvent(new DragEvent('dragend', { dataTransfer: dataTransfer, bubbles: true }));
        """ # JavaScript код для имитации событий drag-and-drop между элементами-источником и целью
        self.driver.execute_script(script, source, target) # Выполнение JavaScript для имитации drag-and-drop между элементами-источником и целью

    def go_to_order_feed(self): # Метод для перехода на страницу ленты заказов, кликая по соответствующей ссылке
        self.click_element(BaseLocators.ORDER_FEED_LINK) # Клик по элементу с локатором ORDER_FEED_LINK для перехода на страницу ленты заказов

    def go_to_constructor(self): # Метод для перехода на страницу конструктора, кликая по соответствующей ссылке
        self.click_element(BaseLocators.CONSTRUCTOR_LINK) # Клик по элементу с локатором CONSTRUCTOR_LINK для перехода на страницу конструктора