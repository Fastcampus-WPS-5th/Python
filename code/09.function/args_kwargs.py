def print_args(*args, **kwargs):
    '입력받은 positional arguments를 출력해줍니다'
    print(args)
    print(kwargs)


def print_kwargs(**kwargs):
    print(kwargs)


print_args('python', 'ruby', 'java', language='python', ide='pycharm')
print('')
print_args(language='python', ide='pycharm')
print('')

print_kwargs(language='python', ide='pycharm')
print('')
#print_kwargs('python', 'ruby', 'java')
print('')
