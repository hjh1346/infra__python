
'''
   여러분의 이름과 주소 좋아하는 음식 2가지를 작성해서 챗팅창에 올려보세요
   json, xml, yaml ...
    
    json은 javascript 객체 표기법을 따르는 문서 형식이다.
    {
    "name" : "김유진",
    "addr" : "김포시",
    "foods" : ["삼겹살", "마라탕"]
    }

'''

#info는 str type 이긴한데 문자열이 특별한 형식(json)을 띄고 있다.
import json


info = '''{
    "name" : "김유진",
    "addr" : "김포시",
    "foods" : ["삼겹살", "마라탕"]
}'''

result = json.loads(info)

print(result["addr"])
print(result["name"])
print(result["foods"])
print(result["foods"][0])
print(result["foods"][1])

#dict에 저장된 데이터를 json 문자열로 변환
result2 = json.dumps(result)




print("종료됨")