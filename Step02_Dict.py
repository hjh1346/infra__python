mem1={"num":1, "name":"kimgura", "isman":True}
print(mem1["num"])
print(mem1["name"])
print(mem1["isman"])

a=mem1["num"]
b=mem1["name"]
c=mem1["isman"]
 
mem1["num"] = 2
mem1["name"] = "kimyujin"
mem1["isman"] = False
del mem1["isman"]

mem1.clear()


mem2 = {"num":3, "name":"kimyujin", "isman":False}

print("종료됩니다")
