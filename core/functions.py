from core.imports import *


class Relayr(object):

    def __init__(self):
        self.driver_location = os.path.join(os.getcwd(), 'core', 'drivers')
        current_os = sys.platform
        if current_os == "linux2":
            self.driver_location = os.path.join(self.driver_location, 'chromedriver_linux2')
        elif current_os == "darwin":
            self.driver_location = os.path.join(self.driver_location, 'chromedriver_darwin')
        elif current_os == "win32":
            self.driver_location = os.path.join(self.driver_location, 'chromedriver_win32.exe')
        self.driver = webdriver.Chrome(executable_path=self.driver_location)
        screen_width = self.driver.execute_script("return window.screen.availWidth")
        screen_height = self.driver.execute_script("return window.screen.availHeight")
        self.driver.set_window_position(0,0)
        self.driver.set_window_size(screen_width, screen_height)
        self.wait = WebDriverWait(self.driver, timeout=20)

    def send_keys_to_input(self, input_locator, keys_to_send):
        self.wait.until(ec.visibility_of_element_located(input_locator)).send_keys(keys_to_send)

    def click_on_element(self, input_locator):
        self.wait.until(ec.element_to_be_clickable(input_locator)).click()

    def get_tab_header(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url