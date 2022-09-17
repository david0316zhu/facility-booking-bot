from selenium import webdriver
username = 
password = 
url = 
driver = webdriver.Chrome("C:/Users/User/Downloads/chromedriver_win32/chromedriver.exe")
driver.get(url)
driver.find_element_by_id("userNameInput").send_keys(username)
driver.find_element_by_id("passwordInput").send_keys(password)
driver.find_element_by_id("submitButton").click()


building_type = ["LKSLIB", "LKCSB", "SCIS1", "SOA", "SOE/SCIS2"]
room_type = ["Classroom", "GSR", "Seminar Room"]