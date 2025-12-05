
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


@allure.feature("Vinegret.cz")
@allure.story("Поиск по ключевому слову")
@allure.title("Проверка поиска по запросу 'Прага'")
@pytest.mark.parametrize("keyword", ["Прага"])

def test_search_keyword(keyword):
    # Опции браузера
    with allure.step("Настраиваем браузер Chrome"):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--start-maximized")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

    try:
        with allure.step("Открываем сайт Vinegret.cz"):
            driver.get(url="https://www.vinegret.cz/")


        with allure.step("Принимаем cookies"):
            driver.find_element(By.CLASS_NAME, 'fc-button-label').click()


        with allure.step(f"Выполняем поиск по ключевому слову: {keyword}"):
            search_input = driver.find_element(By.ID, 'search')
            search_input.send_keys(keyword)
            search_input.send_keys(Keys.ENTER)

        with allure.step("Ожидаем появления списка с ключевым словом"):
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "search-summary-total"))
            )

            assert keyword in driver.page_source, \
                f"Поиск не выдал результатов по слову '{keyword}'"

    finally:
        driver.quit()