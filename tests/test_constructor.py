from locators.locators import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestStellarBurgersConstructorForm:

    def test_constructor_go_to_sauces_scroll_to_sauces(self, driver, login):
        """ Проверка перехода на "Соусы" """
        WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located(MainPage.mn_sauces_button))
        driver.find_element(*MainPage.mn_sauces_button).click()
        WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located(MainPage.current_tab_xpath))

        # Проверка текущей вкладки
        current_tab = driver.find_element(*MainPage.current_tab_xpath).text
        assert current_tab == 'Соусы', f'Ожидалось "Соусы", но найдено "{current_tab}"'



    def test_constructor_go_to_filling_scroll_to_filling(self, driver, login):
        """Проверка перехода на "Начинки" """
        WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.XPATH, MainPage.mn_filling_button)))
        driver.find_element(By.XPATH, MainPage.mn_filling_button).click()
        WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.XPATH, MainPage.current_tab_xpath)))

        current_tab = driver.find_element(*MainPage.current_tab_xpath).text
        assert current_tab == 'Начинки', f'Ожидалось "Начинки", но найдено "{current_tab}"'

    def test_constructor_go_to_bun_scroll_to_bun(self, driver, login):
        """Проверка перехода на "Булки" """
        WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.XPATH, MainPage.mn_ban_button)))
        driver.find_element(By.XPATH, MainPage.mn_ban_button).click()
        WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.XPATH, MainPage.current_tab_xpath)))

        current_tab = driver.find_element(*MainPage.current_tab_xpath).text
        assert current_tab == 'Булки', f'Ожидалось "Булки", но найдено "{current_tab}"'