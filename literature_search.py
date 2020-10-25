from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("/Users/HP/Desktop/chromedriver")

browser.get("https://ieeexplore.ieee.org/Xplore/home.jsp")

search_box = browser.find_element_by_xpath("//*[@id='LayoutWrapper']/div/div/div/div[4]/div/xpl-root/xpl-header/div/div[4]/xpl-search-bar-migr/div/form/div[2]/div/div/xpl-typeahead-migr/div/input")
search_box.send_keys("requirements engineering, machine learning")
search_box.send_keys(Keys.RETURN)
time.sleep(5)

articles = browser.find_elements_by_class_name("List-results-items")
article_list=[]

for article in articles:
    article_list.append(article.text)

with open("article.txt", "w", encoding="UTF-8") as file:
    for article in article_list:
        file.write(article+"\n\n")
time.sleep(5)


browser.quit()
