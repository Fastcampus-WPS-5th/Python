import os

import requests
from bs4 import BeautifulSoup


class NaverWebtoonCrawler:
    _url_detail_base = 'http://comic.naver.com/webtoon/detail.nhn?' \
                       'titleId={webtoon_id}&' \
                       'no={episode_num}&' \
                       'weekday=wed'

    def __init__(self, webtoon_id):
        self.webtoon_id = webtoon_id

    def crawl_page(self, page_num):
        return '해당 페이지의 에피소드 리스트'

    def crawl_episode(self, episode_num=None):
        """
        webtoon_id에 해당하는 웹툰의 episode_num화 내부의 이미지를 저장
        :param episode_num: 
        :return: 
        """
        def make_episode_dir():
            # 이미지를 저장하기 위한 폴더 생성
            dir_path = '{}/{}'.format(self.webtoon_id, episode_num)
            print(dir_path)
            # exists로 이미 생성하려는 폴더가 있는지 검사
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
                print('dir created')
            print('dir exist')

            # try~except구문으로 이미 폴더가 존재할경우 예외처리
            try:
                os.makedirs(dir_path)
            except FileExistsError as e:
                print('dir exist, error:', e)

            # exist_ok매개변수 추가
            os.makedirs(dir_path, exist_ok=True)

        def get_img_tag_list():
            """
            디테일페이지에서 img Tag(bs4)의 리스트를 반환
            :return: 
            """
            # 디테일 페이지의 html을 가져와 img의 href를 출력
            # print(url_detail)
            # requests를 이용해서 url_detail에 get요청을 보냄
            response = requests.get(url_detail)
            # with open('test.html', 'wt') as f:
            #     f.write(response.text)
            # 응답(Response)에서 .text를 이용해 내용을 가져옴
            # 가져온 응답내용을 이용해 BeautifulSoup인스턴스를 생성 (soup)
            soup = BeautifulSoup(response.text, 'lxml')
            # soup인스턴스에서 select_one메서드를 사용해 웹툰뷰어 태그를 리턴
            div_wt_viewer = soup.select_one('div.wt_viewer')
            # 웹튠뷰어 태그에서 img태그들을 전부 찾아 리스트로 반환
            img_list = div_wt_viewer.find_all('img')
            return img_list

        if not episode_num:
            url_detail = self._url_detail_base.format(
                self.webtoon_id,
                '마지막 에피소드 넘버 가져오기'
            )
        else:
            url_detail = self._url_detail_base.format(
                webtoon_id=self.webtoon_id,
                episode_num=episode_num
            )

        # 이미지를 다운받을 폴더 생성
        make_episode_dir()

        # 이미지 태그 목록 가져오기
        img_list = get_img_tag_list()

        # 리스트를 순회하며 각 img태그의 src속성을 출력 및 다운로드
        for img in img_list:
            print(img['src'])
            

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


class NaverWebtoonEpisode:
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
