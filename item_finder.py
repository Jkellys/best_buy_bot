from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from multiprocessing.pool import ThreadPool
from multiprocessing import Pool
import os
from pyMail import send_email
from selenium.webdriver.chrome.options import Options


def open_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("disable-gpu")
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    browser = webdriver.Chrome(executable_path='', options=chrome_options)

    time.sleep(5)

    return browser

# message or email me if found
def notify(item_url):
    #This Module Support Gmail & Microsoft Accounts (hotmail, outlook etc..)
    try:
        send_email(item_url)
    except:
        print('email not sent')

# gets the saves a url
def save_items(item):
    text_file = open("items_list.txt", "a")
    text_file.write(str(item) + '\n')
    text_file.close()

# gets all the url
def get_item_list():
    text_file = open("items_list.txt", "r")
    lines = text_file.readlines()
    text_file.close()
    return lines

def input_item():
    item = input("Input the url of new item:")
    if (len(item) != 0):
        save_items(item)
    with Pool(5) as p :
        p.map(open_new_page, get_item_list())


# opens a new browser to scan for a new item
# only on best buy
def open_new_page(item):

    browser = open_browser()

    browser.get(str(item))
    assert "Best Buy" in browser.title
    print("on the best buy site")
    time.sleep(2)

    is_avaliable(browser)

    #item is the url
    notify(item)


def is_avaliable(browser):
    buyButton = False
    time.sleep(5)

    #check for the right element
    body_text = browser.find_element_by_xpath('//*[@id="test"]/button').text
    assert 'Add to Cart' in body_text


    while not buyButton:
        try:
            addToCartBtn = addButton = browser.browser.find_element_by_xpath('//*[@id="test"]/button')
            print( str() + ' cant be added to cart.')

            time.sleep(2)
            browser.refresh()
        except:

            addToCartBtn = addButton = browser.find_element_by_xpath('//*[@id="test"]/button')
            print("buy button clicked")
            addToCartBtn.click()
            buyButton = True


    browser.close()

if __name__ == '__main__':

    input_item()
