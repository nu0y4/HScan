import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse, urlunparse
import main


def urlCheck(url, isreptile=True):
    url = fix_url(url)
    main.print_yellow(f'爬取{url}链接')
    check_num = 0
    # 定义正则表达式，用于匹配链接
    link_regex = re.compile(r"(?i)https?://\S+")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
    }

    # 获取网页源码

    response = requests.get(url, headers=headers)
    html = response.content

    # 解析HTML并获取所有链接
    soup = BeautifulSoup(html, "html.parser")
    links = []

    for tag in soup.find_all():
        for attr in tag.attrs.values():
            if isinstance(attr, str):
                match = link_regex.search(attr)
                if match:
                    check_num = check_num + 1
                    links.append(match.group(0))

    # 输出所有链接
    main.print_green(f'一共{check_num}条链接')
    for link in links:
        print(link)
        try:
            title = get_title(link, ignore_empty=True)
            main.print_green(title)
        except ConnectionError as e:
            main.print_red('链接错误')
        except Exception as e:
            main.print_red('未知错误:'+e)


def get_title(url, headers=None, ignore_empty=True):
    if not headers:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.title
    if ignore_empty and (not title or not title.string):
        return ""
    return title.string.strip()

def fix_url(url):
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        parsed_url = parsed_url._replace(scheme='http')
    if not parsed_url.netloc:
        raise ValueError("URL格式错误")
    return urlunparse(parsed_url)