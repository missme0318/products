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
	# 上面四行可以用下面這行替代
	products.append([name, price])
print(products)


#讀二維清單
# products[大清單][小清單]
products[0][0] 	# = 第一個商品
products[0][1] 	# = 第一個價格


for product in products:
	print(product[0], '價格是：', product[1], '元')