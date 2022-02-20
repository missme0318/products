#寫二維清單
products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入價格：')
	# p = []
	# p.append(name)
	# p.append(price)
	# products.append(p)
	products.append([name, price])
print(products)


#讀二維清單
# products[大清單][小清單]
products[0][0] 	# = 第一個商品
products[0][1] 	# = 第一個價格