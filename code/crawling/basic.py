import re


class Node(object):
    """
    HTML태그 하나를 가지는 클래스
        내부에 다른 클래스를 가질수도 있음
        가장 큰 범위는 <html></html>
    """
    _pattern_tag_base = r'<{tag}.*?>\s*([.\w\W]*?)\s*</{tag}>'
    _pattern_tag_content = r'<[^!]*?>([.\w\W]*)</.*?>'
    _pattern_tag_class = r'^\s*<.*?class\s*=[\'"](.*?)[\'"]>'

    def __init__(self, source):
        self.source = source

    def __str__(self):
        return '{}\n{}'.format(
            super().__str__(),
            self.source
        )

    def find_tag(self, tag):
        """
        주어진 tag 문자열, 또는 문자열의 리스트 반환
        :param tag: 검색을 원하는 태그. ex)'div'
        :param source: 태그를 검색할 전체 문자열
        :return: 검색 결과가 1개일 경우에는 tag문자열로 만든 Node객체, 2개 이상 일 경우에는 tag문자열로 만든 Node의 리스트
        """
        pattern = re.compile(self._pattern_tag_base.format(tag=tag))
        m_list = re.finditer(pattern, self.source)
        if m_list:
            return_list = [Node(m.group()) for m in m_list]
            return return_list if len(return_list) > 1 else return_list[0]
        return None

    @property
    def content(self):
        """
        Node인스턴스의 내용을 리턴
        :return: Node(태그)내부의 내용 문자열을 리턴
        """
        pattern = re.compile(self._pattern_tag_content)
        m = re.search(pattern, self.source.strip())
        if m:
            return m.group(1).strip()
        return None

    @property
    def class_(self):
        """
        해당 Node가 가진 class속성의 value를 리턴 (문자열)
        :return: 
        """
        pattern = re.compile(self._pattern_tag_class)
        m = re.search(pattern, self.source)
        if m:
            return m.group(1)


with open('example.html') as f:
    html = Node(f.read())

node_div = html.find_tag('div')
print(node_div.class_)
node_p_list = node_div.find_tag('p')
# for node_p in node_p_list:
#     print(type(node_p))
#     print(node_p)
    # print(node_p.content)


# pattern_tag_base = r'<{tag}.*?>\s*([.\w\W]*?)\s*</{tag}>'
#
#
# def find_tag(tag, source):
#     """
#     주어진 tag 문자열, 또는 문자열의 리스트 반환
#     :param tag: 검색을 원하는 태그. ex)'div'
#     :param source: 태그를 검색할 전체 문자열
#     :return: 검색 결과가 1개일 경우에는 tag문자열, 2개 이상 일 경우에는 tag문자열의 리스트
#     """
#     pattern = re.compile(pattern_tag_base.format(tag=tag))
#     m_list = re.finditer(pattern, source)
#     if m_list:
#         return_list = [m.group() for m in m_list]
#         return return_list if len(return_list) > 1 else return_list[0]
#     return None
#
#
# # pattern_tag_content = r'^<.*?>([.\w\W]*?)</.*?>$'
# pattern_tag_content = r'<.*?>([.\w\W]*)</.*?>'
#
#
# def get_tag_content(tag_string):
#     """
#     tag 문자열이 주어졌을 때, 해당 tag의 내용을 리턴
#     :param tag_string: <tag>내용</tag>형태의 문자열
#     :return: 위 형태에서 '내용'부분
#     """
#     pattern = re.compile(pattern_tag_content)
#     m = re.search(pattern, tag_string.strip())
#     if m:
#         return m.group(1)
#     return None
#
#
# # html문자열 변수에서 'div'태그의 내용을 찾아 반환하는 함수 실행
# div = find_tag('div', html)
# p_list = find_tag('p', div)
# print(p_list)
# for p in p_list:
#     print(get_tag_content(p))
#
#
# # 원리
# pattern_div = re.compile(r'<div.*?>([.\w\W]*?)</div>')
# m = re.search(pattern_div, html)
# div = m.group(1)
#
# pattern_p = re.compile(r'<p.*?>([.\w\W]*?)</p>')
# m_list = re.finditer(pattern_p, div)
