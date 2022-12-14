from collections import Counter
from numpy import indices
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# 리스트 내 수 구하기
#db = [1,1,1,1,2,2,2,3,4,5]
db = ["경복궁", "경복궁","경복궁","경복궁", "궁", "궁", "궁", "종묘", "종묘", "보신사"]

search = input()
print(db.count(search))

# 최빈값 구하기
count_items = Counter(db)
print(count_items)

max_item = count_items.most_common(n=1)
print(max_item[0][0])