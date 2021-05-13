#리스트란?
"""
scores= [ ]

for i in range(9):
    scores.append(int(input("성적을 입력하시오")))
print(scores)
"""

# 리스트 요소에 인덱스 범위를 확인하고 값을 저장하는 코드
"""
scores = [1,2,3,4,5,6]
if i >= 0 and i < len(scores) :
    scores[i] = number    
"""

scores = [1,2,3,4,5,6,7,8,9]
for i in range(len(scores)):
    print(i,scores[i])
    
    
    scores[i] = i*10
print(scores)