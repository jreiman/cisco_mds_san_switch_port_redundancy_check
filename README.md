# Cisco MDS Switch Port Redundancy Check

## Description
The Cisco MDS switch port redundancy check application is used to compare a list of connected ports between 2 Cisco MDS SAN switches and list the ports that are not up on both switches. 

## What Problem Does This Solve?
It is a best practice in SAN fibre channel switch installations to deploy switches in pairs with each switch in a seperate fabric.   

Devices connected into the SAN are connected to the same port on each switch to provide connection redundancy.

While there are many products that will monitor the status of switch ports, very few are able to compare the state of the ports between 2 switches to determine if a connected device has lost connection redundancy.

## Requirements
- Python 3.9+  
- Paramiko SSH Module  
```python
python3 -m pip install paramiko
```

## Usage
The program file "port_redundancy_check.py" requires 4 arguments to be passed in a specific order.  
- switch1 IP Address
- switch2 IP Address
- username
- password

**Both switches must use the same username and password*.

```python
python3 port_redundancy_check.py <switch1_ip> <switch2_ip> <username> <password>
```


