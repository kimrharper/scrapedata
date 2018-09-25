from bs4 import BeautifulSoup
from selenium import webdriver

url = "www.google.com"
browser = webdriver.PhantomJS()
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')
a = soup.find('section', 'wrapper')