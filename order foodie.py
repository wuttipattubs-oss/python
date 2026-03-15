food=[]

food_add=input("please order your food number one:")

food.append(food_add)

food_add=input("please order your food number two:")

food.append(food_add)

food_add=input("please order your food number three:")

food.append(food_add)

print("do you want to order more")

ask=input("Yes or No").lower()

if ask =="yes":
    food_add=input("please order your number four food:")
    food.append(food_add)
    print("your order are",food[0],",",food[1],",",food[2],"and",food[3])
else:
    print("your order are",",",food[0],",",food[1],"and",food[2])

