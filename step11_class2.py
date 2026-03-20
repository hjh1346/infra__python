

class mycar:
  
  def __init__(self, name:str):
    print("생성자가 호출됨")
    print(self)
    self.name=name

  def drive(self):
    print(f"{self.name}이(가) 달려요~")


if __name__ == "__main__":
  c1: mycar=mycar("쏘나타")
  c2: mycar=mycar("아반떼")
  c1.drive()
  c2.drive()