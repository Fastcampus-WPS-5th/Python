import re

f = open('example.html')
html = f.read()

pattern_tag_base = r'<{tag}.*?>\s*([.\w\W]*?)\s*</{tag}>'


def find_tag(tag, source):
    """
    주어진 tag 문자열, 또는 문자열의 리스트 반환
    :param tag: 검색을 원하는 태그. ex)'div'
    :param source: 태그를 검색할 전체 문자열
    :return: 검색 결과가 1개일 경우에는 tag문자열, 2개 이상 일 경우에는 tag문자열의 리스트
    """
    pattern = re.compile(pattern_tag_base.format(tag=tag))
    m_list = re.finditer(pattern, source)
    if m_list:
        return_list = [m.group() for m in m_list]
        return return_list if len(return_list) > 1 else return_list[0]
    return None


ex_string1 = '<div class="content">ASDF\n\t</div>'
ex_string2 = '<div class="content">'
ex_string3 = '<p class="content">'
p = '<.*?>([.\w\W]*?)</.*?>'

# pattern_tag_content = r'^<.*?>([.\w\W]*?)</.*?>$'
pattern_tag_content = r'<.*?>([.\w\W]*)</.*?>'


def get_tag_content(tag_string):
    """
    tag 문자열이 주어졌을 때, 해당 tag의 내용을 리턴
    :param tag_string: <tag>내용</tag>형태의 문자열
    :return: 위 형태에서 '내용'부분
    """
    pattern = re.compile(pattern_tag_content)
    m = re.search(pattern, tag_string.strip())
    if m:
        return m.group(1)
    return None


# html문자열 변수에서 'div'태그의 내용을 찾아 반환하는 함수 실행
div = find_tag('div', html)
p_list = find_tag('p', div)
print(p_list)
for p in p_list:
    print(get_tag_content(p))


# 원리
pattern_div = re.compile(r'<div.*?>([.\w\W]*?)</div>')
m = re.search(pattern_div, html)
div = m.group(1)

pattern_p = re.compile(r'<p.*?>([.\w\W]*?)</p>')
m_list = re.finditer(pattern_p, div)
