import allure
from locators.rent_page_locators import RentPageLocators
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step("Подождать загрузки формы Для кого самокат")
    def wait_for_personal_list(self):
        self.wait_for_element(OrderPageLocators.PERSONAL_FORM)

    @allure.step('Заполнить форму Для кого самокат')
    def input_personal_information(self, name, surname, address, metro_st, phone):
        name_locator = OrderPageLocators.INPUT_NAME
        self.click_on_element(name_locator)
        self.send_keys_to_input(name_locator, name)

        surname_locator = OrderPageLocators.INPUT_SURNAME
        self.click_on_element(surname_locator)
        self.send_keys_to_input(surname_locator, surname)

        address_locator = OrderPageLocators.INPUT_ADDRESS
        self.click_on_element( address_locator)
        self.send_keys_to_input(address_locator, address)

        metro_locator = OrderPageLocators.INPUT_METRO_ST
        self.click_on_element(metro_locator)
        self.send_keys_to_input(metro_locator, metro_st + "\ue015" + "\ue007")

        phone_locator = OrderPageLocators.INPUT_PHONE
        self.click_on_element(phone_locator)
        self.send_keys_to_input(phone_locator, phone)

    @allure.step('Кликнуть по кнопке "Далее" для перехода на форму аренды')
    def click_on_button_next(self):
        self.click_on_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Заполнить форму про аренду')
    def input_rent_info(self, data, comment):
        data_locator = RentPageLocators.DATA_FIELD
        self.click_on_element(data_locator)
        self.send_keys_to_input(data_locator, data + "\ue007")

        comment_locator = RentPageLocators.COMMENT
        self.click_on_element(comment_locator)
        self.send_keys_to_input(comment_locator, comment)

        self.click_on_element(RentPageLocators.TIME_FIELD)
        self.click_on_element(RentPageLocators.SELECT_TIME)
        self.click_on_element(RentPageLocators.COLOR_BLACK)

    @allure.step('Кликнуть кнопку "Заказать" для завершения заказа')
    def click_on_button_order(self):
        self.click_on_element(RentPageLocators.ORDER_BUTTON)

    @allure.step('Кликнуть кнопку "Да" для подтверждения заказа')
    def click_on_button_yes(self):
        self.click_on_element(RentPageLocators.YES_BUTTON)

    @allure.step('Кликнуть кнопку Посмотреть статус')
    def click_on_button_see_status(self):
        self.click_on_element(RentPageLocators.SEE_STATUS)

    @allure.step("Получить текст Заказ оформлен")
    def get_text_check_order(self):
        return self.get_text_on_element(RentPageLocators.CHECK_ORDER)
