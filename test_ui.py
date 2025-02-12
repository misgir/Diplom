import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure

@pytest.fixture()
def chrome():
    driver = webdriver.Chrome()
    driver.implicitly_wait(200)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title("Поиск фильма по названию")
@allure.description("Входим на страницу филльма и выбираем фильм")
@allure.severity("normal")
def test_search(chrome):
    chrome.get("https://www.kinopoisk.ru/")
    chrome.find_element(By.NAME, "kp_query").send_keys("Остров")
    chrome.find_element(By.ID, "suggest-item-film-397667").click()
    assert chrome.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "Остров проклятых (2009)"


@allure.title("Ищем фильм с помощью ввода символов")
@allure.description("Вводим в поисковую страку символы")
@allure.severity("normal")
def test_negative(chrome):
    chrome.get("https://www.kinopoisk.ru/")
    chrome.find_element(By.NAME, "kp_query").send_keys("@!%")
    assert chrome.find_element(By.XPATH, "//*[contains(@class, 'emptySuggest')]").text == "По вашему запросу ничего не найдено"


@allure.title("Поиск фильма по имени")
@allure.description("Вводим в поисковую строку полное название фильма")
@allure.severity("normal")
def test_search_english(chrome):
    chrome.get("https://www.kinopoisk.ru/")
    chrome.find_element(By.NAME, "kp_query").send_keys("Shutter Island")
    chrome.find_element(By.ID, "suggest-item-film-397667").click()
    assert chrome.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "Остров проклятых (2009)"


@allure.title("Поиск фильма по цифре")
@allure.description("Вводим в поисковую строку одну цифру для поиска фильма")
@allure.severity("normal")
def test_search_by_digit(chrome):
    chrome.get("https://www.kinopoisk.ru/")
    chrome.find_element(By.NAME, "kp_query").send_keys("3")
    chrome.find_element(By.ID, "suggest-item-film-1298149").click()
    assert chrome.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "365 дней (2020)"


@allure.title("Поиск фильма по актеру")
@allure.description("Вводим в поисковую строку имя актера, входим на стрницу с актером для выбора фильмов с ним ")
@allure.severity("normal")
def test_actors(chrome):
    chrome.get("https://www.kinopoisk.ru/")
    chrome.find_element(By.NAME, "kp_query").send_keys("Брэд Питт")
    chrome.find_element(By.ID, "suggest-item-person-25584").click()
    assert chrome.find_element(By.CSS_SELECTOR, "span[data-tid='f22e0093']").text == "Брэд Питт"
