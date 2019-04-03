import bs4
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager


def get_info():
    base_url = 'https://www.dba.dk/'
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(base_url)
    browser.implicitly_wait(3)
    name = "cykler"

    search_field = browser.find_element_by_id('searchField')
    search_field.send_keys(name)
    search_field.submit()


# find oprettet and click "Seneste 24 timer" and select "København og omegn"

    click_on_Newest = browser.find_elements_by_class_name("radioNavigator")
    click_on_Newest[0].click()

    select_24_hours = browser.find_element_by_xpath(
        "//*[contains(text(), 'Seneste 24 timer')]")
    select_24_hours.click()

    select_copenhagen_area = browser.find_element_by_xpath(
        "//*[contains(text(), 'København og omegn')]")
    select_copenhagen_area.click()

# Sort prices

    #sort_button = browser.find_element_by_xpath("/html/body/div[3]/div[0]/div[0]/section[0]/table[0]/thead[0]/tr[0]/th[3]/span[@data-human-ref='L3NvZWcvP3NvZWc9Y2VudHVyaW9uK2N5a2VsJnNvcnQ9cHJpY2U']")
    sort_button = browser.find_element_by_xpath("/html/body/div[3]/div[0]")
    print(sort_button)

    sleep(30)
    sleep(3)


get_info()
