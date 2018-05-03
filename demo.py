# coding=utf-8
import urllib2


def get_whether():
    content_text = "新余"
    name = urllib2.quote(content_text)  # 用于编码格式的转换
    url = 'http://v.juhe.cn/weather/index?format=2&cityname=%s&key=b7ab23c8e5026e5b07f15eb5f1f804a7' % name
    req = urllib2.Request(url)
    print req
    resp = urllib2.urlopen(req)
    content = resp.read()
    print content
    print type(content)
    content_now = eval(content)
    print content_now
    print type(content_now)
    windy_message = content_now["result"]["sk"]["wind_direction"]
    print "今天的风向是%s" % windy_message

    print content_now["result"]["future"]
    print content_now["result"]["future"][0]["week"],\
        content_now["result"]["future"][0]["temperature"], \
        content_now["result"]["future"][0]["weather"]

    msg = '''
                                                今天是%s
                                                温度是%s
                                                天气是%s
    '''  % (content_now["result"]["future"][0]["week"], content_now["result"]["future"][0]["temperature"],
            content_now["result"]["future"][0]["weather"])
    print msg


get_whether()
