from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import time

def main():
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get("https://web.skola24.se/timetable/timetable-viewer/norrkoping.skola24.se/Ebersteinska%20gymnasiet/")
    
    schoolList = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div/button")))
    schoolList.click()
    time.sleep(5)

    driver.quit()

if __name__ == "__main__":
    main()