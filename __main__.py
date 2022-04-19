from selenium import webdriver

def main():
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get("https://web.skola24.se/timetable/timetable-viewer/norrkoping.skola24.se/Ebersteinska%20gymnasiet/")

if __name__ == "__main__":
    main()