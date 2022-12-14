from numpy import indices
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

#df1 = pd.read_csv("C:/Users/장준하/Desktop/tdmb/tmdb_5000_credits.csv")
#df2 = pd.read_csv("C:/Users/장준하/Desktop/tdmb/tmdb_5000_movies.csv")
#Location = "C:/Users/장준하/Desktop"
#df2 = "real dataset.csv"

df2 = pd.read_csv("C:/Users/장준하/Desktop/real dataset.csv")

tfidf = TfidfVectorizer(stop_words='english')

#df2['overview'] = df2['overview'].fillna('')

tfidf_matrix = tfidf.fit_transform(df2['content(nouns)'])

#data_pd = pd.read_csv("{}/{}".format(Location, df2), header=None, index_col=None, names=None)
#indices = pd.DataFrame.to_numpy(data_pd)

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

#indices = pd.Series(df2.index, index=df2[['destination'] ["classification"] ["city"]]).drop_duplicates()
#indices = df2.iloc[[0,1,2]]

indices = pd.read_csv("C:/Users/장준하/Desktop/real dataset.csv", usecols=[0,1,2])

print(indices)

# 영화의 제목을 입력받으면 코사인 유사도를 통해서 가장 유사도가 높은 상위 10개의 영화 목록 반환
def get_recommendations(destination, classification, city, cosine_sim=cosine_sim):
    # 영화 제목을 통해서 전체 데이터 기준 그 영화의 index 값을 얻기
    idx = indices[destination, classification, city]
    
    # 코사인 유사도 매트릭스 (cosine_sim) 에서 idx 에 해당하는 데이터를 (idx, 유사도) 형태로 얻기
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # 코사인 유사도 기준으로 내림차순 정렬
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # 자기 자신을 제외한 10개의 추천 영화를 슬라이싱
    sim_scores = sim_scores[1:11]
    
    # 추천 영화 목록 10개의 인덱스 정보 추출
    destination_indices = [i[0] for i in sim_scores]
    
    # 인덱스 정보를 통해 영화 제목 추출
    return df2['destination', "classification", "city"].iloc[destination_indices]

print(get_recommendations(input))