from selenium.webdriver.common.by import By


class HeaderLocators:
    CONSTRUCT_BUTTON = (By.XPATH, ".//p[contains(text(), 'Конструктор')]")
    FEED_BUTTON = (By.XPATH, ".//p[contains(text(), 'Лента Заказов')]")
    ACCOUNT_BUTTON = (By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]")


class MainPageLocators:
    FEED_FORM = (By.XPATH, ".//div[@class = 'OrderFeed_orderFeed__2RO_j']")
    CONSTRUCT_FORM = (By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']")
    ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    INGREDIENT_BUN = (By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']")
    CLOSE_DETAILS_BUTTON = (By.XPATH, '//button[contains(@class,"close")]')
    ORDER_FORM = (By.XPATH, ".//div[@class = 'Modal_modal__container__Wo2l_']")
    BASKET = (By.XPATH, ".//div[contains(@class, 'constructor-element_pos_top')]")
    COUNTER_INGREDIENT = (By.XPATH, ".//p[contains(@class, 'counter_counter__num__3nue1')]")
    NUMBER_ORDER = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]")
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")
    POPUP_FORM_DETAILS = (By.XPATH, "//h2[text()= 'Детали ингредиента']")


class LoginPageLocators:
    AUTH_FORM = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']")
    EMAIL_INPUT = (By.XPATH, ".//input[@name = 'name']")
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text() = 'Войти']")
    RECOVER_BUTTON = (By.XPATH, "//a[text() = 'Восстановить пароль']")


class RecoverAndResetPageLocators:
    FIELD_EMAIL = (By.XPATH, ".//input[@name = 'name']")
    BUTTON_RECOVER = (By.XPATH, "//button[text() = 'Восстановить']")
    BUTTON_LOGIN = (By.XPATH, ".//a[text() = 'Войти']")
    FIELD_NEW_PASSWORD = (By.XPATH, ".//input[@name = 'Введите новый пароль']")
    FIELD_CODE_FROM_EMAIL = (By.XPATH, ".//label[text() = 'Введите код из письма']")
    SHOW_PASSWORD = (By.XPATH, ".//div[@class = 'input__icon input__icon-action']")
    ACTIVE_PASSWORD_FIELD = (By.CSS_SELECTOR, ".input.input_status_active")
    SAVE_BUTTON = (By.XPATH, ".//button[text() = 'Сохранить']")
    TITLE_RECOVER = (By.XPATH, ".//h2[text() = 'Восстановление пароля']")


class PersonalAccountLocators:
    ACCOUNT_FORM = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']")
    BUTTON_PROFILE = (By.XPATH, ".//a[text() = 'Профиль']")
    BUTTON_HISTORY_ORDER = (By.XPATH, ".//a[text() = 'История заказов']")
    FORM_HISTORY_FORM = (By.XPATH, ".//div[@class = 'Account_contentBox__2CPm3']")
    BUTTON_LOGOUT = (By.XPATH, ".//button[text() = 'Выход']")


class OrderFeedLocators:
    INFO_ORDER = (By.XPATH, '//p[text()="Cостав"]')
    TITLE_ORDER_FEED = (By.XPATH, '//h1[text()="Лента заказов"]')
    COUNTER_ORDERS_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    COUNTER_ORDERS_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    COUNTER_ORDERS_PROGRESS = (By.XPATH, ".//li[contains(@class, 'text_type_digits-default')]")
    ORDER_WINDOW = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem__2x95r')][1]")
    ORDER_HISTORY = (By.XPATH, './/p[contains(@class, "text_type_digits-default")]')
