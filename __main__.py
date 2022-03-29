from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    driver = webdriver.Firefox()
    driver.get("www.svt.se")

if __name__ == "__main__":
    main()