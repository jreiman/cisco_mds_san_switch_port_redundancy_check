# Cisco MDS Switch Port Redundancy Check

## Description
The Cisco MDS switch port redundancy check is used to compare a list of connected ports between 2 Cisco MDS SAN switches and list the ports that are up on only 1 of the 2 switches.

## What Problem Does This Solve?
It is a best practice in SAN fibre channel switch installations to deploy switches in pairs with each switch in a seperate fabric.   

Devices are connected to the same port on each switch to provide connection redundancy.

There are many programs that will alert on down ports, but they also alert when a port goes down for a planned activity such as a server reboot which can create a lot of false alerts.

By comparing the list of up ports on a pair of switches and listing those ports that are only up on 1 of the 2 switches, it eliminates the false alerts when both ports are down during a planned server reboot.

## Requirements
- Python 3.9+  
- Paramiko SSH Module  
```python
python -m pip install paramiko
```

## Usage
The program file "port_redundancy_check.py" requires 4 arguments to be passed in a specific order.  
- switch1 IP Address
- switch2 IP Address
- username
- password

**Both switches must use the same username and password*.

```python
python port_redundancy_check.py <switch1_ip> <switch2_ip> <username> <password>
```


