import time

from config import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import pickle
import time


#  Options
options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 "
    "Safari/537.36")
# options.add_argument("--proxy-server=190.61.88.147:8080")
driver = webdriver.Chrome(
    options=options
)


def main():

    try:
        actions = ActionChains(driver)
        print(f"[INFO] Download URL", end="")
        driver.get("https://visa.vfsglobal.com/blr/ru/pol/application-detail")
        driver.maximize_window()
        # Load Page
        print(f" >>> OK")
        print(f"[INFO] Enter Login and Pass", end="")
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))
        )
        time.sleep(1)
        element.click()
        input_user = f'/html/body/app-root/div/app-login/section/div/div/mat-card/form/div[1]/mat-form-field/div/div[' \
                     f'1]/div[3]/input '
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, input_user))
        )
        element.send_keys(user)
        input_pass = f'/html/body/app-root/div/app-login/section/div/div/mat-card/form/div[2]/mat-form-field/div/div[' \
                     f'1]/div[3]/input '
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, input_pass))
        )
        element.send_keys(password)
        print(f" >>> OK\r[INFO] Waiting enter CAPTCHA", end="")
        while True:
            # 1 CBox (VISA Centre)
            element = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="mat-select-0"]/div/div[2]/div'))
            )
            print(f" >>> OK\n[INFO] Enter VISA Centre", end="")
            time.sleep(6)
            element.click()
            element = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="mat-option-1"]/span')))
            element.click()
            print(f" >>> OK\n[INFO] Enter Category", end="")
            # 2 CBox (Category)
            element = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/app-eligibility-criteria/section/form'
                                                          '/mat-card[1]/form/div[2]/mat-form-field/div/div[1]')))
            time.sleep(6)
            element.click()
            element = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="mat-option-246"]/span')))
            time.sleep(6)
            element.click()
            print(f" >>> OK\n[INFO] Enter Sub Category", end="")
            # 3 CBox (Sub Category)
            element = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="mat-select-4"]/div/div[2]/div')))
            time.sleep(6)
            element.click()
            element = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="mat-option-252"]/span')))
            time.sleep(6)
            element.click()
            print(f" >>> OK\n[INFO] Date of Birthday", end="")
            # 4 Date of Birthday
            time.sleep(3)
            actions.send_keys(Keys.TAB)
            actions.send_keys(Keys.ENTER)
            element = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/app-eligibility-criteria/section/form'
                                                          '/mat-card[1]/form/div[4]/div[3]/input')))
            time.sleep(6)
            element.send_keys(DofB)
            print(f" >>> OK\n[INFO] Enter Citizenship", end="")
            # 5 Citizenship
            element = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="mat-select-6"]/div/div[2]')))
            time.sleep(6)
            element.click()
            element = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="mat-option-24"]/span')))
            time.sleep(6)
            element.click()
            print(f" >>> OK")
            # /html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button/span[1]
            time.sleep(6)
            if "Приносим извинения, в настоящий момент нет доступных слотов для записи. " \
               "Пожалуйста, попробуйте позже" in driver.page_source:
                print("[INFO] VISA not received :(    Refresh after 30 second", end="")
                time.sleep(10)
                # Вместо обновления меняем первый бокс
                # 1 CBox (VISA Centre)
                element = WebDriverWait(driver, 60).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="mat-select-0"]/div/div[2]/div'))
                )
                print(f" >>> OK\n[INFO] Refresh Page", end="")
                time.sleep(6)
                element.click()
                element = WebDriverWait(driver, 60).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="mat-option-2"]/span')))
                element.click()
                # driver.refresh()
            else:
                print("[!!!INFO!!!] YEAH, VISA received!!!")
                time.sleep(999999)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    main()
