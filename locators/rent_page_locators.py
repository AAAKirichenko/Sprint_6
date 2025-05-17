from selenium.webdriver.common.by import By


class RentPageLocators:
    DATA_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    TIME_FIELD = (By.XPATH, "//div[text()='* Срок аренды']")
    SELECT_TIME = (By.CSS_SELECTOR, "div.Dropdown-option:nth-child(2)")
    COLOR_BLACK = (By.ID, "black")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.CSS_SELECTOR, "button.Button_Middle__1CSJM:nth-child(2)")
    YES_BUTTON = (By.CSS_SELECTOR, "div.Order_Buttons__1xGrp:nth-child(2) > button:nth-child(2)")
    SEE_STATUS = (By.XPATH, ".// button[text() = 'Посмотреть статус']")
    CHECK_ORDER = (By.XPATH, ".//div[contains(text(), 'Самокат на складе')]")