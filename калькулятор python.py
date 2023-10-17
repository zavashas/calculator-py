num = [1,2,3,4,5,3,3]
num2 = [6,7,8,3,5]
num3 = (4,6,8,3,6)
num4 = (5,47,8,9)
def program1 (num):
    return sum(num)
print(program1(num))

def program2(num):
    return max(num)
print(program2(num))

def program3(num):
    return set(num)
print(program3(num))

def program4(num, num2):
    return num + num2 
print(program4(num, num2))

def program5(num3, element):
    if element in num3:
        return num3.index(element)
    else:
        return "Элемент не найден"
element = 1
print(program5(num3, element))  
element = 3
print(program5(num3, element))  

def program6 (num3,num4):
    return num3 + num4 
print(program5(num3, num4))

def program7(num3, element):
    new_num3 = list(num3)
    new_num3.remove(element)
    return tuple(new_num3)
element = 3
print(program7(num3, element)) 

def program8(num3, element):
    return num3.count(element)
element = 3
print(program8(num3, element))