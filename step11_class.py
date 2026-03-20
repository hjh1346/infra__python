'''
    1. 클래스는 객체를 생성할 수 있는 설계도 역할
    2. DATA TYPE의 역할
    객체는 속성(저장소)와 기능(함수)로 이루어 진다.

'''

class Car:

    def drive(self):
        print("달려요!")

if __name__ == "__main__":
  c1: Car=Car()
  c1.drive()

  c2: Car=Car()
  c3: Car=Car()

