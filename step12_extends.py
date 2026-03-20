
# 클래스 상속에 대해서 알아보자

class phone:
    def call(self):
        print("전화를 걸어요!")
class handphone(phone): #클래스명(상속받을 클래스)
   def mobile_call(self):
      print("이동중에 전화를 걸어요!")
   def take_picture(self):
      print("100만 화소의 사진을 찍어요!")

class SmartPhone(handphone):
   
    def do_internet(self):
        print("인터냇을 해요!")


    # 부모 클래스(HandPhone)의 사진 찍는 기능을 재정의(Overriding)
    def take_picture(self):
        print("1000 만 화소의 사진을 찍어요!")


if __name__ == "__main__":
  p1:phone=phone()
  p1.call()

  print("--------------")

  p2:handphone=handphone()
  p2.call()
  p2.mobile_call()
  p2.take_picture()

if __name__ == "__main__" :
    p1:phone = phone()
    p1.call()


    print("-------------------")


    p3:handphone = handphone()
    p3.call()
    p3.mobile_call()
    p3.take_picture()
