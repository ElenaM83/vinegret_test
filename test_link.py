import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



@allure.feature("Vinegret.cz")
@allure.story("Переход по ссылкам в разделе контакты")


def test_link():
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
            driver.get(url="https://www.vinegret.cz/kontakty-2021")


        with allure.step("Принимаем cookies"):
            driver.find_element(By.CLASS_NAME, 'fc-button-label').click()


        raw_links = driver.find_elements(By.CSS_SELECTOR, "p > a")
        news_urls = [item.get_attribute("href") for item in raw_links]

        assert news_urls, "Не найдены ссылки на соц сеть"

        for url in news_urls:
            with allure.step(f"Открываем соц сеть по ссылке: {url}"):
                driver.get(url)
                time.sleep(2)
                assert "vinegret" in driver.current_url

    finally:
        driver.quit()