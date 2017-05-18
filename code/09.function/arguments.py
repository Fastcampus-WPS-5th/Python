def make_student(name, age, gender, cls='WPS'):
    return {
        'name': name,
        'age': age,
        'gender': gender,
        'class': cls,
    }


def print_student(student): 
    for key, value in student.items():
        print('{:7}: {}'.format(key, value))
    print('===')


s1 = make_student('hanyeong.lee', 30, 'male', 'FDS')
print_student(s1)

# make_student를 키워드인자로 호출한 결과를 s2에 할당
# 키워드인자 순서는 age, name, gender순으로 주어짐
s2 = make_student(cls='Android', age=28, name='boyeong.park', gender='female')
print_student(s2)

