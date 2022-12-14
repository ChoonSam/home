from konlpy.tag import Komoran
import sys

komoran = Komoran()

sys.stdout = open('내용 형태소분석.txt', 'w')

try :
    f = open("C:/Users/장준하/Desktop/형태소분석.txt", 'r', encoding='utf-8')
    data = f.readline()
    LineNumber = 1
    morphs = komoran.nouns(data)
    print(morphs)
    
    for Line in f:
        morphs = komoran.nouns(Line)
        print(morphs)
    f.close()
except :
    print("None File")

sys.stdout.close()