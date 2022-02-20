# os = operating system 作業系統
import os


productss = []
# path路徑
# isfile檢查檔案在不在
if os.path.isfile('products.csv'):
	print('找到檔案了')
	
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			productss.append([name, price])
	print(productss)
else:
	print('檔案不存在！')