#讀取檔案＋跳過標題讀取
def read_file(filname):
	products = []
	with open(filname, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

#讓使用者輸入
def user_input(products):
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
	return products


#讀二維清單
# products[大清單][小清單]
# products[0][0] 	# = 第一個商品
# products[0][1] 	# = 第一個價格

#印出輸入清單
def print_prodeuct(products):
	for product in products:
		print(product[0], '價格是：', product[1], '元')

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for product in products:
			f.write(product[0] + ',' + str(product[1]) + '\n')

def main():
	import os
	if os.path.isfile('products.py'):
		print('yeah~找到檔案囉～')
		products = read_file('products.csv')
	else:
		print('找不到的檔案')
	products = user_input(products)
	print_prodeuct(products)
	write_file('products.csv', products)

main() #程式進入點

# refactor重構程式 = 用function將結構整理好的專用術語