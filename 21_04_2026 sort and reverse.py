#โจทย์
#num = [20, 59, 88,2,6,4,10,1,4,2,23,222]
๒อยากให้ทำการ insert 93 ที่ list 5
#ให้ remove222
#append 223
#จากนั้น sort และแสดงค่า ปัจจุบันออกมา
#ถ้า แสดงออกแล้วไม่เจอค่า 111 ให้ #append เข้าไป แล้วเช็คค่าออกมา
#จากนั้น reverse  และ เช็คค่า

num=[20,59, 88,2,6,4,10,1,4,2,23,222]
num.insert(5,93)
num.remove(222)
num.append(223)
num.sort()
print(num)
num.append(111)
num.reverse()
print(num)
