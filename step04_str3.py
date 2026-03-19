
# 검색 혹은 ai의 도움을 받아서 info에 들어 있는 문자열을 dict type으로 바꾸세요
# 그런 다음 dict에 들어 있는 내용을 확인 후 다시 dict에 있는 내용을 이용해서 yaml 문자열 형식으로 변환해보세요.

import yaml


info = '''
name: 김유진
addr: 김포시
foods:
  - 삼겹살
  - 마라탕
isMan: false
body:
  weight: 60
  height: 160
'''

result = yaml.safe_load(info)

print(result)


result2= yaml.dump(result, allow_unicode=True, sort_keys=False)


print(result2)









