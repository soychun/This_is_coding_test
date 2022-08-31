# list에서 요소 개수 세기
x = [1,2,3,4,5,5]
print(x.count(5))
# output : 2

# list에서 중복 제거하기
x = [1,2,3,4,5,5]
x_list = list(set(sorted(x)))
# output : [1, 2, 3, 4, 5]