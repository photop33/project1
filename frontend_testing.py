
from selenium import webdriver

def user_name(a):
    a=str(a)
    driver = webdriver.Chrome("C:\\Users\\l1313\\Desktop\\chromedriver.exe")
    driver.get("http://127.0.0.1:5000/user/" + a + "")
    x=driver.find_element_by_xpath('/html/body/pre')
    print(x.text)
    
user_name(1)

