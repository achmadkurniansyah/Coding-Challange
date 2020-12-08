import math


class PaginationHelper:
    def __init__(self, list, page):
        self.list = list
        self.page = page

    def item_count(self):
        return len(self.list)

    def page_count(self):
        return math.ceil(len(self.list) / self.page)

    def page_item_count(self, num):
        page_count = len(self.list[num * self.page: (num * self.page) + self.page])

        if page_count == 0 or page_count < 0 or page_count > len(self.list):
            return -1

        return page_count

    def page_index(self, num):
        if num > len(self.list) - 1 or num < 0:
            return - 1
        return math.floor(num / self.page)


helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)

helper_page_count = helper.page_count()
print(helper_page_count)

helper_item_count = helper.item_count()
print(helper_item_count)

helper_page_item_count_0 = helper.page_item_count(0)
print(helper_page_item_count_0)

helper_page_item_count_1 = helper.page_item_count(1)
print(helper_page_item_count_1)

helper_page_item_count_2 = helper.page_item_count(2)
print(helper_page_item_count_2)

helper_page_index_5 = helper.page_index(5)
print(helper_page_index_5)

helper_page_index_2 = helper.page_index(2)
print(helper_page_index_2)

helper_page_index_20 = helper.page_index(20)
print(helper_page_index_20)

helper_page_index_minus_10 = helper.page_index(-10)
print(helper_page_index_minus_10)
