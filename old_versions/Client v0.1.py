# Python program to implement client side of chat room.

# We're going to go hardcore and use tkinter!

import socket
import select
import os
import sys

from _thread import *
from tkinter import *
  
server = socket.socket()
if len(sys.argv) != 3: 
    print("Correct usage: script, IP address, port number")
    
IP_address = input('Please enter the host ip address: ')
Port = 1234

print('Connecting...')
server.connect((IP_address, Port))
print('Done connecting! \n')

server.send(os.getlogin().encode())

def tkintering():
    '''
    tkintering()
    Does some tkinter stuff.
    '''
    def send(event = None):
        '''
        send()
        Sends stuff to the server!
        '''
        if len(e.get()) > 0:
            server.send(e.get().encode())
            print('[You] ' + e.get())
            e.delete(0, END)
        
    root = Tk()
    root.title('Python ChatRoom')
    root.iconbitmap(os.getcwd() + '\\' + 'message.ico')
    e = Entry(root, width = 50, font = ('Segoe UI', 12))
    e.grid(row = 0, column = 0)
    b = Button(root, text = 'Send', command = send, font = ('Segoe UI', 12))
    b.grid(row = 0, column = 1)
    root.bind('<Return>', send)
    root.grid()
    
    
    root.deiconify()
    root.mainloop()

# Start the tkinter thread!
start_new_thread(tkintering, ())
  
while True: 
  
    # maintains a list of possible input streams 
    sockets_list = [server] 
  
    """ There are two possible input situations. Either the 
    user wants to give  manual input to send to other people, 
    or the server is sending a message  to be printed on the 
    screen. Select returns from sockets_list, the stream that 
    is reader for input. So for example, if the server wants 
    to send a message, then the if condition will hold true 
    below. If the user wants to send a message, the else 
    condition will evaluate as true"""
    read_sockets = sockets_list
  
    for socks in read_sockets:
        if socks == server: 
            message = socks.recv(2048) 
            print(str(message)[2:-1])
            
server.close() 
