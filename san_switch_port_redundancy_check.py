from san_switch import ssh_run_single_command
from san_switch import Switch


command = "show interface brief | egrep -i 'fc' | egrep -v 'sup' | egrep -v 'up|trunking' | cut -d ' ' -f 1 | no-more"
dukelabmds01 = Switch("dukelabmds01", "172.18.77.159")

def main():
    print(dukelabmds01.hostname)

if __name__ == '__main__':
    main()