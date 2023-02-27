import requests

import main
from main import print_blue

list = ['Not Found',
        '找不到文件或目录',
        '用户未登录',
        '未找到']


def pocfuntion(pocname='请输入POC名字',  # POC的名字
               url='请输入url链接',  # 检测的主要url
               addurl='请输入url检测链接',  # POC主要检测链接
               timeout=6,  # 超时时间
               errorlist=[],  # 存在非正常返回网页的关键词
               includelist='',
               code='utf-8',  # 网页的解码格式
               verify=False,  # 是否开启证书检测
               ifprint=False
               ):
    if url[-1] == '/':
        url = url[0:len(url)-1]
    if pocname == '请输入POC名字':
        main.print_red(pocname)
    if url == '请输入url链接':
        main.print_red(url)
    if addurl == '请输入url检测链接':
        main.print_red(addurl)
    if verify is True:
        main.print_red('当前为开启证书检测模式')
    errorlist.append(list)
    print_blue(pocname)
    # if not url[0:1] == '/':
    #     url = url + '/'
    try:
        re = requests.get(url+addurl,
                          timeout=timeout,
                          verify=verify)
        re.encoding = code
        # 用于检测返回的数据是否为正常
        if_error = 0
        # 200的网页正常以及存在内容的网页继续
        if str(re) == '<Response [200]>' and re.text:
            # 遍历一些错误的关键词进行比对
            for i in list:
                # 如果不存在这些关键词的返回内容，即if_error为1
                if not i in re.text:
                    if isinstance(includelist, str):
                        return 1
                    elif isinstance(includelist, list):
                        for item in includelist:
                            if item in re.text:
                                if_error = 1
                                if ifprint:
                                    main.print_red(re.text)

                # 但凡有一个是包含其中一种关键词的都if_error为0
                else:
                    if_error = 0
            # 检测if_error是否为1
            if if_error == 1:
                return f'返回成功:{re.text}'
            # 不为1时就返回失败
            else:
                return f'返回失败:{re.text}'
        else:
            return '网页错误'+str(re)
    except ConnectionError as e:
        return '连接失败'
    except TimeoutError as e:
        return '连接超时'
    except Exception as e:
        return '未知错误：' + str(e)

