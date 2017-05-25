import requests


class NaverWebtoonCrawler:
    def __init__(self, webtoon_id):
        self.webtoon_id = webtoon_id

    def crawl_page(self, page_num):
        return '해당 페이지의 에피소드 리스트'

    def crawl_episode(self, episode_num=None):
        if not episode_num:
            return '마지막화'
        return '해당 에피소드'

    def crawl_all_episodes(self):
        return ''


class NaverWebtoon:
    def __init__(self, webtoon_id):
        self.webtoon_id = webtoon_id
        self.episode_list = []

    def get_info(self):
        return '정보 리턴'

    def view_last_episode(self):
        return ''

    def view_episode_list(self, num=1):
        return ''

    def save_webtoon(self, create_html=False):
        if create_html:
            return '다운받은 웹툰을 볼 수 있는 html까지 생성해서 저장'
        return '특정 경로에 웹툰 전체를 다운받아서 저장'


# url을 url과 params dict로 분리
from bs4 import BeautifulSoup

url_naver_webtoon_episode_list = 'http://comic.naver.com/webtoon/list.nhn'
id_1 = 651673
id_2 = 119874
params_webtoon_episode_list = {
    'titleId': id_1,
    'page': 1,
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
# print(type(div_comicinfo_detail_h2.contents))
# print(div_comicinfo_detail_h2.contents)
# title = div_comicinfo_detail_h2.contents[0].strip()
# print(title)
#
# # div.comicinfo > div.detail > h2 > span.wrt_nm.text.strip()
# div_comicinfo_detail_h2_wrt_nm = div_comicinfo_detail_h2.find('span', class_='wrt_nm')
# author_name = div_comicinfo_detail_h2_wrt_nm.text.strip()
# print(author_name)

title = soup.select_one('div.comicinfo > div.detail > h2').contents[0].strip()
author_name = soup.select_one('div.comicinfo > div.detail > h2 > span').text.strip()
print(title, author_name)


class Episode:
    # url_thumbnail, title, rating, date는 property로 구현 (전부 읽기전용, private으로 선언하지 말 것)
    def __init__(self, url_thumbnail, title, rating, date):
        self._url_thumbnail = url_thumbnail
        self._title = title
        self._rating = rating
        self._date = date

    @property
    def url_thumbnail(self):
        return self._url_thumbnail

    @property
    def title(self):
        return self._title

    @property
    def rating(self):
        return self._rating

    @property
    def date(self):
        return self._date

# 1. 전체 에피소드 리스트를 가져오기
# 2. 에피소드 번호를 입력하면(no) 내부의 웹툰 이미지 주소를 가져오기 (여러장의 이미지로 분할되어있음)
# 3. 썸네일이미지 또는 내부 웹툰 이미지를 저장
# 4. 모든것을 통합해서 실행하면 웹툰을 각 화별 폴더를 생성해서 저장하기
# 5. 저장한 파일을 접근할 수 있는 HTML생성

episode_list = []
# 에피소드 리스트를 가져온다
# 각 에피소드는 class Episode형 인스턴스가 되도록 함
# 각 에피소드의 썸네일 이미지 URL, 제목, 별점, 등록일을
# url_thumbnail, title, rating, date에 등록
table = soup.find('table', class_='viewList')
tr_list = table.find_all('tr')
for tr in tr_list:
    if not tr.find('td', class_='title'):
        continue
    title = tr.find('td', class_='title').find('a').text
    link = tr.find('td', class_='title').find('a')['href']

    # td_list = tr.find_all('td')
    # print(td_list)
    # td_rating = td_list[2]
    # print(td_rating)
    # strong = td_rating.find('strong')
    # print(strong)
    # rating = strong.text.strip()

    rating = tr.find_all('td')[2].find('strong').text
    date = tr.find('td', class_='num').text
    print(title)
    print(link)
    print(rating)
    print(date)

    episode = Episode(
        url_thumbnail='',
        title=title,
        rating=rating,
        date=date
    )
    episode_list.append(episode)

for episode in episode_list:
    print(episode)
