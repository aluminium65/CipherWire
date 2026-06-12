import socket
import argparse

def connection(target_ip, target_port):
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
          tcp_socket.connect((target_ip, target_port))
          print(f"[+] Connected Successfully to {target_ip}!")
        except socket.error as e:
          print(f'Connection Error: {e}')
        finally:
          tcp_socket.close()


def listen_connection(target_port):
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.bind(('localhost', target_port))
        tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcp_socket.listen(1)
        print(f"[+] Listening on {socket.gethostname()} : {target_port}")
        client, addr = tcp_socket.accept()
        print(f"[+] Accepted connection from {addr}")
        tcp_socket.close()
        client.close()



if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="ShadowNetwork")
        parser.add_argument('-t', '--target', type=str, help='Enter the IP')
        parser.add_argument('-p', '--port', type=int, default=5555, help='Enter Port number')
        parser.add_argument('-l', '--listen', action='store_true', help='listen for connection on the specified port.')
        args = parser.parse_args()

        if args.listen == True:
          print(f"Listening on Port: {args.port}")
          listen_connection(args.port)

        else:
          connection(args.target, args.port)
