import time

from config import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pickle
import time

#  Options
options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 "
    "Safari/537.36")
driver = webdriver.Chrome(
    options=options
)


def main():
    try:
        # Load Page
        print(f"[INFO] Download URL", end="")
        driver.get("https://visa.vfsglobal.com/blr/ru/pol/application-detail")
        print(f" >>> OK")
        # Enter Login and Pass
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))
        )
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

        print("[INFO]")
        # Choose a value ComboBox
        # Start Button
        # element = WebDriverWait(driver, 60).until(
        #     EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/app-dashboard/section[1]/div/div['
        #                                               '2]/button/span[1]'))
        # )
        # print("[INFO]")
        # element.click()

        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mat-select-0"]/div/div[2]/div'))
        )
        element.click()
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mat-option-1"]/span')))
        combo = driver.find_element(By.XPATH, '//*[@id="mat-option-1"]/span')
        combo.click()
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/app-eligibility-criteria/section/form'
                                                      '/mat-card[1]/form/div[2]/mat-form-field/div/div[1]')))
        combo = driver.find_element(By.XPATH, '/html/body/app-root/div/app-eligibility-criteria/section/form/mat'
                                              '-card[1]/form/div[2]/mat-form-field/div/div[1]')
        combo.click()
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mat-option-246"]/span')))
        combo = driver.find_element(By.XPATH, '//*[@id="mat-option-246"]/span')
        combo.click()
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mat-select-4"]/div/div[2]/div')))
        combo = driver.find_element(By.XPATH, '//*[@id="mat-select-4"]/div/div[2]/div')
        combo.click()
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mat-option-252"]/span')))
        combo = driver.find_element(By.XPATH, '//*[@id="mat-option-252"]/span')
        combo.click()
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/app-eligibility-criteria/section/form'
                                                      '/mat-card[1]/form/div[4]/div[3]/input')))
        combo = driver.find_element(By.XPATH, '/html/body/app-root/div/app-eligibility-criteria/section/form/mat'
                                              '-card[1]/form/div[4]/div[3]/input')
        combo.send_keys(DofB)
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mat-select-6"]/div/div[2]')))
        combo = driver.find_element(By.XPATH, '//*[@id="mat-select-6"]/div/div[2]')
        combo.click()
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mat-option-24"]/span')))
        combo = driver.find_element(By.XPATH, '//*[@id="mat-option-24"]/span')
        combo.click()
        time.sleep(100)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    main()
