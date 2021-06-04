
import requests
import re


def get_lanzhou_url() -> str:

    res = requests.get('http://geem2.com/',)
    r = re.compile(
        r'<a href="(.{10,40})" target="_blank">64位引擎稳定版本下载地址.+?</a>')
    html = res.content.decode('GBK')
    r_res = r.search(html)
    url = r_res.group(1)
    return url


if __name__ == '__main__':
    print(get_lanzhou_url())
