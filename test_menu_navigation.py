import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


@allure.feature("Vinegret.cz")
@allure.story("Переход по пунктам меню в шапке сайта")


def test_menu_navigation():
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
            time.sleep(3)

        with allure.step("Принимаем cookies"):
            driver.find_element(By.CLASS_NAME, 'fc-button-label').click()
            time.sleep(2)

        with allure.step("Находим все пункты меню в шапке сайта"):
            menu_items = driver.find_elements(By.CSS_SELECTOR, ".top-line a")
            assert menu_items, "Пункты меню не найдены в шапке сайта"


        actions = ActionChains(driver)

        # Проходим по каждому пункту меню
        for index in range(len(menu_items)):
            menu_items = driver.find_elements(By.CSS_SELECTOR, ".top-line a")
            item = menu_items[index]

            link_text = item.text.strip()
            href_before = item.get_attribute("href")

            with allure.step(f"Кликаем по пункту меню: {link_text}"):
                actions.move_to_element(item).pause(0.2).click().perform()
                time.sleep(2)


    finally:
        driver.quit()
