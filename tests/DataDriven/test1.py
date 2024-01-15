import time

import openpyxl
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



class Test_Login:

    def read_from_xl(self,filepath):
        credntials = []
        workbook = openpyxl.load_workbook(filepath)
        sheet = workbook.active
        for row in sheet.iter_rows(min_row=2, values_only=True):
            username, password = row
            credntials.append({"username": username, "password": password})
        return credntials

    filepath = r"C:\Users\aksha\OneDrive\Desktop\PyTesting\PythonWebAutomationPro\DataIP.xlsx"
    @pytest.mark.parametrize("cred", read_from_xl(filepath))
    def test_token_req(self,cred):
        username = cred["username"]
        password = cred['password']
        res = test_Login(username, password)

    def test_Login(self):
        driver = webdriver.Chrome()
        driver.get("https://app.vwo.com")

        username = driver.find_element(By.XPATH, "//input[@id='login-username']")
        username.send_keys("contact+atb5x@thetestingacademy.com")

        password = driver.find_element(By.XPATH, "//input[@id='login-password']")
        password.send_keys("ATBx@1234")

        submit = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")
        submit.click()

        time.sleep(10)

        data = driver.find_element(By.XPATH, "//span[@class='Fw(semi-bold) ng-binding']")

        assert data.text == "Aman", "TC1 failed"
