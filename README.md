# Cisco MDS Switch Port Redundancy Check

## Description
The Cisco MDS switch port redundancy check is used to compare a list of connected ports between 2 Cisco MDS SAN switches and list the ports that are up on only 1 of the 2 switches.

## Requirements
- Python 3.9+  
- Paramiko SSH Module  
```python
python -m pip install paramiko
```

## Usage
The program file "port_redundancy_check.py" requires 4 arguments to be passed in the following order:  
- switch1 IP Address
- switch2 IP Address
- username
- password

**Both switches must use the same username and password*.

```python
python port_redundancy_check.py <switch1_ip> <switch2_ip> <username> <password>
```

## Example
Switch1 has ip address 1.1.1.1, hostname coreswitch01, and  ports fc1/1 and fc1/2 are connected.  
Switch2 has ip address 2.2.2.2, hostname coreswitch02, and only port fc1/1 is connected.  
The program will be initiated as follows:
```python
python port_redundancy_check.py 1.1.1.1 2.2.2.2 username password
```
The output that is returned will be:  
```
Non-Redundant Ports for Switch Pair coreswitch01 & coreswitch02: [fc1/2]
```
The output indicates that switch port fc1/2 is only connected on one of the switches and should be investigated.