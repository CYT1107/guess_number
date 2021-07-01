#產生隨機整數1~100
import random
r = random.randint(1 , 100)
print(r)
#重複猜數字
while True:
    i = input('請輸入數字（1-100）：')
    i = int(i)
    if i == r:#猜對說猜對
        print('你猜對了！')
        break
    elif i < r:#猜錯給提示
        print('你猜錯了！比這個數字大')
    elif i > r:
        print('你猜錯了！比這個數字小')