from locators.locators import *


class TestStellarBurgersConstructorForm:

    def test_constructor_go_to_sauces_scroll_to_sauces(self, login):
        """Проверка перехода на "Соусы" """
        driver = login

        sauce_class = h_sauce.get_attribute("class")
        expected_class = 'Соусы'

        assert expected_class in sauce_class, f"Ожидаемый класс '{expected_class}' не найден в '{sauce_class}'"



    def test_constructor_go_to_filling_scroll_to_filling(self, login):
        """Проверка перехода на "Начинки" """
        driver = login

        filling_class = h_filling.get_attribute("class")
        expected_class = 'Начинки'

        assert expected_class in filling_class, f"Ожидаемый класс '{expected_class}' не найден в '{filling_class}'"

    def test_constructor_go_to_bun_scroll_to_bun(self, login):
        """Проверка перехода на "Булки" """
        driver = login

        bun_class = h_bun.get_attribute("class")
        expected_class = 'Булки'

        assert expected_class in bun_class, f"Ожидаемый класс '{expected_class}' не найден в '{bun_class}'"