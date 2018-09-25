import requests
import re
# from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
data = {
    'cate': 'realtimehot'
}

try:
    r = requests.get('http://s.weibo.com/top/summary?cate=realtimehot', params=data, headers=headers)
    # print(r.url)
    if r.status_code == 200:
        html = r.text
except:
    html = ""

# soup = BeautifulSoup(html, "lxml")
# html = str(soup.find_all('script')[-2])[525:-12]
# print(html)
# hot_key = re.findall(r'(?<=list_realtimehot\\">)[\w ]*\\.*?(?=<\\/a>\\n)|(?<=realtime_\d{5}\\"\\n>)\w*\\.*?(?=<\\/a>\\n)', html)
hot_key = re.findall(r'(?<=Refer=top" target="_blank">).*?(?=</a>)|(?<=realtimehot_ad" word=").*?(?=" url_show)', html)
# hot_url= re.findall(r'(?<=\\/weibo\\/)[%,A-Z,a-z,0-9]*?(?=&Refer=top\\" target)', html)
i=0
for x in hot_key:
    print(i+1,end=" ")
    print(x)
    # print(x.encode('latin-1').decode('unicode_escape'))
    i=i+1
