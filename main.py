import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pickle
import time

#  Options
options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
driver = webdriver.Chrome(
    options=options
)


def main():
    try:
        # Load Page
        print(f"[INFO] Download URL", end="")
        driver.get("https://visa.vfsglobal.com/blr/ru/pol/application-detail")
        print(f" >>> OK")
        time.sleep(10)

        # Enter Login and Pass
        time.sleep(1)
        input_user = f'/html/body/app-root/div/app-login/section/div/div/mat-card/form/div[1]/mat-form-field/div/div[' \
                    f'1]/div[3]/input '
        driver.find_element(By.XPATH, value=input_user).send_keys("v2322048@gmail.com")
        input_pass = f'/html/body/app-root/div/app-login/section/div/div/mat-card/form/div[2]/mat-form-field/div/div[' \
                     f'1]/div[3]/input '
        driver.find_element(By.XPATH, value=input_pass).send_keys("JFRfm5neYAeNQj*")
        time.sleep(60)
        print("123")

        # Нажимаем на комбобокс
        combo = driver.find_element(By.XPATH, '//*[@id="mat-select-0"]/div/div[2]/div')
        combo.click()

        # Rec Cookies
        time.sleep(100)
        print(f"[INFO] Save Cookie", end="")
        pickle.dump(driver.get_cookies(), open("cookies_visa", "wb"))
        print(" >>> OK")
        # Download Cookies
        # print(f"[INFO] Download Cookie", end="")
        # for cookie in pickle.load(open("cookies", "rb")):
        #     driver.add_cookie(cookie)
        # print(" >>> OK")
        # time.sleep(10)
        # driver.refresh()
        time.sleep(100)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    main()
