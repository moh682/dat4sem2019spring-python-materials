from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


base_url = 'http://www.kultunaut.dk/perl/arrlist/type-nynaut/UK?showmap=&Area=Kbh.+og+Frederiksberg&periode=&Genre=Musik'
# to make that work on OS X I had to: brew install geckodriver
browser = webdriver.Firefox()
browser.get(base_url)

# Scroll down
browser.find_element_by_tag_name('body').send_keys(Keys.END)
# Scroll up
browser.find_element_by_tag_name('body').send_keys(Keys.HOME)

browser.find_elements_by_link_text('Next page')[0].click()
browser.find_element_by_tag_name('body').send_keys(Keys.END)
sleep(2)

browser.find_elements_by_link_text('Next page')[0].click()
browser.find_element_by_tag_name('body').send_keys(Keys.END)
sleep(2)

browser.find_elements_by_link_text('Next page')[0].click()
browser.find_element_by_tag_name('body').send_keys(Keys.END)
sleep(2)

browser.find_elements_by_link_text('Next page')[0].click()
browser.find_element_by_tag_name('body').send_keys(Keys.END)
sleep(2)
