import tkinter
from tkinter import ttk

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def main():
    def create_circle(x, y, r, canvasName, color): #center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1, fill=color.get())

    def selenium_schoolList():
        school_ul = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div/ul")))
        school_li = school_ul.find_elements(By.TAG_NAME, value="li")

        return [school.get_attribute("data-text") for school in school_li]        
    
    def school_menu_update(selected_school):
        school_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div/input")))
        school_input.send_keys(selected_school + Keys.ENTER)
        
        selenium_classList()
            
    def selenium_classList():
        
        """ WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[3]/div/div/button"))).click()
        test = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.w-widget-timetable-viewer > div.w-page-content > div > div:nth-child(2) > div.w-panel-footer > div:nth-child(1) > div:nth-child(3) > div > div > ul > li:nth-child(1) > a > div > div > span")))
        print("this is important!!!!!", test.text) """
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[3]/div/div/button"))).click()
        class_ul = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[3]/div/div/ul")))
        class_li = class_ul.find_elements(By.TAG_NAME, value="span")
        
        classes = []
        print(class_li)
        for li in class_li:
            print(li.text)
            classes.append(li.text)
        
        class_menu['menu'].delete(0, 'end')
        for class_item in classes:
            class_menu["menu"].add_command(label=class_item, command=class_menu_update)
        # print("li test", test.get_attribute("data-text"))
        
    def class_menu_update(selected_class):
        class_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[3]/div/div/input")))
        class_input.send_keys(selected_class + Keys.ENTER)
        
    def schema_available():
        try:
            schema = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div[2]/div/img")))
        except:
            schema = False
            
        if schema == False:
            schema_state.set("red")
        else:
            schema_state.set("green")
    
    # Initialize selenium
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get("https://web.skola24.se/timetable/timetable-viewer/norrkoping.skola24.se/Ebersteinska%20gymnasiet/")
    
    # Tkinter placement and functionality
    window = tkinter.Tk()
    window.state("zoomed")
    
    selected_school = tkinter.StringVar()
    selected_school.set("Select a school")
    school_menu = tkinter.OptionMenu(window, selected_school, "Select a school", *selenium_schoolList(), command=school_menu_update)
    school_menu.pack()
    
    class_list = []
    selected_class = tkinter.StringVar()
    selected_class.set("Select a class")
    class_menu = tkinter.OptionMenu(window, selected_class, "Select a class", *class_list, command=class_menu_update)
    class_menu.pack()

    schema_state = tkinter.StringVar()
    schema_state.set("red")
    schema_state_circle = tkinter.Canvas(window)
    schema_state_circle.pack()
    
    create_circle(20, 20, 15, schema_state_circle, schema_state)
    
    
    window.mainloop()
    

if __name__ == "__main__":
    main()