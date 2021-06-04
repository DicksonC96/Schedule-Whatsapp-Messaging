from selenium import webdriver
import selenium
from selenium.webdriver.chrome.options import Options
import time
import csv
from tqdm import tqdm

options = Options()
options.add_argument("--user-data-dir=C:\\Users\\DELL\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 4")
options.add_experimental_option("excludeSwitches", ["enable-automation","enable-logging"])
options.add_experimental_option('useAutomationExtension', False)

def link_creator():
    keys = []
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    days = range(1,32)
    for month in months:
        for day in days:
            keys.append(month+'-'+str(day))
    return keys

keys = link_creator()
print(keys)

driver = webdriver.Chrome('C:\\Users\\DELL\\Desktop\\chromedriver.exe', options=options)
driver.maximize_window()

# Bypass 'accept cookies'
driver.get('https://www.sokaglobal.org/resources/daily-encouragement/may-1.html')
time.sleep(5)
try:
    driver.find_element_by_xpath("//*[@id=\"page-top\"]/div[2]/div/div/div[2]/div[2]/a[1]").click()
except:
    pass

with open('C:\\Users\\DELL\\Desktop\\guidance1.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['EngDate', 'EngGuidance', 'ChiDate', 'ChiGuidance'])
    #file.write('EngDate|EngGuidance|ChiDate|ChiGuidance\n')
    start = time.time()
    for key in tqdm(keys, total=len(keys), ncols=100):
        texts = []
        driver.get('https://www.sokaglobal.org/resources/daily-encouragement/'+key+'.html')
        try:
            engdate = driver.find_element_by_xpath("//*[@id=\"page-top\"]/div/div[3]/div[1]/div[3]/div[1]")
            engguidance = driver.find_element_by_xpath("//*[@id=\"page-top\"]/div[1]/div[3]/div[1]/div[3]/div[2]")
            texts.append(engdate.text)
            texts.append(engguidance.text)
            #file.write(engdate.text+'|'+engguidance.text+'|')
        except:
            texts.append(key)
            texts.append('N/A')

        driver.get('https://www.sokaglobal.org/chs/resources/daily-encouragement/'+key+'.html')
        try:
            chidate = driver.find_element_by_xpath("//*[@id=\"page-top\"]/div/div[3]/div[1]/div[3]/div[1]")
            chiguidance = driver.find_element_by_xpath("//*[@id=\"page-top\"]/div/div[3]/div[1]/div[3]/div[2]")
            writer.writerow([texts[0], texts[1], chidate.text, chiguidance.text])
            #file.write(chidate.text+'|'+chiguidance.text+'\n')
        except:
            writer.writerow([texts[0], texts[1], key,'N/A'])
        
        #writer.writerow([engdate.text, engguidance.text, chidate.text, chiguidance.text])
print(time.time() - start)
driver.close()
