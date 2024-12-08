class Item:
    def __init__(self, name, size, points):
        self.name = name
        self.size = size
        self.points = points


def knapsack(items, capacity): #Функция динамически считает наибольшее значение очков
    n = len(items)

    DP = [[0] * (capacity) for _ in range(n)]

    for i in range(n):
        item=items[i]
        size=item.size
        point=item.points
        for j in range(capacity):
            if size<=j+1 and i==0:
                DP[i][j]=point
            elif size<j+1:
                past=point+DP[i-1][j-size]
                pres=DP[i-1][j]
                DP[i][j]=max(past,pres)
            elif size==j+1:
                past = point
                pres = DP[i - 1][j]
                DP[i][j] = max(past, pres)
    mx = 0
    for i in range(len(DP)):
        local_mx = (max(DP[i]))
        if local_mx > mx:
            mx = local_mx
            list_ind = i
            mx_ind = DP[list_ind].index(mx)
    return DP, mx_ind,mx


def get_items(DP,items): # Функция возвращает список предметов
    DP,ind,mx=DP

    n = len(items)-1
    selected_items = []
    for i in range(n, 0, -1):
        if DP[i][ind] != DP[i - 1][ind]:
            selected_items.append(items[i])
            ind -= items[i].size
            if ind < 0:
                break
    return selected_items,mx


inventory = [[0]] * 9
inventory[8]=['i']
items = [Item('r', 3, 25), Item('p', 2, 15),
         Item('a', 2, 15), Item('m', 2, 20),
         Item('i', 1, 5), Item('k', 1, 15),
         Item('x', 3, 20), Item('t', 1, 25),
         Item('f', 1, 15), Item('d', 1, 10),
         Item('s', 2, 20), Item('c', 2, 20)]


items_res,points=get_items(knapsack(items,8),items)
ind=0
points+=5
for i in items_res:
    for j in range(i.size):
        inventory[ind+j]=[i.name]
    ind=ind+j+1


for i in range(0,len(inventory),3):
    print(inventory[i],inventory[i+1],inventory[i+2])
print(points)


for i in items:
    if i not in items_res:
        points-=i.points
print(points)