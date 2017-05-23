'''
상위폴더에 우클릭 -> Mark Directory As... -> Sources Root
'''
from class_sample import Shop

lotteria = Shop('롯데리아', '패스트푸드점', '신사역')
lotteria.shop_info()

lotteria.shop_type = '학원'
print(lotteria.shop_type)
lotteria.shop_info()