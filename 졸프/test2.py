from collections import Counter
from numpy import indices
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import sys

tfidf = TfidfVectorizer(stop_words='english')

df1 = pd.read_csv("C:/Users/장준하/Desktop/데이터분류/real dataset1(목적지).csv")
df2 = pd.read_csv("C:/Users/장준하/Desktop/데이터분류/real dataset2(분류).csv")
df3 = pd.read_csv("C:/Users/장준하/Desktop/데이터분류/real dataset3(시).csv")
df4 = pd.read_csv("C:/Users/장준하/Desktop/데이터분류/real dataset4(구).csv")
df5 = pd.read_csv("C:/Users/장준하/Desktop/데이터분류/real dataset5(로).csv")
df6 = pd.read_csv("C:/Users/장준하/Desktop/데이터분류/real dataset6(길).csv")
df7 = pd.read_csv("C:/Users/장준하/Desktop/데이터분류/real dataset7(대중교통).csv")
df8 = pd.read_csv("C:/Users/장준하/Desktop/데이터분류/real dataset8(행사).csv")
df9 = pd.read_csv("C:/Users/장준하/Desktop/데이터분류/real dataset9(내용).csv")

tfidf_matrix1 = tfidf.fit_transform(df1['destination'])
tfidf_matrix2 = tfidf.fit_transform(df2['classification'])
tfidf_matrix3 = tfidf.fit_transform(df3['city'])
tfidf_matrix4 = tfidf.fit_transform(df4['twon'])
tfidf_matrix5 = tfidf.fit_transform(df5['ro'])
tfidf_matrix6 = tfidf.fit_transform(df6['road'])
tfidf_matrix7 = tfidf.fit_transform(df7['publictransport'])
tfidf_matrix8 = tfidf.fit_transform(df8['event'])
tfidf_matrix9 = tfidf.fit_transform(df9['content'])

sys.stdout = open('확인용3.txt', 'w')

#print(tfidf_matrix1.shape, tfidf_matrix2.shape, tfidf_matrix3.shape, tfidf_matrix4.shape, tfidf_matrix5.shape, tfidf_matrix6.shape, tfidf_matrix7.shape, tfidf_matrix8.shape, tfidf_matrix9.shape)

cosine_sim1 = linear_kernel(tfidf_matrix1, tfidf_matrix1)
cosine_sim2 = linear_kernel(tfidf_matrix2, tfidf_matrix2)
cosine_sim3 = linear_kernel(tfidf_matrix3, tfidf_matrix3)
cosine_sim4 = linear_kernel(tfidf_matrix4, tfidf_matrix4)
cosine_sim5 = linear_kernel(tfidf_matrix5, tfidf_matrix5)
cosine_sim6 = linear_kernel(tfidf_matrix6, tfidf_matrix6)
cosine_sim7 = linear_kernel(tfidf_matrix7, tfidf_matrix7)
cosine_sim8 = linear_kernel(tfidf_matrix8, tfidf_matrix8)
cosine_sim9 = linear_kernel(tfidf_matrix9, tfidf_matrix9)

#print(cosine_sim1, cosine_sim2, cosine_sim3, cosine_sim4, cosine_sim5, cosine_sim6, cosine_sim7, cosine_sim8)

indices1 = pd.Series(df1.index, index=df1['destination']).drop_duplicates()
indices2 = pd.Series(df2.index, index=df2['classification']).drop_duplicates()
indices3 = pd.Series(df3.index, index=df3['city']).drop_duplicates()
indices4 = pd.Series(df4.index, index=df4['twon']).drop_duplicates()
indices5 = pd.Series(df5.index, index=df5['ro']).drop_duplicates()
indices6 = pd.Series(df6.index, index=df6['road']).drop_duplicates()
indices7 = pd.Series(df7.index, index=df7['publictransport']).drop_duplicates()
indices8 = pd.Series(df8.index, index=df8['event']).drop_duplicates()
indices9 = pd.Series(df9.index, index=df9['content']).drop_duplicates()

