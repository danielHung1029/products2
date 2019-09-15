products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	p = []
	p.append(name)
	p.append(price) #上三行可直接寫成p = [name, price]
	products.append(p) #上三行可直接寫成products.append([name, price])
print(products)

#products[0][0] #第0格大清單中的第0格小清單

for p in products:
	print(p[0], '的價格是', p[1])

# 'abc' + '123' = 'abc123' 字串可+

with open ('products.csv', 'w') as f: #當資料中有多種不同屬性之變數，可用exl打開
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') # +逗號是為了讓不同屬性可隔成兩格
