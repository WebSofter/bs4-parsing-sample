#!/usr/bin/env python
from urllib.request import urlopen
from bs4 import BeautifulSoup, NavigableString
import re
import csv

page_start = 0
page_end = 144

def get_page_list(url):
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    listTables = soup.find_all('table', width = re.compile('100%'), attrs={'cellspacing': '0', 'border':'0', 'cellpadding': '4'})
    data = []
    for table in listTables:
        listTr = table.find_all('tr')
        name = listTr[0].find_all('td')[0].text
        date = listTr[0].find_all('td')[2].text
        #question = listTr[1].find_all('td')[0].find('p').text
        #if areatable is None:
        listTr1 = listTr[1].find_all('td')[0]
        if listTr1.select('p') is None:
            pass
        else:
            if(len(listTr1.select('p'))>1):
                question = listTr1.select('p')[0].text
                if isinstance(listTr1.find('p').next_sibling, NavigableString):
                    answer = listTr1.select('p')[1].text
                else:
                    if isinstance(listTr1.find('p').next_sibling, type(None)):
                        answer = listTr1.find_all('p')[-1].text
                    else:
                        answer = listTr1.find('p').next_sibling.text
            else:
                print(listTr1.select('p'))
                question = listTr1.text#listTr1.select('p').text
                answer = ''#listTr1.find('p').next_sibling.text
        data.append({'name':name, 'date':date, 'question': question, 'answer':answer})
        #print(data)
    return data

def write_csv(data, comment_index, page_index):
    with open('file.csv', 'a') as f:
        writer = csv.writer(f, delimiter='|', quoting=csv.QUOTE_MINIMAL)
        #print(data[0]['name'])
        #string = string.replace("\r","")
        #string = string.replace("\n","").replace("\r","")
        name = data['name'].strip()
        if name == "":
            name = "user"+str(comment_index)
        writer.writerow([str(comment_index), str(page_index), name, data['date'], data['question'].replace("\n","").replace("\r",""), data['answer'].replace("\n","").replace("\r",""), 'user'+str(comment_index)+'@mail.ru'])

def get_url(number):
    return 'http://remmob.com/guest/?&page=' + str(number)

#print(get_page_list(get_url(0)))
#data = get_page_list(get_url(0))
#write_csv(data[0], int(0))


p = page_start# page index
c = 0 # comment index
page_end = page_end * 10
while p < page_end:
    #print('Page Num:' + str(i))
    comments = get_page_list(get_url(int(p)))
    for comment in comments:
        write_csv(comment, c, p)
        c += 1
    p = p + 10

# for data in get_page_list(page_url):
#     print(data)

#print(type(lists))
#print(lists)