import math
class PaginationHelper :
    def __init__(self, list, page):
            self.list = list
            self.page = page


    def item_count(self): #hitung total list
            return len(self.list)
    
    def page_count(self): #hitung total halaman dr banyaknya list, 1 halaman utk 4 list
		    return int(math.ceil(self.item_count() / self.page))

    def page_item_count(self,item): #hitung hal ke i ada brp list
		    if (item+1) * self.page <= self.item_count():
		            return self.page
		    if item*self.page<self.item_count() and (item+1) * self.page > self.item_count():
			        return self.item_count()%self.page
		    return -1

    def page_index(self,index): #hitung list ke-i ada di halaman berapa, start dr 0
		    if index < self.item_count() and index >= 0 :
			        return int(index/self.page)
		    return -1
	

helper = PaginationHelper(['a','b','c','d','e','f'], 4) # 6 list, 1 halaman memuat 4 list

print (helper.page_count()) # 2 halaman yg memuat 6 list (hal1= 4, hal2= 2)
print (helper.item_count()) # total list ada 6
print (helper.page_item_count(0)) # halaman ke 1 (start from 0) memuat 4 list
print (helper.page_item_count(1)) # halaman ke 2 memuat 2 list
print (helper.page_item_count(2)) # halaman ke 3 tidak ada list, return -1

print (helper.page_index(5)) #list ke 5 ada di halaman 2 (start from 0)
print (helper.page_index(2)) #list ke 2 ada di halaman 1
print (helper.page_index(20)) #list ke 20 (tidak ada), return -1
print (helper.page_index(-10)) #list negative : invalid
