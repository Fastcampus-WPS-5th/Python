def return_list(value, result=None):
    if result == None:
        result = []
    print('input value: {}, result id: {}'.format(value, id(result)))
    result.append(value)
    return result


# 기존에 result에 전달할 리스트 변수가 있던 경우
l = ['apple']
new_l = return_list('banana', l)
print(new_l)

new_l2 = return_list('melon', new_l)
print(new_l2)

# return_list함수에 result매개변수로 사용할 list변수를 전달하지 않은 경우
l2 = return_list('민아')
print(l2)

l3 = return_list('혜리')
print(l3)

