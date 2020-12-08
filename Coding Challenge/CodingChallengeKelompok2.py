import math
class PaginationHelper:
    def __init__(self, lists, page):
        self.lists = lists
        self.page = page
    
    def createPage(self):
        tempElement = self.lists.copy()
        elementLength = len(tempElement)
        pageDict = {}
        for i in range(math.ceil(elementLength/self.page)):
            temp = []
            for j in tempElement:
                if len(temp) == self.page:
                    break
                else:
                    temp.append(j)
            for k in range(len(temp)):
                tempElement.pop(0)
            pageDict[i] = temp
        return pageDict

    def page_count(self):
        temp = self.createPage()
        return len(temp)

    def item_count(self):
        return len(self.lists) 

    def page_item_count(self,pages):
        temp = self.createPage()
        if pages < 0:
            return -1
        elif temp.get(pages) == None:
            return -1
        else:
            return len(temp.get(pages))
    def page_index(self,x):
        if x>(len(self.lists)) or x<=0 :
            return -1
        a = math.floor((x-1)/self.page)
        return a

helper = PaginationHelper(['a','b','c','d','e','f','g','g','h'],4)

print(helper.page_count())
print(helper.item_count())
print(helper.page_item_count(0))
print(helper.page_item_count(1))
print(helper.page_item_count(2))
print("#########################")
print(helper.page_index(5))
print(helper.page_index(2))
print(helper.page_index(20))
print(helper.page_index(-10))
print(helper.page_index(9))

