from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from urls import Urls
from locators import BaseLocators

class BasePage:
    def __init__(self, driver): # инициализация драйвера и базового URL
        self.driver = driver # инициализация драйвера
        self.wait = WebDriverWait(driver, 15) # инициализация WebDriverWait с таймаутом 15 секунд
        self.base_url = Urls.BASE_URL # инициализация базового URL из класса Urls

    def open(self, url=""): # метод для открытия страницы по заданному URL, по умолчанию открывает базовый URL
        self.driver.get(f"{self.base_url}{url}") # открытие страницы по заданному URL, объединяя базовый URL и переданный URL

    def find_element(self, locator): # метод для поиска элемента на странице по заданному локатору, ожидая его присутствия
        return self.wait.until(EC.presence_of_element_located(locator)) # возвращает найденный элемент, ожидая его присутствия на странице

    def find_elements(self, locator): # новый метод для поиска списка элементов (исправление ревью)
        return self.wait.until(EC.presence_of_all_elements_located(locator)) # ждем появления элементов и возвращаем список

    def get_elements(self, locator): # поиск элементов БЕЗ ожидания (для списков, которые могут быть пустыми, чтобы избежать таймаута)
        return self.driver.find_elements(*locator) # мгновенный поиск через драйвер

    def is_element_displayed(self, locator): # НОВЫЙ метод по ревью: проверка отображения элемента БЕЗ длинного ожидания (решает проблему прямого driver в main_page)
        try:
            element = self.driver.find_element(*locator) # мгновенный поиск элемента (без WebDriverWait)
            return element.is_displayed() # возврат True, если элемент видим
        except: # перехват любой ошибки
            return False # элемент не найден или не видим → False
        
    def get_current_url(self): # метод получения текущего URL страницы
        return self.driver.current_url # возврат current_url из драйвера

    def refresh_page(self): # новый метод для обновления страницы (исправление ревью)
        self.driver.refresh() # обновляем страницу через драйвер    

    def click_element(self, locator): # метод безопасного клика (с обработкой overlay)
        try: # попытка стандартного клика
            element = self.wait.until(EC.element_to_be_clickable(locator)) # ожидание кликабельности
            element.click() # физический клик мышью
        except ElementClickInterceptedException: # перехват ошибки overlay
            element = self.wait.until(EC.presence_of_element_located(locator)) # ожидание присутствия
            self.driver.execute_script("arguments[0].click();", element) # Выполняем клик напрямую через JavaScript, игнорируя слои сверху

    def get_text(self, locator): # метод для получения текста элемента, ожидая его видимости
        return self.wait.until(EC.visibility_of_element_located(locator)).text # возвращает текст элемента, ожидая его видимости на странице

    def wait_for_overlay_to_disappear(self): # ожидание исчезновения модального окна
        self.wait.until(EC.invisibility_of_element_located(BaseLocators.MODAL_OVERLAY)) # ждем, пока локатор темного фона пропадет с экрана

    def drag_and_drop_js(self, source_locator, target_locator): # метод для выполнения drag-and-drop с помощью JavaScript, принимая локаторы источника и цели
        source = self.find_element(source_locator) # поиск элемента-источника по заданному локатору
        target = self.find_element(target_locator) # поиск элемента-цели по заданному локатору
        script = """
        var source = arguments[0];
        var target = arguments[1];
        var dataTransfer = new DataTransfer();
        source.dispatchEvent(new DragEvent('dragstart', { dataTransfer: dataTransfer, bubbles: true }));
        target.dispatchEvent(new DragEvent('dragenter', { dataTransfer: dataTransfer, bubbles: true }));
        target.dispatchEvent(new DragEvent('dragover', { dataTransfer: dataTransfer, bubbles: true }));
        target.dispatchEvent(new DragEvent('drop', { dataTransfer: dataTransfer, bubbles: true }));
        source.dispatchEvent(new DragEvent('dragend', { dataTransfer: dataTransfer, bubbles: true }));
        """ # javaScript код для имитации событий drag-and-drop между элементами-источником и целью
        self.driver.execute_script(script, source, target) # выполнение JavaScript для имитации drag-and-drop между элементами-источником и целью

    def go_to_order_feed(self): # метод для перехода на страницу ленты заказов, кликая по соответствующей ссылке
        self.click_element(BaseLocators.ORDER_FEED_LINK) # клик по элементу с локатором ORDER_FEED_LINK для перехода на страницу ленты заказов

    def go_to_constructor(self): # метод для перехода на страницу конструктора, кликая по соответствующей ссылке
        self.click_element(BaseLocators.CONSTRUCTOR_LINK) # клик по элементу с локатором CONSTRUCTOR_LINK для перехода на страницу конструктора