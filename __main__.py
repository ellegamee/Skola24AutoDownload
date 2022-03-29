from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

def main():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get("www.svt.se")

if __name__ == "__main__":
    main()