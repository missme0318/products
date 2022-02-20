#讓使用者輸入

products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入價格：')
	prince = int(price)
	#寫二維清單
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

#印出輸入清單
for product in products:
	print(product[0], '價格是：', product[1], '元')

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for product in products:
		f.write(product[0] + ',' + str(product[1]) + '\n')

#讀取檔案＋跳過標題讀取
productss = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue
		name, price = line.strip().split(',')
		productss.append([name, price])
print(productss)