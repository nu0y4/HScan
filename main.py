from colorama import Fore

logo_pic_h = '''
██╗  ██╗██╗  ██╗ ██████╗██╗  ██╗██████╗ ██╗   ██╗███████╗███████╗███████╗██████╗ 
██║  ██║██║  ██║██╔════╝██║ ██╔╝██╔══██╗██║   ██║╚════██║██╔════╝██╔════╝██╔══██╗
███████║███████║██║     █████╔╝ ██████╔╝██║   ██║    ██╔╝█████╗  █████╗  ██████╔╝
██╔══██║╚════██║██║     ██╔═██╗ ██╔══██╗██║   ██║   ██╔╝ ██╔══╝  ██╔══╝  ██╔══██╗
██║  ██║     ██║╚██████╗██║  ██╗██████╔╝╚██████╔╝   ██║  ███████╗███████╗██║  ██║
╚═╝  ╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚═╝  ╚══════╝╚══════╝╚═╝  ╚═╝'''

logo_pic_t = '''                                                
                        ███████╗ ██████╗ ██████╗                                 
                        ██╔════╝██╔═══██╗██╔══██╗                                
                        ███████╗██║   ██║██████╔╝                                
                        ╚════██║██║   ██║██╔══██╗                                
                        ███████║╚██████╔╝██║  ██║                                
                        ╚══════╝ ╚═════╝ ╚═╝  ╚═╝'''


def hprint(context='',  # 内容。
           enter=True,  # 是否在内容之后回车
           logo=False
           ):
    if logo:
        print_red(logo_pic_h, tf=False)
        print_green(logo_pic_t, tf=False)
    else:
        if enter:
            print(f'{context}')
        else:
            print(f'{context}', end='')


def print_red(context='====检测到漏洞===='):
    hprint(Fore.RED + context + Fore.RESET)


def print_green(context='====检测到漏洞===='):
    hprint(Fore.GREEN + context + Fore.RESET)


def print_white(context='====检测到漏洞===='):
    hprint(Fore.WHITE + context + Fore.RESET)


def print_black(context='====检测到漏洞===='):
    hprint(Fore.BLACK + context + Fore.RESET)


def print_yellow(context='====检测到漏洞===='):
    hprint(Fore.YELLOW + context + Fore.RESET)


def print_blue(context='====检测到漏洞===='):
    hprint(Fore.BLUE + context + Fore.RESET)
