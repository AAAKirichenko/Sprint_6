from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTIONS = (By.CLASS_NAME, "accordion__button")
    TOP_REGISTER_BUTTON = (By.XPATH, "//div[@class='Header_Nav__AGCXC']//button[@class='Button_Button__ra12g']")
    MID_REGISTER_BUTTON = (By.CSS_SELECTOR, ".Home_FinishButton__1_cWm .Button_Button__ra12g")
    LOGO_SAMOCAT = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    LOGO_YANDEX = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")

    @staticmethod
    def answer(number):
        return By.ID, f'accordion__panel-{number-1}'

    @staticmethod
    def question(number):
        return By.ID, f'accordion__heading-{number-1}'

