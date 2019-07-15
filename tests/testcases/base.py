from selenium import webdriver
import unittest


class Base(unittest.TestCase):
    def setUp(self, driver=None, time=30, url=None, accept_next_alert=True):
        self.driver = webdriver.Chrome() if driver is None else driver
        self.driver.implicitly_wait(time)
        self.base_url = url
        self.verificationErrors = []
        self.accept_next_alert = accept_next_alert

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
