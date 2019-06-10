products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q': #quit
		break
	price = input('請輸入商品價格：')
	price = int(price)
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價格是', p[1])

#'abc'+'123'='abc123'
#'abc'*3 ='abcabcabc'

with open('products.csv', 'w', encoding='utf-16') as f: #with來自動關閉, utf-8 or utf-16修正中文亂碼問題
	f.write('商品'+ ','+ '價格'+ '\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')

