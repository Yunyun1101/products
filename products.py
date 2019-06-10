import os # operating system
# products = []

#檢查檔案是否有, 若有讀取檔案
def read_file(filename):
	products = []
	if os.path.isfile(filename): #找相對路徑,同樣的資料夾是否有檔案
		print('yeah! 找到檔案了！')
		with open(filename,'r',encoding='utf-16') as f:
			for line in f:
				if '商品,價格' in line:
					continue # 繼續
				name , price = line.strip().split(',') #strip 去除換行＆前後空格, split 切割前後字串
				products.append([name, price])
	else:
		print('找不到檔案....')
	return products

# 讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱：')
		if name == 'q': #quit
			break
		price = input('請輸入商品價格：')
		price = int(price)
		products.append([name, price])
	return products

# 印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-16') as f: #with來自動關閉, utf-8 or utf-16修正中文亂碼問題
		f.write('商品'+ ','+ '價格'+ '\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

products = read_file('products.csv')
products = user_input(products)
print_products(products)
write_file('products.csv',products)
