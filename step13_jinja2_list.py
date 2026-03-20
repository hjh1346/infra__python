from jinja2 import Template


my_template:str='''
    친구목록
    {% for name in friends %}
    - {{ name }}
    {% endfor %}
'''

temp:Template=Template(my_template)
names=["김구라", "해골", "원숭이"]

result:str=temp.render(friends=names)
print(result)