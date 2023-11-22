# Example usage:
#
# python select_server.py 3490

import sys
import socket
import select


def run_server(port):
    listening_socket = build_listening_socket(port)

    reading_sockets = {listening_socket}

    while True:
        ready_sockets, _, _ = select.select(reading_sockets, {}, {})

        for s in ready_sockets:
            if s is listening_socket:
                new_socket, _ = s.accept()
                print(f"{new_socket.getpeername()}: connected")
                reading_sockets.add(new_socket)

            else:
                data = s.recv(4096)

                if data != b'':
                    print(f'{s.getpeername()} {len(data)} bytes: {data}')
                else:
                    reading_sockets.remove(s)
                    print(f"{s.getpeername()}: disconnected")
                    s.close()


def build_listening_socket(port):
    listening_socket = socket.socket()
    listening_socket.bind(('', port))
    listening_socket.listen()

    print('waiting for connections')
    return listening_socket


#--------------------------------#
# Do not modify below this line! #
#--------------------------------#

def usage():
    print("usage: select_server.py port", file=sys.stderr)

def main(argv):
    try:
        port = int(argv[1])
    except:
        usage()
        return 1

    run_server(port)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
