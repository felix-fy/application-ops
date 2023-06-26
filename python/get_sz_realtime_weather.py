import urllib.request
import urllib.parse


url = 'https://opendata.sz.gov.cn/api/29200_00903509/1/service.xhtml?'

data = {'appKey': '0d09b55e593b4b759243ecb00f06c1b5',
        'page': '1',
        'rows': '1',
        'startDate': '20230609',
        'endDate': '20230610'}  # 参数列表，字典类型

data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
result = response.read().decode('utf-8')

print(result)
