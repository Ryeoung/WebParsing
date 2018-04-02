import os
import sys
import urllib.request
import json
#딕션너리로 받아서 parsing 하는 함수
def print_book(info):
    title=info.get('title').replace('<b>','')
    title=title.replace('</b>','')
    author=info.get('author')
    isbn=info.get('isbn')
    print("--------------------------------------------------------------------------------------------------")
    print("책 재목 : %s \n 책 저자 : %s \n isbn: %s" %(title,author,isbn))

client_id = "MNyk0DBRTQWENkYDFaEe"
client_secret = "nr3PR0xAHH"
#검색할 단어를 입력한는 함수
encText = urllib.parse.quote("주식")
#json으로 데이터를 받음
url = "https://openapi.naver.com/v1/search/book?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
#requset header에 내가 네이버에 등록한 client_id 와 받은 client_secret를 넣는 부분
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
#request를 보내고 resspone을 json 형태로 받는 부분
response = urllib.request.urlopen(request)
#respone의 http 코드를 rescode애 저장
rescode = response.getcode()
#rescode가 200이면 제대로 받음
if(rescode==200):
    #response_body에 패킷 body 부분만 읽어 저장한다
    response_body = response.read()
    #json 파일을 딕션너리 자료형 형태로 respon_json에 저장
    respon_json= json.loads(response_body.decode('utf-8'))
    #respon_json의 items key값에 책에 관한 내용이 저장되어 있어 따로 빼냄 자료형은 리스트
    items=respon_json["items"]
    #items은 리스트 자료형이고 리스트 요소 요소는 딕션너리 자료형으로 이루어짐
    for i in items:
        #print_book 함수를 통해서 딕션너리를 parsiong하고 출력
        print_book(i)


else:
    #만약 http 코드가 200이 아닐 경우 모두 에러로 처리하고 에러 표시
    print("Error Code:" + rescode)