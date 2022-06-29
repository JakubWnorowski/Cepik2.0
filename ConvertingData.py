# -*- coding: utf-8 -*-

#This part is reading data from Cepik results, changes it to SQL queries and saving to file. This is 1st part of application
#It can be said that it is primitive json to sql data converter :))

import datetime
import math
import requests

#Years to find
startingYear = 1950
endingYear = 1953  #For read to today - use datetime library  --- NOTE: It spend a huge amount of time

result = []
counter = 0
pages = 2
count = 0
table_name = "data"

#This function return SQL code to buid a database using the data from cepik
def tableCreator(str0):
    global counter
    global result
    global pages

    tresult = []
    tab = str0.split('"')

    for i in range(0, len(tab)):

        if(tab[i] == "id"):
            tresult.append(counter)
            tresult.append(str(tab[i+2]))
        if(tab[i] == "type"):
            tresult.append(str(tab[i + 2]))
        if(tab[i] == "marka"):
            tresult.append(str(tab[i + 2]))
        if (tab[i] == "kategoria-pojazdu"):
            tresult.append(str(tab[i + 2]))
        if (tab[i] == "typ"):
            tresult.append(str(tab[i + 2]))
        if (tab[i] == "model"):
            tresult.append(str(tab[i + 2]))
        if (tab[i] == "wariant"):
            tresult.append(str(tab[i + 2]))
        if (tab[i] == "rodzaj-pojazdu"):
            tresult.append(str(tab[i + 2]))
        if (tab[i] == "pochodzenie-pojazdu"):
            tresult.append(str(tab[i + 2]))
        if (tab[i] == "rok-produkcji"):
            tresult.append(str(tab[i + 2]))
        if (tab[i] == "data-pierwszej-rejestracji-w-kraju"):
            tresult.append(str(tab[i + 2]))
        if (tab[i] == "pojemnosc-skokowa-silnika"):
            tresult.append(str(tab[i + 1][1:-1]))
        if (tab[i] == "masa-wlasna"):
            tresult.append(str(tab[i + 1][1:-1]))
        if (tab[i] == "rodzaj-paliwa"):
            if(tab[i+2] == "wojewodztwo-kod"):
                tresult.append("null")
                continue
            tresult.append(str(tab[i + 2]))
        if (tab[i] == "wojewodztwo-kod"):
            tresult.append(str(tab[i + 2]))
            counter += 1
            result.append(tresult)
            tresult = []


#Reading loop
for i in range(startingYear, endingYear+1):

    #Read first page
    page_url = "https://api.cepik.gov.pl/pojazdy?wojewodztwo=20&data-od=" + str(i) + "0101&data-do=" + str(i) + "1231&limit=500&page=1"
    page = requests.get(page_url)
    data = str(page.content)
    tab = data.split('"')

    #Define number of pages in current year
    for k in range(0, len(tab)):
        if (tab[k] == "count"):
            count = str(tab[k + 1][1:-1])
            pages = math.ceil(int(count) / 500)

    #Read data from next pages
    for j in range(1, pages+1):
        page_url = "https://api.cepik.gov.pl/pojazdy?wojewodztwo=20&data-od=" + str(i) + "0101&data-do="+ str(i) + "1231&limit=500&page=" + str(j)
        page = requests.get(page_url)
        data = str(page.content)
        tableCreator(data)

    print(str(i) + " - " + str(len(result)))
    print("Pomyslnie wczytano rok " + str(i))


#Saving to file
file = open("data.txt", "w")
for i in result:
    print('INSERT INTO `'+ table_name + '` (`id`, `type`, `marka`, `kategoria-pojazdu`, `typ`, `model`, `wariant`, `rodzaj-pojazdu`, `pochodzenie-pojazdu`, `rok-produkcji`, `data-pierwszej-rejestracji-w-kraju`, `pojemnosc-skokowa-silnika`, `masa-wlasna`, `rodzaj-paliwa`, `wojewodztwo-kod`) VALUES ("'+ str(i[1]) + '", "' + str(i[2]) + '", "' + str(i[3]) + '", "' + str(i[4]) + '", "' +str(i[5]) + '", "' +str(i[6]) + '", "' +str(i[7]) + '", "' +str(i[8]) + '", "' +str(i[9]) + '", "' +str(i[10]) + '", "' +str(i[11]) + '", "' +str(i[12]) + '", "' +str(i[13]) + '", "' +str(i[14]) + '", "' +str(i[15]) +'");', file=file)
file.close()