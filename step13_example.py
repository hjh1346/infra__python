from jinja2 import Template


info:dict={
    "num":1,
    "name":"김구라",
    "body":{
        "height":180,
        "weight":80
    },
    "hobby":["피아노", "당구", "프로그래밍"]
}

'''
   위에 info 안에 들어 있는 데이터를 이용해서 아래와 같은 형식의 문자열을 출력해 보세요
   
   번호:1
   이름:김구라
   키:180cm
   몸무게:80kg
   취미:피아노 당구 프로그래밍

'''

template_str = '''
   번호: {{ info.num }}
   이름: {{ info.name }}
   키: {{ info.body.height }} cm
   몸무게: {{ info.body.weight }} kg
   취미 :

     {% for h in info.hobby %}
     - {{ h }}
     {% endfor %}
'''


# 템플릿 생성
template = Template(template_str)

# 렌더링 (데이터 넣기)
result = template.render(info=info)

# 출력
print(result)