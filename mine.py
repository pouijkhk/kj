try:
	x1 = int(input("أدخل العدد الأول:"))
	x2 = int(input("أدخل العدد الثاني:"))
	print("1-جمع")
	print("2-طرح")
	print("3-ضرب")
	print("4-قسمة")
	x3 = int(input("أختر:"))
	if x3 == 1:
		print(x1, " + ", x2, " = ", x1 + x2)
	elif x3 == 2:
		print(x1, " - ", x2, " = ", x1 - x2)
	elif x3 == 3:
		print(x1, " × ", x2, " = ", x1 * x2)
	elif x3 == 4:
		print(x1, " ÷ ", x2, " = ", x1 / x2)
	else:
		print(x1 ** x2)

except:
	print("HA")
