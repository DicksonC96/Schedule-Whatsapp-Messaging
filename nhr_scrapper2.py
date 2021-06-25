import os
import time

def link_creator():
    keys = []
    chapter_range = [4,6]
    subchapter_range = [(71,80),(131,139)]#[(61,68),(61,68),(61,65),(71,80),(81,89),(131,139)]
    for chap, subchap in zip(chapter_range, subchapter_range):
        min, max = subchap
        t = 1
        while t < min-1:
            keys.append(tuple(map(str,(chap,t,t+9))))
            t += 10
        keys.append(tuple(map(str,(chap, min, max))))
    return keys

def scrapper(keys):
    for chap, min, max in keys:
        filenames = []
        path_to_file = 'C:\\Users\\DELL\\Desktop\\NHR\\'
        name_of_file = '{}-{}-{}.pdf'.format(chap, min, max)
        page_to_open = 'https://www.sokaglobal.org/chs/resources/study-materials/buddhist-study/the-new-human-revolution/vol-30-chapter-{}-{}-{}.html'.format(chap, min, max)

        command_to_run = 'start chrome --headless --print-to-pdf="{0}{1}" {2}'.format(path_to_file, name_of_file, page_to_open)
        print('launch:'+command_to_run)

        os.popen(command_to_run)
        filenames.append(path_to_file+name_of_file)
    time.sleep(30)
    filesizes = [os.path.getsize(file) for file in filenames]
    return filesizes

# Retry loop
keys = link_creator()
print(keys)
while keys:
    filesizes = scrapper(keys)
    keys = [keys[i] for i in range(len(filesizes)) if filesizes[i] < 400000]
    print(keys)