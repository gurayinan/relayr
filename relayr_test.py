from core.functions import *


class MediumTestCases(unittest.TestCase, Relayr):

    def setUp(self):
        self.relayr = Relayr()
        self.relayr.driver.get("http://www.google.com")

    def test_search(self):
        self.relayr.send_keys_to_input(GoogleMainPage.MAIN_SEARCH_BOX, "relayr")
        self.relayr.click_on_element(GoogleMainPage.SEARCH_BUTTON)
        self.assertIn("relayr", self.relayr.get_tab_header())

    def test_im_lucky(self):
        self.relayr.send_keys_to_input(GoogleMainPage.MAIN_SEARCH_BOX, "relayr")
        self.relayr.click_on_element(GoogleMainPage.I_FEEL_LUCKY_BUTTON)
        self.assertNotIn("google.com", self.relayr.get_current_url())

    def tearDown(self):
        self.relayr.driver.quit()


if __name__ == "__main__":
    unittest.main()
