import unittest

from selene.api import *
from selenium import webdriver


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        browser.set_driver(webdriver.Chrome(executable_path='chromedriver.exe', options=options))
        browser.open_url('https://opensource-demo.orangehrmlive.com/index.php/auth/login')

    def tearDownClass(cls) -> None:
        browser.quit()

    def test_01_login_with_incorrect_username(self):
        s('input[id="txtUsername"]').send_keys('Daddy')
        s('input[id="txtPassword"]').send_keys('admin123')
        s('input[id="btnLogin"]').click()
        assert s('span[id="spanMessage"]').is_displayed()

    def test_02_login_with_incorrect_password(self):
        s('input[id="txtUsername"]').send_keys('Admin')
        s('input[id="txtPassword"]').send_keys('admin123123')
        s('input[id="btnLogin"]').click()
        assert s('span[id="spanMessage"]').is_displayed()

    def test_03_login_with_incorrect_username_and_password(self):
        s('input[id="txtUsername"]').send_keys('Daddy')
        s('input[id="txtPassword"]').send_keys('admin123234')
        s('input[id="btnLogin"]').click()
        assert s('span[id="spanMessage"]').is_displayed()

    def test_04_login_with_correct_credentials(self):
        s('input[id="txtUsername"]').send_keys('Admin')
        s('input[id="txtPassword"]').send_keys('admin123')
        s('input[id="btnLogin"]').click()
        assert s('.head h1').should(have.text("Dashboard"))


if __name__ == '__main__':
    unittest.main()
