import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import datetime
import sys

### Time delay
#time.sleep(60*60*15)

while True:

    keys = []
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mdays = zip(months, days)
    for month in mdays:
        for day in range(month[1]):
            keys.append(month[0]+'-'+str(day))

    yday = int(datetime.datetime.now().strftime('%j'))-1#, datetime.datetime.now())
    englink = 'https://www.sokaglobal.org/resources/daily-encouragement/'+keys[yday+1]+'.html'
    chilink = 'https://www.sokaglobal.org/chs/resources/daily-encouragement/'+keys[yday+1]+'.html'

    engtitle = 'Daily Encouragement'

    with open('C:\\Users\\DELL\\Desktop\\guidance2021.csv', 'r', encoding='utf-8-sig') as file:
        data = pd.read_csv(file, sep=';')

    engdate = data.iloc[yday,0]
    engmessage = data.iloc[yday,1]
    engsensei = 'Daisaku Ikeda, SGI President'
    chititle = '每日一句'
    chidate = data.iloc[yday,2]
    chimessage = data.iloc[yday,3]
    chisensei= '国际创价学会会长池田大作'

    ### Whatsapp automated messaging ###
    def nextline():
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()

    options = Options()
    options.add_argument("--user-data-dir=C:\\Users\\DELL\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 4")
    options.add_experimental_option("excludeSwitches", ["enable-automation","enable-logging"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome('C:\\Users\\DELL\\Desktop\\chromedriver.exe', options=options)
    driver.maximize_window()
    driver.get('https://web.whatsapp.com')  # Already authenticated

    time.sleep(20)

    ##################### Provide Recepient Name Here ###############################
    driver.find_element_by_xpath("//*[@title='+60 18-468 7326']").click()
    

    for eng in [engtitle, engdate, engmessage, engsensei, englink]:
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(eng)
        nextline()
    nextline()
    for chi in [chititle, chidate, chimessage, chisensei, chilink]:
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(chi)
        nextline()

    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()

    time.sleep(5)
    driver.close()
    print('Message sent.', flush=True)

    sleep_duration = 60*10
    rest = interrupt = time.time()
    print(time.strftime('Sleep for %Hh %Mm %Ss ...', time.gmtime(sleep_duration)), flush=True)
    response = 'n'
    while response.lower() == 'n':
        try:
            time.sleep(sleep_duration-(interrupt-rest))#60*24))
            break

        except KeyboardInterrupt:
            interrupt = time.time()
            print(time.strftime('Time Elapsed: %Hh %Mm %Ss', time.gmtime(interrupt-rest)))
            print(time.strftime('Time Left: %Hh %Mm %Ss', time.gmtime(sleep_duration-(interrupt-rest))))
            response = input('Stop automated messaging? [y/N]... ')
            while response.lower() not in ['y', 'n']:
                response = input('Stop automated messaging? [y/N]... ')
            if response.lower() == 'y':
                sys.exit()
            else:
                print(time.strftime('Continue sleep for %Hh %Mm %Ss ...', time.gmtime(sleep_duration-(interrupt-rest))), flush=True)