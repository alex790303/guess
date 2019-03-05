#猜數字比大小，會告訴你比答案大或小，即猜中的次數
import random
end = input('請決定隨機數字範圍最大值:')
start = input('請決定隨機數字範圍最小值：')
end = int(end)
start = int(start)

r = random.randint(start, end)
count = 0
while True:
	count += 1 #count = count + 1
	num = input('請輸入數字:')
	num = int(num)
	if num == r:
		print('答案:',r ,'恭喜猜對了!')
		print('你猜了',count ,'次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這次你猜的',count ,'次')	
