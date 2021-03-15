# lru design
# @param operators int整型二维数组 the ops
# @param k int整型 the k
# @return int整型一维数组
#
class Solution:
    # 字典存储键值对；列表实现值常用性更新
    dict_lru = {}
    list_lru = []

    def set(self, key, val, k):
        self.dict_lru[key] = val
        self.list_lru.append(key)
        if len(self.list_lru) > k:
            del self.dict_lru[self.list_lru[0]]
            del self.list_lru[0]

    def get(self, key):
        if key in self.dict_lru:
            self.list_lru.remove(key)
            self.list_lru.append(key)
            return self.dict_lru[key]
        return -1

    def LRU(self, operators, k):
        ret = []
        SET = 1
        GET = 2

        for items in operators:
            if items[0] == SET:
                self.set(str(items[1]), items[2], k)

            elif items[0] == GET:
                ret.append(self.get(str(items[1])))

        return ret


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.LRU([[1, 1, 1], [1, 2, 2], [1, 3, 2], [2, 1], [1, 4, 4], [2, 2]], 3)
    )
