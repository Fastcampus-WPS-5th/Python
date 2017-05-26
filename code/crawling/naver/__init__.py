import os


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
        os.makedirs('{}/{}'.format(self.webtoon_id, episode_num))
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
