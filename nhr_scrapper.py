from selenium import webdriver
import selenium
from selenium.webdriver.chrome.options import Options
import time
import csv
from tqdm import tqdm
import json

options = Options()
options.add_argument("--user-data-dir=C:\\Users\\DELL\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 4")
options.add_experimental_option("excludeSwitches", ["enable-automation","enable-logging"])
options.add_experimental_option('useAutomationExtension', False)

def link_creator():
    keys = []
    chaps = list(map(str, (range(1, 7))))
    filenames = ['第三十卷：第一章《大山》','第三十卷：第二章《雌伏》','第三十卷：第三章《雄飞》','第三十卷：第四章《晓钟》','第三十卷：第五章《胜利欢呼》','第三十卷：第六章《誓愿》']
    subchapter_range = [(61,68),(61,68),(61,65),(71,80),(81,89),(131,139)]
    for subchap in subchapter_range:
        key = []
        min, max = subchap
        t = 1
        while t < min-1:
            key.append(tuple(map(str,(t,t+9))))
            t += 10
        key.append(tuple(map(str,(min, max))))
        keys.append(key)
    return zip(chaps, filenames, keys)

tup = list(link_creator())
print(tup)

driver = webdriver.Chrome('C:\\Users\\DELL\\Desktop\\github_projects\\Scheduled-Whatsapp-Messaging\\chromedriver.exe', options=options)
driver.maximize_window()

# Bypass 'accept cookies'
driver.get('https://www.sokaglobal.org/chs/resources/study-materials/buddhist-study/the-new-human-revolution/vol-30-chapter-3-1-10.html')
time.sleep(5)
try:
    driver.find_element_by_xpath("//*[@id=\"page-top\"]/div[2]/div/div/div[2]/div[2]/a[1]").click()
except:
    pass

for chap, filename, keys in tup[0]: #:4, 6]:
    file_path = 'C:\\Users\\DELL\\Desktop\\NHR2\\{}.txt'.format(filename)
    with open(file_path, 'w', encoding='utf-8-sig') as file:
        start = time.time()
        for min, max in keys:
            url = 'https://www.sokaglobal.org/chs/resources/study-materials/buddhist-study/the-new-human-revolution/vol-30-chapter-{}-{}-{}.html'.format(chap, min, max)
            driver.get(url)
            text = driver.find_element_by_xpath("//*[@class='cp-text01']")
            file.write(text.text)
'''
        text = driver.find_element_by_xpath("//*[@id=\"page-top\"]/div/div[3]/div[1]/div[3]/div[1]")
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
'''