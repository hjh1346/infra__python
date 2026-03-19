from unittest import result


def test1():
    print("test1() 호출됨")

test1()
result1 = test1()

def test2(arg):
    print("전달 받은 내용:",arg)
    print(f"전달 받은 내용:{arg}")

test2(None)
test2(10)
test2("kim")

def print_sum(num1:int, num2:int):
    sum = num1+num2
    print(f"{num1}+{num2}={sum}")

print_sum(10,20)
print_sum(30,40)

def print_info(name: str, addr: str):
    print(f"이름은 {name} 이고 주소는 {addr}")

print_info("김구라", "노량진")
print_info(addr="행신동", name="해골")

def get_sum(num1:int, num2: int):
    sum=num1+num2
    return sum

result2 = get_sum(10, 20)
print(result2)




print("종료 됩니다")
