global index
index = 0
    
def up():
    global index
    if index == 0:
        index = 3
    else:
        index -= 1
    print(index)

for j in range(3):
    up()