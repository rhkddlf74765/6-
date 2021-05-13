#1
num_list1 = list(map(int,input("첫 번째 리스트 값을 콤마로 구분하여 입력하시오:").split(',')))
num_list2 = list(map(int,input("두 번째 리스트 값을 콤마로 구분하여 입력하시오:").split(',')))

print("리스트 변환",num_list1,num_list2,sep='\n')

list_sum = [x+y for x,y in zip(num_list1,num_list2)]
list_mul = [x*y for x,y in zip(num_list1,num_list2)]

print("리스트 합",list_sum, sep='\n')
print("리스트 곱",list_mul, sep='\n')

#2
str_list = list(map(str,input("문자를 콤마로 구분하여 입력하시오:").split(',')))
print("리스트 변환",str_list,sep='\n')
str_list.sort()
print("정렬",str_list,sep='\n')