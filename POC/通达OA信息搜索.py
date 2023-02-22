'''
通达OA信息搜索
'''


import requests

import main

info_url = ['/inc/expired.php',
            '/inc/reg_trial.php',
            '/inc/reg_trial_submit.php',
            '/resque/worker.php']


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}


def td_oa(inurl, timeout=6):
    url = inurl+info_url[0]

    re = requests.get(url,verify=False,headers=headers)
    title = re.text
    title = title[title.index('<title>')+len('<title>'):title.index('</title>')]
    if '版' in title:
        main.print_green('版本：'+title)


