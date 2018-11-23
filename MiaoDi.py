


class  MiaoDi:
    pass

auth_token = 'a1403ae464864b5aaa8355b253f661c2'

account_sid = 'e595e7361d8d4c82bc2eacc1fa2c786c'

url = 'https://api.miaodiyun.com/20150822/industrySMS/sendSMS'

headers = {'Content-type': 'application/x-www-form-urlencoded'}

templateid = '309107489'

import time
timestamp = time.strftime('%Y%m%d%H%M%S')

#把sig参数用md5加密
sig = account_sid + auth_token + timestamp
import hashlib
md = hashlib.md5()
md.update(sig.encode('utf-8'))

sig = md.hexdigest()


to = '15915454257'

code = '晚上好苗苗'

data = {
    'accountSid': account_sid,
    'templateid': templateid,
    'to': to,
    'param': code,
    'timestamp': timestamp,
    'sig': sig
}
# 将字典转换为url参数形式
from urllib.parse import urlencode
data = urlencode(data)
# 创建浏览器对象
import http.client
connect = http.client.HTTPConnection('api.miaodiyun.com')
# 发送POST请求
connect.request(method='POST', url=url, body=data, headers=headers)
# 获取响应
resp = connect.getresponse()
# 打印响应结果
print(resp.read().decode('utf-8'))



