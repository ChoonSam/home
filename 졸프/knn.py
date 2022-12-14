import random
from tkinter import X, Y #데이터 생성을 위해 램덤모듈 사용
import numpy as np
import matplotlib.pyplot as plt

#랜덤으로 데이터 입력(학습)
r = [] #방울토마토 1
b = [] #토마토 0
for i in range(50):
    #크기가 1~10 사이에 있고, 무게가 50~100 사이에 있으면 방울토마토
    r.append([random.randint(1,10),random.randint(50,100),1])
    #크기가 7~20 사이에 있고, 무게가 80~120 사이에 있으면 토마토
    b.append([random.randint(7,20),random.randint(80,120),0])
    
#점x와 점y의 거리 구하는 함수
def distance(x,y):
    return np.sqrt(pow((x[0]-y[0]),2)+pow((x[1]-y[1]),2))

#knn알고리즘
def knn(x,y,k):
    result=[]
    cnt=0
    for i in range(len(y)):
        result.append([distance(x,y[i]),y[i][2]])
    result.sort()
    for i in range(k):
        if(result[i][1]==i):
            cnt+=1
    if(cnt > (k/2)):
        print("이것은 방울토마토")
    else:
        print("이것은 토마토")

size = input("크기>>")
weight = input("무게>>")
num = input("k>>") #K요소
new = [int(size), int(weight)]

knn(new, r+b, int(num))

print(r,b)
rr = np.array(r)
bb = np.array(b)
for i,j in rr[:,:2]:
    plt.plot(i,j,'or')
for i,j in bb[:,:2]:
    plt.plot(i,j,'ob')
plt.plot(int(size), int(weight), 'og')
plt.show()

print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

# 어레이된 정수 어레이 `nums`에서 `target`에 가장 가까운 `k` 요소를 찾는 함수
def findKClosestElements(nums, k, target):
 
    left = 0
    right = len(nums) - 1
 
    while right - left >= k:
        if abs(nums[left] - target) > abs(nums[right] - target):
            left = left + 1
        else:
            right = right - 1
 
    return nums[left:left + k]
 
 
if __name__ == '__main__':
 
    nums = (r,b)
    target = [8,90,1]
    k = 4
 
    print(findKClosestElements(nums, k, target))