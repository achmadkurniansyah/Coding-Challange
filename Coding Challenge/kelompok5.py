import math

class PaginationHelper:
	def __init__(self, list, page):
			self.list = list
			self.page = page

    #menentukan jumlah item
	def item_count(self): 
			return len(self.list)
	
    #menentukan jumlah halaman
	def page_count(self): 
			return int(math.ceil(self.item_count() / self.page))			
	
    #menentukan jumlah item di setiap halaman
	def page_item_count(self,page_index): 
			if (page_index+1) * self.page <= self.item_count():
					return self.page
			if page_index*self.page<self.item_count() and (page_index+1) * self.page > self.item_count():
					return math.floor(self.item_count()%self.page)
			return -1

    #menentukan item tsb ada di index halaman berapa
	def page_index(self,item_index): 
			if item_index < self.item_count() and item_index >= 0 :
					return math.floor(item_index/self.page)
			return -1
	

helper = PaginationHelper(['a','b','c','d','e','f'],4)
print (helper.page_count())
print (helper.item_count())
print (helper.page_item_count(0)) 
print (helper.page_item_count(1)) 
print (helper.page_item_count(2))
print (helper.page_index(5))
print (helper.page_index(2))
print (helper.page_index(20))
print (helper.page_index(-10))
