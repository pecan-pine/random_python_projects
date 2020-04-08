from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
def google(string):
    return 'http://www.google.com/search?q='+string

stocks = ['s and p 500', 'delta', 'advance auto parts', 'red robin', 'ford', 'nokia']

for stock in stocks:
    browser.get(google(stock + ' stock'))
    if stocks.index(stock) != len(stocks)-1:
        browser.execute_script("window.open('');")
        browser.switch_to.window(browser.window_handles[stocks.index(stock)+1])


