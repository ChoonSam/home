from konlpy.tag import Komoran
import sys
import pandas as pd
from regex import D
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import csv

komoran = Komoran()
lst = []
tyu = []

nnn = pd.read_csv("C:/Users/장준하/Desktop/nnnn.csv", encoding='utf-8')

try :
    f = open("C:/Users/장준하/Desktop/검색어추출.txt", 'r', encoding='utf-8')
    data = f.readline()
    LineNumber = 1
    search = input()
    counting1 = data.count(search)
    lst.append(counting1)
    
    for Line in f:
        counting2 = (Line.count(search))
        lst.append(counting2)
    f.close()
except :
    print("None File")

idx = lst.index(max(lst))
car = (nnn.iloc[[idx]])
car.to_csv("검색어.csv", encoding='utf-8-sig')
sl = []
with open("D:/visual code/검색어.csv", 'rt', encoding='utf-8')as f:
    dt = csv.reader(f)
    ylst = list(dt)
    pt = ylst[1][1]

##########################################################################################################

df2 = pd.read_csv("C:/Users/장준하/Desktop/dataset.csv", encoding='utf-8')

tfidf = TfidfVectorizer(stop_words='english')

tfidf_matrix = tfidf.fit_transform(df2['content'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(df2.index, index=df2['destination']).drop_duplicates()

def get_recommendations(destination, cosine_sim=cosine_sim):
    idx = indices[destination]
    
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    sim_scores = sim_scores[0:10]
    
    destination_indices = [i[0] for i in sim_scores]
    
    return df2['destination'].iloc[destination_indices]

ghj = get_recommendations(pt)
print(ghj)
ghj.to_csv("결과값.csv", encoding='utf-8-sig')

with open("D:/visual code/결과값.csv", 'rt', encoding='utf-8')as h:
        bb = csv.reader(h)
        ppp = list(bb)
        bbbb = int(ppp[1][0]) + 1
        dddd = int(ppp[2][0]) + 1
        eeee = int(ppp[3][0]) + 1
        gggg = int(ppp[4][0]) + 1
        iiii = int(ppp[5][0]) + 1
        jjjj = int(ppp[6][0]) + 1
        kkkk = int(ppp[7][0]) + 1
        llll = int(ppp[8][0]) + 1
        mmmm = int(ppp[9][0]) + 1
        nnnn = int(ppp[10][0]) + 1
        with open("C:/Users/장준하/Desktop/dataset.csv", 'rt', encoding='utf-8')as a:
            tt = csv.reader(a)
            lll = list(tt)
            b = lll[int(bbbb)][2]
            d = lll[int(dddd)][2]
            e = lll[int(eeee)][2]
            g = lll[int(gggg)][2]
            i = lll[int(iiii)][2]
            j = lll[int(jjjj)][2]
            k = lll[int(kkkk)][2]
            l = lll[int(llll)][2]
            m = lll[int(mmmm)][2]
            n = lll[int(nnnn)][2]

print(bbbb,dddd,eeee,gggg,iiii,jjjj,kkkk,llll,mmmm,nnnn)
print(b)
print(d)
print(e)
print(g)
print(i)
print(j)
print(k)
print(l)
print(m)
print(n)
