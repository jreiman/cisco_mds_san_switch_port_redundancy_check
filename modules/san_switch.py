from paramiko import SSHClient, AutoAddPolicy

def ssh_run_single_command(ip_address, username, password, command):
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(hostname=ip_address, port=22, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.readlines()
    output_with_ending_whitespace_removed = [i.rstrip() for i in output]
    ssh.close()
    return output_with_ending_whitespace_removed

class Switch:
    def __init__(self, ip_address, username, password):
        self.ip_address = ip_address
        self.username = username
        self.password = password
    
    def get_list_of_up_ports(self):
        command_list_of_down_ports = "show interface brief | egrep -i 'fc' | egrep -v 'sup' | egrep 'up|trunking' | cut -d ' ' -f 1 | no-more"
        output = ssh_run_single_command(self.ip_address, self.username, self.password, command_list_of_down_ports)
        return output

    def get_hostname(self):
        command_show_switchname = "show switchname"
        output = ssh_run_single_command(self.ip_address, self.username, self.password, command_show_switchname)
        return output
    
    



