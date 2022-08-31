opposites = {"NORTH": "SOUTH", "SOUTH": "NORTH",
             "EAST": "WEST", "WEST": "EAST"}

def dirReduc(arr):
    new_list = []
    for i in range(0, len(arr)):
        if len(new_list) == 0:
            new_list.append(arr[i])
        elif new_list[-1] != opposites[arr[i]]:
            new_list.append(arr[i])
        else:
            new_list.pop()
    return new_list


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

# print(dirReduc(a))
