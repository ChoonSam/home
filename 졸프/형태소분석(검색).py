from re import S
from konlpy.tag import Komoran
import sys
import pandas as pd
import csv

df2 = pd.read_csv("C:/Users/장준하/Desktop/형분.csv", encoding='utf-8')

komoran = Komoran()

print(df2)

search = input()

sys.stdout = open('형분.txt', 'w')

try :
    if search not in df2:
        print("찾는 문자열이 존재하지 않습니다.")
    else:
        print("찾는 문자열이 존재합니다.")
        if not(search in df2):
            df2[search] = 1
        else:
            df2[search] = df2[search] + 1

    for line in df2:
            if search not in df2:
                print("찾는 문자열이 존재하지 않습니다.")
            else:
                print("찾는 문자열이 존재합니다.")
                if not(search in df2):
                    df2[search] = 1
                else:
                    df2[search] = df2[search] + 1

except :
    print("None File")

sys.stdout.close()