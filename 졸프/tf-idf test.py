import pandas as pd
from math import log
import sys

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows', None)
 
#docs = pd.read_csv("C:/Users/장준하/Desktop/test.csv",  encoding='cp949')
docs = [
    "네가 참 궁금해 그건 너도 마찬가지",
    "이거면 충분해 쫓고 쫓는 이런 놀이",
    "참을 수 없는 이끌림과 호기심",
    "묘한 너와 나 두고 보면 알겠지",
    "Woo 눈동자 아래로",
    "Woo 감추고 있는 거",
    "Woo yeah It's so bad It's good",
    "난 그 맘을 좀 봐야겠어",
    "Narcissistic my god I love it",
    "서로를 비춘 밤",
    "아름다운 까만 눈빛 더 빠져 깊이",
    "넌 내게로 난 네게로",
    "숨 참고 love dive",
    "Woo lalalalalalala",
    "Woo 어서 와서 love dive",
    "Woo oh perfect sacrifice yeah",
    "숨 참고 love dive",
    "마음은 이렇게 알다가도 모르지",
    "사랑이라는 건 한순간에 필 테니",
    "직접 들어와 두 눈으로 확인해",
    "내 맘 가장 깊은 데로 오면 돼",
    "Woo 망설일 시간은",
    "Woo 3초면 되는 걸",
    "Woo yeah It's so bad It's good",
    "원하면 감히 뛰어들어",
    "Narcissistic my god I love it",
    "서로를 비춘 밤",
    "아름다운 까만 눈빛 더 빠져 깊이",
    "넌 내게로 난 네게로",
    "숨 참고 love dive",
    "Woo lalalalalalala",
    "Woo 어서 와서 love dive",
    "Woo oh perfect sacrifice yeah",
    "숨 참고 love dive",
    "숨 참고 love dive",
    "숨 참고 love dive",
    "숨 참고 love dive",
    "숨 참고 love dive",
    "Woo lalalalalalala",
    "Woo 어서 와서 love dive",
    "Woo oh perfect sacrifice yeah",
]


voca = list(set(w for doc in docs for w in doc.split()))
voca.sort()
 
n = len(docs)  # 문서 개수

def tf(t, d):
    return d.count(t)
 
def df(t):
    df = 0
    for doc in docs:
        df += t in doc
    return log(n/df+1)
 
def idf(t):
    return log(n/(df(t)+1))
 
def tf_idf(t, d):
    return tf(t, d) * idf(t)

result = []
print()

# TF
tf_list = [[tf(voca[j], docs[i]) for j in range(len(voca))] for i in range(n)]
tf_res = pd.DataFrame(tf_list, columns=voca)
#print(tf_res)
 
# IDF
idf_list = [idf(voca[j]) for j in range(len(voca))]
idf_res = pd.DataFrame(idf_list, index=voca, columns=["IDF"])
 
# TF-IDF
tf_idf_list = [[tf_idf(voca[j], docs[i]) for j in range(len(voca))] for i in range(n)]
tfidf_res = pd.DataFrame(tf_idf_list, columns=voca)
#print(tf_idf_list)

sys.stdout = open('test2.csv', 'w')

print(docs)
print(tf_list)

sys.stdout.close()