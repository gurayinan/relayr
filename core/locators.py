from selenium.webdriver.common.by import By


class GoogleMainPage(object):

    MAIN_SEARCH_BOX = (By.ID, "lst-ib")
    SEARCH_BUTTON = (By.NAME, "btnK")
    I_FEEL_LUCKY_BUTTON = (By.NAME, "btnI")