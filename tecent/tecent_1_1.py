n=int(input())
if n > 1:
    f=list(map(int, input().split(' ')))
else:
    f=[int(input())]
# n = 4
# f = [0, 20, 50, 1000]

idx = 0

def get_cost(val):
    if val < 100:
        return 50
    else:
        return 100

cur_cost = 0
for _val in f:
    idx += 1
    count = idx
    # 第一种方式
    if _val < 1000:
        cost_1 = count * 20
        cost_2 = get_cost(_val)
        new_cost = min(cost_1, cost_2)
        print(new_cost-cur_cost)
        cur_cost = new_cost
    else:
        print(20)
    # idx += 1