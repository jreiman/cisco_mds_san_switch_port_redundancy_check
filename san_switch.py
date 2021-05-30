from paramiko import SSHClient, AutoAddPolicy

def ssh_run_single_command(ip_address, username, password, command):
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(hostname=ip_address, port=22, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.readlines()
    output = [i.rstrip() for i in output]
    ssh.close()
    return output

class Switch:
    def __init__(self, hostname, ip_address):
        self.hostname = hostname
        self.ip_address = ip_address
    
    def list_down_ports(self, username, password):
        command_list_down_ports = "show interface brief | egrep -i 'fc' | egrep -v 'sup' | egrep -v 'up|trunking' | cut -d ' ' -f 1 | no-more"
        output = ssh_run_single_command(self.ip_address, username, password, command_list_down_ports)
        return output



