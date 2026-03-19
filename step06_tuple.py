# 3개의 str type 데이터를 tuple에 순서대로 담고
# 그 객체의 참조값을 tuple type tuple1 이라는 변수에 담기
tuple1 = ("one", "two", "three")

result1= tuple1[0]
result2= tuple1[1]
result3= tuple1[2]


tuple2=("김구라",)

tuple3 = 10, 20, 30

a, b, c = tuple3

first="girl"
second="boy"
'''
tmp=first
first=second
first=tmp
'''
first, second = second, first




print("종료합니다")