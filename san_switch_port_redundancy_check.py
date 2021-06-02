from san_switch import Switch
from sys import argv
from list_comparison import find_differences_between_two_lists_and_sort_result as differences

switch1_ip_address = argv[1]
switch2_ip_address = argv[2]
username = argv[3]
password = argv[4]

switch1 = Switch(switch1_ip_address, username, password)
switch2 = Switch(switch2_ip_address, username, password)

def main():
    switch1_hostname = switch1.get_hostname()
    switch2_hostname = switch2.get_hostname()
    switch1_list_of_up_ports = switch1.get_list_of_up_ports()
    switch2_list_of_up_ports = switch2.get_list_of_up_ports()
    differences_between_switch1_and_switch2_list_of_up_ports = differences(switch1_list_of_up_ports, switch2_list_of_up_ports)
    print(switch1_hostname)
    print(switch2_hostname)
    print(switch1_list_of_up_ports)
    print(switch2_list_of_up_ports)
    print(differences_between_switch1_and_switch2_list_of_up_ports)

if __name__ == '__main__':
    main()