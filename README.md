# HScan
## 项目创建于北京时间2023年2月19日
### 作者近期需要参加学校比赛，该项目更新比较慢

```
功能：
-- poc扫描(单链接或者批量扫描)
-- 网页url提取
```
```
未来更新功能：
-- 自动化深度扫描
-- cms指纹识别
-- 多线程工作
-- 更新更丰富的poc库
```

## POC列表
```
CVE-2020-27986
CVE-2023-23752
CVE-2021-36749
CNVD-2021-30167
用友NC目录遍历
泛微OAV8SQL注入
龙璟科技 电池能量BEMS 任意文件下载漏洞
齐治堡垒机任意用户登录
金和OA-C6任意文件下载
一米OA 任意文件读取漏洞
```
## poc检测
![image](https://user-images.githubusercontent.com/46450756/221391060-7b0687d0-46fe-4f36-9714-97471904eee4.png)

## url爬虫
![image](https://user-images.githubusercontent.com/46450756/221391193-150dc6c0-2278-4f58-9046-08ff9c1c0a1d.png)

## 安装:
```
git clone https://github.com/soryecker/HScan.git
cd ./HScan
python3 run.py
```

## 使用:
```

██╗  ██╗██╗  ██╗ ██████╗██╗  ██╗██████╗ ██╗   ██╗███████╗███████╗███████╗██████╗ 
██║  ██║██║  ██║██╔════╝██║ ██╔╝██╔══██╗██║   ██║╚════██║██╔════╝██╔════╝██╔══██╗
███████║███████║██║     █████╔╝ ██████╔╝██║   ██║    ██╔╝█████╗  █████╗  ██████╔╝
██╔══██║╚════██║██║     ██╔═██╗ ██╔══██╗██║   ██║   ██╔╝ ██╔══╝  ██╔══╝  ██╔══██╗
██║  ██║     ██║╚██████╗██║  ██╗██████╔╝╚██████╔╝   ██║  ███████╗███████╗██║  ██║
╚═╝  ╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚═╝  ╚══════╝╚══════╝╚═╝  ╚═╝
                                                
                        ███████╗ ██████╗ ██████╗                                 
                        ██╔════╝██╔═══██╗██╔══██╗                                
                        ███████╗██║   ██║██████╔╝                                
                        ╚════██║██║   ██║██╔══██╗                                
                        ███████║╚██████╔╝██║  ██║                                
                        ╚══════╝ ╚═════╝ ╚═╝  ╚═╝
usage: Run.py [-h] [--url URL] [--timeout TIMEOUT] [--thead THEAD]
              [--file FILE]

未知版本(内测版)

options:
  -h, --help            show this help message and exit
  --url URL, -u URL     需要扫描的url
  --timeout TIMEOUT, -t TIMEOUT
                        指定超时数值,默认为6
  --thead THEAD, -n THEAD
                        线程数,默认为1
  --file FILE, -f FILE  批量url文本
  
 ```

# POC持续更新
