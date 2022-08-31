import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import openpyxl

# tuy chinh kich thuoc windows va che do an danh
chrome_options = Options()
chrome_options.add_argument("headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("disable-gpu")
# khoi tao doi tuong

driver = webdriver.Chrome(executable_path="C:\\Users\\quyk5\\Desktop\\CNN_Architechture\\selenium\\chromedriver.exe")


# tao request
url = "https://inxpress360.com/ma-buu-dien/"
driver.get(url)

links = driver.find_elements_by_xpath('//*[@id="tve_editor"]/div[6]/div/div[*]/div/div/table/tbody/tr[*]/td[2]/div/p/a')
list_link = [link.get_attribute('href') for link in links]
list_name = [link.text for link in links]
weight = len(list_link)
def crawlData(link, name):
    driver.get(link)
    table = pd.read_html(driver.page_source)
    filename = "C:\\Users\\quyk5\\Desktop\\CNN_Architechture\\selenium\\zipcode\\" + name + ".csv" 
    for i in table:
        i.to_csv(filename, index= False, encoding= 'utf-8-sig')



for j in range(0,weight):
    crawlData(list_link[j], list_name[j])



# for i in range(0,63):
    
#     driver.get(url)
#     list_city = pd.read_html(driver.page_source)
#     filename = "C:\\Users\\quyk5\\Desktop\\CNN_Architechture\\selenium\\zipcode" + city_name[i] + ".csv"
#     for j in list_city:
#         j.to_csv(filename, index= False, encoding='utf-8-sig')








