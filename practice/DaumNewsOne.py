# 웹 크롤링 => 네이버 뉴스

import requests
from bs4 import BeautifulSoup


# requests => 웹사이트 코드 복사 GET
# BeautifulSoup4 => requests GET 해온 코드에서 필요한 정보만 find해서 가져오기

url = 'https://news.v.daum.net/v/20211021152915953'
result = requests.get(url)
# print(result.text)

# <tag id of class> </tag>
# class => .
# id => #

# title = doc.select('h3.tit_view') # list type
# title2 = doc.select('h3.tit_view')[0]

doc = BeautifulSoup(result.text, 'html.parser')
title = doc.select('h3.tit_view')[0].get_text()
contents = doc.select('section p')

contents.pop(-1) # 기자 정보 삭제
content = '' # 본문 총합
for info in contents:
    content += info.get_text()

print('###########################################')
print('#뉴스 제목: {}'.format(title))
print('###########################################')
print('# 뉴스 본문: {}'.format(content))
