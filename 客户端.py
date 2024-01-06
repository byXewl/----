import socket

socket_clent = socket.socket()
#链接服务 端
socket_clent.connect(("localhost",8888))
recv_data = socket_clent.recv(1024)
print(f"服务端回复的消息是：{recv_data.decode('UTF-8')}")
while True:
    msg = input("输入要发送的消息:")
    if msg == "exit":
        break
    socket_clent.send(msg.encode("UTF-8"))

    recv_data = socket_clent.recv(1024)
    if not recv_data:
        break
    print(f"服务端回复的 消息是：{recv_data.decode('UTF-8')}")

socket_clent.close()