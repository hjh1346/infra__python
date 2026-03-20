
'''
    html/index.html 외부에 있는 template 파일을 읽어와서
    data를 연결해서 원하는 문자열을 얻어내서
    콘솔창에 출력하는 예제(나중에는 콘솔창이 아니고 클라이언트의 웹브라우저에 출력하게 된다)
'''

from jinja2 import Environment, FileSystemLoader, Template
file_loader=FileSystemLoader("html")
env=Environment(loader=file_loader)
temp:Template=env.get_template("index.html")
notice_data = {
    "title":"오늘의 공지사항",
    "notice":["드디어 불금입니다", "어쩌구...", "저쩌구..."]
}

result:str = temp.render(notice_data)


# 출력하기
print(result)