#print(indices1, indices2, indices3, indices4, indices5, indices6, indices7, indices8, indices9)

print("여까지")

def get_recommendations1(destination, cosine_sim1=cosine_sim1):
    idx1 = indices[destination]
    sim_scores1 = list(enumerate(cosine_sim1[idx1]))
    sim_scores1 = sorted(sim_scores1, key=lambda x: x[1], reverse=True)
    sim_scores1 = sim_scores1[:1]
    destination_indices = [a[0] for a in sim_scores1]
    return df1[["destination"].iloc[destination_indices]]

def get_recommendations(classification, cosine_sim2=cosine_sim2):
    idx2 = indices[classification]
    sim_scores2 = list(enumerate(cosine_sim2[idx2]))
    sim_scores2 = sorted(sim_scores2, key=lambda x: x[1], reverse=True)
    sim_scores2 = sim_scores2[:1]
    classification_indices = [b[0] for b in sim_scores2]
    return df2[["classification"].iloc[classification_indices]]

def get_recommendations(city, cosine_sim3=cosine_sim3):
    idx3 = indices[city]
    sim_scores3 = list(enumerate(cosine_sim3[idx3]))
    sim_scores3 = sorted(sim_scores3, key=lambda x: x[1], reverse=True)
    sim_scores3 = sim_scores3[:1]
    city_indices = [c[0] for c in sim_scores3]
    return df3[["city"].iloc[city_indices]]

def get_recommendations(twon, cosine_sim4=cosine_sim4):
    idx4 = indices[twon]
    sim_scores4 = list(enumerate(cosine_sim4[idx4]))
    sim_scores4 = sorted(sim_scores4, key=lambda x: x[1], reverse=True)
    sim_scores4 = sim_scores4[:1]
    twon_indices = [d[0] for d in sim_scores4]
    return df4[["twon"].iloc[twon_indices]]

def get_recommendations(ro, cosine_sim5=cosine_sim5):
    idx5 = indices[ro]
    sim_scores5 = list(enumerate(cosine_sim5[idx5]))
    sim_scores5 = sorted(sim_scores5, key=lambda x: x[1], reverse=True)
    sim_scores5 = sim_scores5[:1]
    ro_indices = [e[0] for e in sim_scores5]
    return df5[["ro"].iloc[ro_indices]]

def get_recommendations(road, cosine_sim6=cosine_sim6):
    idx6 = indices[road]
    sim_scores6 = list(enumerate(cosine_sim6[idx6]))
    sim_scores6 = sorted(sim_scores6, key=lambda x: x[1], reverse=True)
    sim_scores6 = sim_scores6[:1]
    road_indices = [f[0] for f in sim_scores6]
    return df6[["road"].iloc[road_indices]]

def get_recommendations(publictransport, cosine_sim7=cosine_sim7):
    idx7 = indices[publictransport]
    sim_scores7 = list(enumerate(cosine_sim7[idx7]))
    sim_scores7 = sorted(sim_scores7, key=lambda x: x[1], reverse=True)
    sim_scores7 = sim_scores7[:1]
    publictransport_indices = [g[0] for g in sim_scores7]
    return df7[["publictransport"].iloc[publictransport_indices]]

def get_recommendations(event, cosine_sim8=cosine_sim8):
    idx8 = indices[event]
    sim_scores8 = list(enumerate(cosine_sim8[idx8]))
    sim_scores8 = sorted(sim_scores8, key=lambda x: x[1], reverse=True)
    sim_scores8 = sim_scores8[:1]
    event_indices = [h[0] for h in sim_scores8]
    return df8[["event"].iloc[event_indices]]

def get_recommendations(content, cosine_sim9=cosine_sim9):
    idx9 = indices[content]
    sim_scores9 = list(enumerate(cosine_sim9[idx9]))
    sim_scores9 = sorted(sim_scores9, key=lambda x: x[1], reverse=True)
    sim_scores9 = sim_scores9[:1]
    content_indices = [i[0] for i in sim_scores9]
    return df9[["content"].iloc[content_indices]]

print(get_recommendations1(input))

sys.stdout.close()