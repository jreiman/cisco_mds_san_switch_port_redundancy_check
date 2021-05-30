from san_switch import Switch
from sys import argv

username = argv[1]
password = argv[2]
dukelabmds01 = Switch("dukelabmds01", "172.18.77.159")
dukelabmds02 = Switch("dukelabmds02", "172.18.77.160")

def main():
    dukelabmds01_down_ports_list = dukelabmds01.list_down_ports(username, password)
    dukelabmds02_down_ports_list = dukelabmds02.list_down_ports(username, password)
    print(dukelabmds01_down_ports_list)
    print(dukelabmds02_down_ports_list)

if __name__ == '__main__':
    main()