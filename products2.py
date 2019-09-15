products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	price = int(price)
	p = []
	p.append(name)
	p.append(price) #上三行可直接寫成p = [name, price]
	products.append(p) #上三行可直接寫成products.append([name, price])
print(products)

#products[0][0] #第0格大清單中的第0格小清單

for p in products:
	print(p[0], '的價格是', p[1])

# 'abc' + '123' = 'abc123' 字串可+

with open ('products2.csv', 'w', encoding = 'utf-8') as f: #當資料中有多種不同屬性之變數，可用exl打開
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') # +逗號是為了讓不同屬性可隔成兩格
#使用exl打開檔案仍會有亂碼產生的情況，這是因為exl讀取模式並未使用UTF-8編碼
