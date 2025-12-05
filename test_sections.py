import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service



@allure.feature("Vinegret.cz")
@allure.story("Проверка ссылок на страницы в блоке Последние Новости")


def test_sections():
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


        raw_links = driver.find_elements(By.CSS_SELECTOR, "#latest-news-scroller .scroller-item div a")
        news_urls = [item.get_attribute("href") for item in raw_links]

        assert news_urls, "Не найдены ссылки на новости"


        for url in news_urls:
            with allure.step(f"Открываем новость по ссылке: {url}"):
                driver.get(url)

                assert "vinegret.cz" in driver.current_url, "Открылась не новостная страница"



    finally:
        driver.quit()