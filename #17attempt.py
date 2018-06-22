#17 attempt
import urllib.request
import urllib.parse
import re

'''
try:
    url='https://www.nytimes.com/'
    values={'s':'basics',
            'submit':'search'}
    headers={}
    headers['User-Agent']='Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    data=urllib.parse.urlencode(values)
    data=data.encode('utf-8')
    req=urllib.request.Request(url,headers=headers)
    req_2=urllib.request.Request(url,data)
    resp=urllib.request.urlopen(req)
    resp_2=urllib.request.urlopen(req_2)
    respData=resp.read()
    respData_2=resp_2.read()
    paragraphs=re.findall(r'<p>(.*?)</p>',str(respData))
    paragraphs_2=re.findall(r'<p>(.*?)</p>',str(respData_2))
    for each in paragraphs:
        print(each)
    for eachP in paragraphs_2:
        print(eachP)
except Exception as e:
    print(str(e))
'''

try:
    url='https://www.nytimes.com/'
    headers={}
    headers['User-Agent']='Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    req=urllib.request.Request(url,headers=headers)
    resp=urllib.request.urlopen(req)
    respData=resp.read()
    paragraphs=re.findall(r'<p>(.*?)</p>',str(respData))
    for each in paragraphs:
        print(each)
        
except Exception as e:
    print(str(e))

