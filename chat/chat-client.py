from socket import socket
from threading import Thread


def main():
    class RefreshScreenThread(Thread):
        def __init__(self, client):
            super().__init__()
            self._client = client

        def run(self):
            while running:
                data = self._client.recv(1024)
                if not data:
                    break
                print(data.decode('utf-8'))

    nickname = input('Пожалуйста, введите свой ник: ')

    if nickname == 'Piska' or nickname == 'Pisun':
        print('ERROR')
        return

    my_client = socket()
    my_client.connect(('127.0.0.1', 12345))
    running = True
    RefreshScreenThread(my_client).start()
    while running:
        content = input('> ')
        if content == 'byebye':
            my_client.send(content.encode('utf-8'))
            running = False
        else:
            msg = nickname + ': ' + content
            my_client.send(msg.encode('utf-8'))


if __name__ == '__main__':
    main()
