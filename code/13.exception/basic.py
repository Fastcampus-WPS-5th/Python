"""
1. 정규표현식으로 검사했을 때 일치하는 패턴이 없을 경우 발생할 NotMatchedException 을 정의
    1-1. Exception 을 상속
    1-2. __init__ 초기화 메서드에 패턴문자열과 소스문자열을 받도록 함
    1-3. __str__메서드가 일치하는 결과가 없다는 문자열을 리턴하도록 함
2. 패턴문자열과 소스문자열을 매개변수로 갖는 search_from_source 함수를 정의하고, re.search 에 소스 문자열을 전달했을 때
    MatchObject 를 찾지 못하면 NotMatchedException 을 발생시킴
3. try~except 구문에서 위 함수를 실행해 예외를 발생시킴 (raise NotMatchedException(arg1, arg2))
4. 위 구문에 else 절을 추가해서 예외가 발생하지 않았을 경우의 검색결과를 출력
5. 위 구문에 finally 절을 추가해서 프로그램이 끝났음을 출력
"""
import re


class NotMatchedException(Exception):
    """
    pattern, source를 받아 매치되지 않았음을 알려주는 Exception클래스
    """

    def __init__(self, pattern_string, source_string):
        self.pattern_string = pattern_string
        self.source_string = source_string

    def __str__(self):
        return 'Pattern "{}" is not matched in source "{}"'.format(
            self.pattern_string,
            self.source_string
        )


def search_from_source(pattern_string, source_string):
    m = re.search(pattern_string, source_string)
    if m:
        return m
    raise NotMatchedException(pattern_string, source_string)


try:
    source = 'Lux, the Lady of Luminocity'
    # pattern_string = r'L\w{3}\b'
    pattern_string = r'L\w{1}\b'
    m = search_from_source(pattern_string, source)
except NotMatchedException as e:
    print(e)
else:
    print('Search result : {}'.format(m.group()))
finally:
    print('-- Search end --')
