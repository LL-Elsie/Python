# pip install requests
import requests
from requests import utils

# 接口地址
url = 'http://127.0.0.1:8787/dar/user/login'
# 请求头
header = {'Content-Type': 'application/x-www-formurlencoded;charset=UTF-8'}
# 参数
data = {
    "user_name": "test01",
    "passwd": "admin123"
}

# -----------------post---------------------------
# 向服务器发起一个http请求
res = requests.post(url=url, data=data)

# 返回文本类型的数据
#print(res.text)
# print(res.text.encode().decode('unicode_escape'))

# 返回二进制内容
# print(res.content)

#  返回json类型
#print(res.json())

# ------------------------get----------------------

url_2 = 'http://127.0.0.1:8787/coupApply/cms/goodsList'
header_2 = {'Content-Type': 'application/x-www-formurlencoded;charset=UTF-8'}

json_data = {
    "msgType": "getHandsetListOfCust",
    "page": 1,
    "size": 20
}
res_2 = requests.get(url=url_2,params=json_data,headers=header_2)
# 默认返回的是接口的一个状态码
# print(res_2)

# 返回文本类型的接口返回值、返回字符串类型

# print(res_2.text,type(res_2.text))

# 返回json格式、返回字典类型
# print(res_2.json(),type(res_2.json()))


# -------------------------requests.session() 会话-----------------
session = requests.session()
# res_3 = session.request(method='get',url=url_2,params=json_data,headers=header_2)
# print(res_3.json())

# -----------------------cookie---------------------------
# 获取接口的cookie
result = session.request(method='post',url=url,data=data)
# 获取接口的cookie
cookie = requests.utils.dict_from_cookiejar(result.cookies)
# print(result.text)
print(cookie)