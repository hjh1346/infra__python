"""
    회원 한명의 정보는 번호, 이름, 주소로 이루어 있다.
    그리고 그러한 회원이 여러명이다.
    여러명의 회원 목록을 하나의 묶음으로(하나의 data)로 관리하고 싶다면...
"""

# 3명의 회원정보를 각각 dict에 담은 다음 그 dict를 list에 담는 코드를 챗팅창에 보내보세요

a1 = {"age":30, "addr":"sucham1", "name":"kimyujin"}
a2 = {"age":31, "addr":"sucham2", "name":"jesun"}
a3 = {"age":26, "addr":"dosari", "name":"yejin"}

a_list = [a1, a2, a3]

a=a_list
b=a_list[0]
c=a_list[0]["age"]
d=a_list[0]["name"]

print("종료 합니다")
