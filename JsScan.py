import re
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from main import print_red, print_green


# def get_js_api(js_code):
#     # 创建PyExecJS上下文
#     ctxt = PyExecJS.compile(js_code)
#     # 获取全局对象
#     global_obj = ctxt.eval('this')
#     # 查找所有函数名和变量名
#     pattern = r'[a-zA-Z]+\w*(?=\()|[a-zA-Z]+\w*(?!=\()'
#     matches = re.findall(pattern, js_code)
#     # 过滤出可能为API的名称
#     apis = []
#     for match in matches:
#         if match in global_obj and callable(global_obj[match]):
#             apis.append(match)
#     return list(set(apis))

def browse_webpage(url):
    # 使用Chrome浏览器引擎打开网页
    options = webdriver.ChromeOptions()  # 创建一个配置对象
    options.add_argument("--headless")  # 开启无界面模式
    options.add_argument("--disable-gpu")  # 禁用gpu
    driver = webdriver.Chrome(chrome_options=options)
    try:
        driver.get(url)
        # 获取网页源代码
        html = driver.page_source
        # 关闭浏览器并杀掉Chrome进程
        driver.quit()
        webdriver.Chrome(service_log_path=None).service.stop()
        # 返回网页内容
        return html
    except:
        print_red('[!]出错！网络连接失败或者chrome引擎未安装')
        return '错误'


def parse_js_links(html):
    # 匹配script标签中src属性的正则表达式
    pattern = re.compile(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', re.IGNORECASE)
    # 从网页源码中查找所有匹配的JS链接
    js_links = []

    for script in pattern.findall(html):
        # 匹配script标签中的src属性值的正则表达式
        src_pattern = re.compile(r'src=["\'](.*?)["\']', re.IGNORECASE)
        src_match = src_pattern.search(script)
        if src_match:
            link = src_match.group(1)
            if link.startswith("//"):
                # 去除前两个斜杠
                link = link[2:]
            js_links.append(link)

    return js_links


def extract_domain(url):
    pattern = r'^http[s]?:\/\/([\w.]+)\/'
    match = re.match(pattern, url)
    if match:
        return match.group(1)
    else:
        return None


def run(url):
    req = browse_webpage(url)
    if not req == '错误':
        for i in parse_js_links(req, ):
            if i.startswith("/") and not i.startswith("//"):
                domain = extract_domain(url)
                js_url = domain + i
                print(js_url)
            else:
                print(i)


def main():
    print_green('[+]当前模式为js爬虫')
    print_red('退出请输入"退出/exit"')
    while True:
        url = input('请输入URL: ')
        if '退出' == url or 'exit' == url:
            break
        else:
            run(url)
            print('=' * 10)


if __name__ == '__main__':
    main()
