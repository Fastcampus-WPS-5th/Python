# naver패키지 내부의 NaverWebtoonCrawler클래스형 인스턴스를 생성,
# 인스턴스에서 crawl_episode실행
from naver import NaverWebtoonCrawler

webtoon_id_yumi = 651673
crawler = NaverWebtoonCrawler(webtoon_id_yumi)
crawler.crawl_episode(1)