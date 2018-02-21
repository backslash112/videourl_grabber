import glob
import os
import codecs

file_name = "/Users/mengtingyao/Downloads/video.txt"
result = []
title = ''
with codecs.open(file_name, 'rb', encoding='UTF-8') as fin:
    for line in fin:
#        print(line)
        result.append(line)



def get_name_from_url(file_url):
    return file_url.split('/')[-1][0:-4]

def check(name, mylist):
    for item in mylist:
        if name in item:
            return item.split(';')[0]
    return ''


list_of_files = glob.glob('/Users/mengtingyao/Downloads/*.mp*')
def run():
    for file_url in list_of_files:
        old_name = get_name_from_url(file_url)
        title = check(old_name, result)
        if title:
            print(title)
            new_file_url = file_url.replace(old_name, title)
            os.rename(file_url, new_file_url)

run()
            

