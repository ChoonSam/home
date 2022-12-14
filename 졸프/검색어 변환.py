from konlpy.tag import Komoran
import sys
import pandas as pd
import csv

komoran = Komoran()
lst = []
car = []
#sys.stdout = open('mmmm.txt', 'w')
nnn = pd.read_csv("C:/Users/장준하/Desktop/nnnn.csv", encoding='utf-8')

try :
    f = open("C:/Users/장준하/Desktop/검색어추출.txt", 'r', encoding='utf-8')
    data = f.readline()
    LineNumber = 1
    #morphs = komoran.nouns(data)
    search = input()
    counting1 = data.count(search)
    lst.append(counting1)
    
    for Line in f:
        #morphs = komoran.nouns(Line)
        counting2 = (Line.count(search))
        lst.append(counting2)
    f.close()
except :
    print("None File")

#print(lst)
idx = lst.index(max(lst))
#print(idx)
car = (nnn.iloc[[idx]])
#print(car)
car.to_csv("검색어.csv", encoding='utf-8-sig')

sl = []
with open("D:/visual code/검색어.csv", 'rt', encoding='utf-8')as f:
    dt = csv.reader(f)
    ylst = list(dt)
    pt = ylst[1][1]
print(pt)