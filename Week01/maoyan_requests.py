# 安装并使用 requests、bs4 库，爬取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
# 使用requests库获取猫眼电影信息
# 使用BeautifulSoup解析网页

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

cookie = 'uuid_n_v=v1; uuid=3C72C500094511EBA174E19CC73B5E537C8F8D1C4C09434389766CBD1524C548; _csrf=d1a2e04f83b8adc3b883f7a18f73e3ead6c7fa58dfe48abdb797c9cf2ff6de51; _lxsdk_cuid=175077429a4c8-0717ce5184234d8-7824675c-144000-175077429a4c8; _lxsdk=3C72C500094511EBA174E19CC73B5E537C8F8D1C4C09434389766CBD1524C548; __mta=44347803.1602147855117.1602156066577.1602157714366.16; _lxsdk_s=17507f16efe-57e-b39-cf7%7C%7C5'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {'Cookie':cookie,'user-agent':user_agent}

myurl = 'https://maoyan.com/films?showType=1'

# 通过get方法得到一个Response对象
response = requests.get(myurl,headers=header)

# 得到一个BeautifulSoup对象
soup = bs(response.text, 'html.parser')

dl_data = soup.find_all('dd')[:10]

save_data = []

for item in dl_data:
    name = item.find('span',attrs={"class":"name"}).text
    tag = item.find('div',attrs={"class":"movie-hover-info"}).select("div")[1].get_text().replace('类型:', '').replace(' ', '').replace('\n', '')
    release = item.find('div',attrs={"class":"movie-hover-info"}).select("div")[3].get_text().replace('上映时间:', '').replace(' ', '').replace('\n', '')
    row = [name, tag, release]
    print(row)
    save_data.append(row)


save_df = pd.DataFrame(save_data, columns=["电影名", "类型", "上映时间"])
save_df.to_csv("./maoyan_requests.csv", index=False) # 不保留行索引
