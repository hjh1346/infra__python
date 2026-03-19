# str type에 대해서 알아보자

#양쪽에 공백이 포함되거나 포함될 가능성이 있는 문자열이 있다고 가정하자
#만일 공백을 제거 하고 싶다면?
text="  cloud infra  "
result1=text.strip()

#.으로 분리하기
myIp= "192.168.0.2"
result2=myIp.split(".")
#join으로 다시 합치기
result3 = ".".join(result2)
#특정 문자열 찾아서 대체하기
result4 = "hello mimi!".replace("mi", "ma")

result5 = "python".upper()
result6 = "PYTHON".lower()

# 등등 여러가지 기능들이 제공된다.

print("제거합니다")
