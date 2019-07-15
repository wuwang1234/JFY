from tests.testcases.base import Base
import time
import random


class Registor(Base):
    url = 'http://129.28.40.179:5000'

    def setUp(self):
        super(Registor, self).setUp(url=self.url)

    def test_registor(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        registor_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[2]/a")
        registor_button.click()
        username = driver.find_element_by_id('username')
        number = driver.find_element_by_id('number')
        email = driver.find_element_by_id('email')
        passwd = driver.find_element_by_id('passwd')
        username.send_keys('zhanghong' + str(random.randint(1,100000)))
        number.send_keys('18829291209')
        email.send_keys('2382725346@qq.com')
        passwd.send_keys('zxcv123wuwang')
        submit = driver.find_element_by_id('submit')
        submit.click()
        print(driver.page_source)
        time.sleep(10)
        driver.close()
