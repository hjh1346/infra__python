nums=[10, 20, 30, 40, 50]
names=["kim", "park", "jo", "oh", "choi"]
for item in nums:
    print(item)

for item in names:
    print("names를 순서대로 출력중...")
    print(item)


r1 = range(5)
r2 = range(10)
print(r1)
print(r2)

for item in range(5):
    print(item)

result2=range(len(names))

for i in range(len(names)):
    print("list의 index와 함께 출력합니다")
    print(i, names[i])
    


print("종료 합니다")