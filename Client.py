import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 12345        # The port used by the server

def receive_messages(client_socket):
    while True:
        try:
            # Receive message from server
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)
        except:
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    # Start a thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    while True:
        # Send message to server
        message = input()
        if message.lower() == 'exit':
            break
        client.send(message.encode('utf-8'))

    client.close()

if __name__ == "__main__":
    main()
