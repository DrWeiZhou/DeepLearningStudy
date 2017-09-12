list = ['aaa', 'bbb', 'ccc', 'ddd']
print(list)

list[0] = 'haha'
print(list)

list.append('eee')
list.insert(0,'hehe')
print(list)
for one in list:
    # list.pop()
    print("sorry:"+one)
print(list)
del list[0]
print(list)

squares = []
for num in range(1,11):
    square = num ** 2
    squares.append(square)
print(squares)

print( [square1** 2 for square1 in range(1,11)])