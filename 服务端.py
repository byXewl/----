import socket

socket_server = socket.socket() # 默认是tcp的socket
# 绑定ip和端口
socket_server.bind(("localhost", 8888))
# 监听端口
socket_server.listen(1) # 允许链接的数量
# 等待客户端链接
result = socket_server.accept()
# result是一个二元元组
#conn = result[0]
#address = result[1]
conn,address = result
#accept是阻塞方法，等待客户端连接卡在这
print(f"接收到了客户端的链接，客户端信息：{address}")
conn.send("你好客户端！".encode("UTF-8"))

while True:
    #接收客户端信息
    data = conn.recv(1024).decode("UTF-8")
    # recv接收的参数是缓冲区大小，1024即可
    # recv返回是一个字节数字bytes对象，不是字符串，通过decode方法编码，将其转化成字符串对象
    if not data:
        break
    print(f"客户端发来的信息是：{data}")
    #发送回复消息
    msg = input("请输入要发送客户端的消息：")
    if msg == "exit":
        break
    conn.send(msg.encode("UTF-8"))

#关闭连接
conn.close()
socket_server.close()







