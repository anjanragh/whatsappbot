import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import csv
import random
options = Options()
# options.headless = True
driver = webdriver.Firefox(options=options)
# driver.get('http://google.com')
# print(driver.title)
# driver.quit()

listofjokes = []
with open("../../../Desktop/cleanjokes.csv") as c:
    spamreader = csv.reader(c, delimiter=',')
    for row in spamreader:
        listofjokes.append(row)
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 24000)


def sendMessage():
    string = listofjokes[random.randint(1, len(listofjokes))][1]
    print(string)

    # Replace 'Friend's Name' with the name of your friend
    # or the name of a group
    target = '"Amuse me"'

    # Replace the below string with your own message

    # string = "Test message sent using Python!!!"
    print("It comes here\n")
    x_arg = '//span[contains(@title,' + target + ')]'
    group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    print(group_title, "Is the title")
    group_title.click()
    print("group_title", group_title)
    inp_xpath = '//div[@spellcheck="true"][@data-tab="1"]'
    input_box = wait.until(EC.presence_of_element_located((
        By.XPATH, inp_xpath)))
    for i in range(1):
        input_box.send_keys(string + Keys.ENTER)
        time.sleep(1)


while(True):
    try:
        sendMessage()
    except:
        continue
# try:
#     while(True):
#         sendMessage()
# except:
#     print("Error")
