from selenium import webdriver

def main():
    driver = webdriver.Chrome()
    driver.get("www.svt.se")

if __name__ == "__main__":
    main()