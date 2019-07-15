from tests.testcases.base import Base
import time


class Login(Base):
    url = 'http://129.28.40.179:5000'

    def setUp(self):
        super(Login, self).setUp(url=self.url)

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        login_button = driver.find_element_by_css_selector('body > div.navbar.navbar-inverse > div > div.navbar-collapse.collapse > ul > li:nth-child(1) > a')
        login_button.click()
        username = driver.find_element_by_id('username')
        passwd = driver.find_element_by_id('passwd')
        username.send_keys('zhanghong')
        passwd.send_keys('zxcv123wuwang')
        submit = driver.find_element_by_id('submit')
        submit.click()
        time.sleep(1)
        print(driver.page_source)
        driver.close()
