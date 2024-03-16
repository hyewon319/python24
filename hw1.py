'''def show_circle_area_1(radius) :
    msg = '반지름이 1인 원의 넓이는 3.14' 
    return msg


input_radius = input('구하고자하는 원의 반지름은? ')
result = show_circle_area_1(input_radius)
print(result)
'''

def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(please):
    please = '반지름이 10인 원의 넓이 = 3.14 x 10 x10 = 314 '
    return please

input_prompt = input('넓이를 구하고자 하는 원의 반지름은? ')
input_please = input('반지름이 10인 원의 넓이 = 3.14 * 10 * 10 = 314')
result = get_circle_area(input_please)
print(result)


