import requests

# url을 url과 params dict로 분리
from bs4 import BeautifulSoup

url_naver_webtoon_episode_list = 'http://comic.naver.com/webtoon/list.nhn'
params_webtoon_episode_list = {
    'titleId': '651673',
    'weekday': 'wed',
}


# 이 작업들을 한 번에 처리해주는 함수를 구현
def get_html_from_url(url, params):
    # 실제 요청한 URL(URL과 Params가 합쳐진)을 print해보기
    # print(무언가) -> 위의 url과 params를 조합해서 만들어질 요청URL을 출력
    # 위의 두 변수(url, params)는 사용하면 안됨. requests라이브러리가 지원하는 방식으로 해결
    response = requests.get(url, params)

    # 요청한 URL을 출력
    # print(response.url)

    # 응답의 상태코드를 출력
    # print(response.status_code)

    # 응답의 텍스트 인코딩을 출력
    # print(response.encoding)

    return response.text


html = get_html_from_url(url_naver_webtoon_episode_list, params_webtoon_episode_list)
# pip install lxml
soup = BeautifulSoup(html, 'lxml')

# div.comicinfo
div_comicinfo = soup.find('div', class_='comicinfo')

# div.comicinfo > div.detail
div_comicinfo_detail = div_comicinfo.find('div', class_='detail')

# div.comicinfo > div.detail > h2
div_comicinfo_detail_h2 = div_comicinfo_detail.find('h2')

# div.comicinfo > div.detail > h2.contents[0].strip()
print(type(div_comicinfo_detail_h2.contents))
print(div_comicinfo_detail_h2.contents)
title = div_comicinfo_detail_h2.contents[0].strip()
print(title)

# div.comicinfo > div.detail > h2 > span.wrt_nm.text.strip()
div_comicinfo_detail_h2_wrt_nm = div_comicinfo_detail_h2.find('span', class_='wrt_nm')
author_name = div_comicinfo_detail_h2_wrt_nm.text.strip()
print(author_name)


class Episode:
    pass


episode_list = []
# 에피소드 리스트를 가져온다
# 각 에피소드는 class Episode형 인스턴스가 되도록 함
# 각 에피소드의 썸네일 이미지 URL, 제목, 별점, 등록일을
# url_thumbnail, title, rating, date에 등록
