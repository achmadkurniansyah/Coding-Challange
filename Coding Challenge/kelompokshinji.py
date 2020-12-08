import math

class PaginationHelper():
    def __init__(self, list, page):
        self.array = list
        self.halaman = page
        global itemlist
        global pages
        itemlist = []   
        pages = []
        for i in self.array:
            pages.append(i)
            if len(pages) >= self.halaman:
                itemlist.append(pages)
                pages = []
        itemlist.append(pages)
        for i in itemlist:
            if len(i) == 0:
                itemlist.remove(i)

    def page_count(self):
        return print(math.ceil(len(self.array)/self.halaman))

    def item_count(self):
        return print(len(self.array))

    def page_item_count(self, a):
        if a+1 > len(itemlist):
            return print(-1)
        else:
            return print(len(itemlist[a]))

    def page_index(self, indexes):
        if indexes < 0:
            return print(-1)
        elif indexes >= len(self.array):
            return print(-1)
        else:
            for i in range(len(itemlist)):
                for j in range(len(itemlist[i])):
                    if itemlist[i][j] == self.array[indexes]:
                        return print(i)
        

helper = PaginationHelper(['a','b','c','d','e','f'],4)
helper.page_count()
helper.item_count()
helper.page_item_count(0)
helper.page_item_count(1)
helper.page_item_count(2)
helper.page_index(5) 
helper.page_index(2) 
helper.page_index(20) 
helper.page_index(-10) 
