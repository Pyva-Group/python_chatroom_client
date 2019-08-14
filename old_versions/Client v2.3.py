# Python program to implement client side of chat room.
# Created by the Pyva Group. 

# Update v2.3
# May 20, 2019
# Optimized for the client end.
# Includes an agreement and stuff.
# Help menu integration.
# Yoy! Almost ready for release. 

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



# Gotta get them to agree to the whole thing first if necessary!

f = open('README.txt', 'r')
info = ''.join(f.readlines())
if info[353] != '0':
    read = False
    info = info[:353] + '1' + info[354:]
else:
    read = True
f.close()


def tkintering():
    '''
    tkintering()
    All the agreement and terms and conditions stuff.
    '''
    # Disable just closing.
    def on_closing():
        '''
        on_closing()
        Hehehehehehe
        '''
        print('Please take the time to actually read this. ')
        tkintering()
    
    # Did the actually read it?
    def agree(event = False):
        '''
        agree()
        They actually agree!
        '''
        f = open('README.txt', 'r')
        info = ''.join(f.readlines())
        f.close()

        
        root.destroy()
        print('Thank you for reading through all of that. ')
        return

    def meh(event = False):
        '''
        meh()
        Meh.
        '''
        print('You have not accepted the Terms and Conditions. ')
        print('Please tell us why you did not agree so that we can improve our service. ')
        print('(Your files have remained intact. ')
        root.destroy()
        sys.exit()
        return

    def disagree(event = False):
        '''
        disagree()
        Wipe this program!
        '''
        try:
            os.remove(os.getcwd() + '\\' + os.path.basename(__file__))
        except:
            pass
        print('You have disagreed, so the SOFTWARE has been wiped from your hard drive. ')
        print('Have a nice day! :) ')
        root.destroy()
        sys.exit()
        return
    
    root = Tk()
    root.title('Terms and Conditions')
    root.iconbitmap(os.getcwd() + '\\message.ico')

    # Label!
    l = Label(root, height = 2, width = 50, font = ('Segoe UI', 18))
    l['text'] = 'Terms and Conditions of Use for this Python ChatRoom'
    l.grid(row = 0, column = 0, columnspan = 2)

    # Text widget!
    t = Text(root, height = 30, width = 100, font = ('Segoe UI', 12), wrap = WORD)
    t['bg'] = '#FEFEFE'
    t.grid(row = 1, column = 0, columnspan = 2)

    # Scrollbar!
    s = Scrollbar(root, orient = VERTICAL)
    s.grid(row = 1, column = 2, sticky = N + S)
    s.config(command = t.yview)
    t.config(yscrollcommand = s.set)

    # Get all the long words! 
    f = open('Terms and Conditions.txt', 'r')
    tac = ''.join(f.readlines())
    f.close()
    t.insert(END, tac)
    t.config(state = DISABLED)

    # Buttons!
    b = Button(root, text = 'I accept', font = ('Segoe UI', 10), command = disagree)
    b.bind('<Button-2>', agree)
    b.bind('<Button-3>', agree)
    b.grid(row = 2, column = 0)
    b2 = Button(root, text = 'I do not accept', font = ('Segoe UI', 10), command = disagree)
    b2.bind('<Button-2>', agree)
    b2.bind('<Button-3>', meh)
    b2.grid(row = 2, column = 1)
    

    # Done!
    root.resizable(width = False, height = False)
    root.protocol('WM_DELETE_WINDOW', on_closing)
    root.mainloop()

if not read:

    print('Please make sure you read all of this. Especially the end! That is the most important part. ')
    
    tkintering()
    f = open('README.txt', 'w')
    f.write(info)
    f.close()
    print('Please take the time to read these Terms and Conditions. ')
    print('If you do not, bad stuff will likely happen. ')

    

# Now, start the actual program! :P  
server = socket.socket()
if len(sys.argv) != 3: 
    print("Correct usage: script, IP address, port number")

localIP = socket.gethostbyname(socket.gethostname())
print('Your local IP address is ' + localIP + '. ')
IP_address = input('Please enter the host ip address: ')
if len(IP_address) == 0:
    IP_address = localIP
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
    if len(e.get()) != 0:
        server.send(e.get().encode())
        root.destroy()

print('Please enter the password in the Tkinter window. ')

root = Tk()
root.grid()

root.title('Password Entry')
root.bind('<Return>', send_password)
root.iconbitmap(os.getcwd() + '\\message.ico')

l = Label(root, text = 'Password: ', font = ('Segoe UI', 12))
l.grid(row = 0, column = 0)

e = Entry(root, width = 50, font = ('Segoe UI', 12))
e.grid(row = 0, column = 1)

b = Button(root, width = 50, text = 'Enter', font = ('Segoe UI', 12), command = send_password)
b.grid(row = 1, column = 1)

root.resizable(width = False, height = False)
root.lift()
root.deiconify()
root.mainloop()

def sound(s):
    '''
    sound(s)
    Plays a sound from the specified directory!
    '''
    winsound.PlaySound(s, 1)

# The listening stuff!
def listen():
    '''
    listen()
    Listens to the server!
    '''
    
    # Now acutally doing stuff!
    read_sockets = [server] # (Perhaps for establishing private connections in a later update.) 

    while True: 

        # Each loop, we check for inputs and print them out. 
        try:
          
            for socks in read_sockets:
                if socks == server:
                    
                    m = socks.recv(2048).decode()
                    messes = m.split('\n')
                    for message in messes:

                        if message == ' ' * len(message):
                            continue

                        if ']' in message and '[' in message:
                            legitMessage = message[message.index(']') + 2:]
                            usernames.insert(END, message[:message.index(']') + 1])

                            if legitMessage.startswith('/w'):
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
                                start_new_thread(sound, (os.getcwd() + '\\erro.wav',))

                            # Execution!
                            elif message.startswith('/exec '):

                                try:
                                    commands = message.split(' ')
                                    exec(' '.join(commands[1:]))
                                except:
                                    continue
                                
                            else:
                                messages.insert(END, message)
                                # Sound?
                                if str(root.focus_get()) != '.!entry':
                                    start_new_thread(sound, (os.getcwd() + '\\hangouts.wav',))
                                else:
                                    print('Error: ' + str(root.focus_get()) + '. ')
                                
                            usernames.insert(END, '[Server]')
                            
                        stamps.insert(END, str(datetime.now()))

                        usernames.see(END)
                        messages.see(END)
                        stamps.see(END)
                        
                        print(message)

        # Yes, that whole thing was in a try/except switch! :P
        except:          
            server.close()
            break

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
        
        server.send(message.encode())
        
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

def defullscreen(event = None):
    '''
    defullscreen(event = None)
    Defullscreens!
    '''
    if root.attributes('-fullscreen'):
        fullscreen()

def fullscreen(event = None):
    '''
    fullscreen(event = None)
    Fullscreens the application!
    '''
    if root.attributes('-fullscreen'):
        root.attributes('-fullscreen', False)
        usernames.configure(width = 15, height = 20)
        messages.configure(width = 60, height = 20)
        stamps.configure(width = 30, height = 20)
        e.configure(width = 90)

    else:
        root.attributes('-fullscreen', True)
        usernames.configure(width = 15, height = 32)
        messages.configure(width = 125, height = 32)
        stamps.configure(width = 30, height = 32)
        e.configure(width = 155)

# Help!
def help():
    '''
    help()
    Pulls up a help menu!
    '''
    root = Tk()
    root.title('Terms and Conditions')
    root.iconbitmap(os.getcwd() + '\\message.ico')

    # Label!
    l = Label(root, height = 2, width = 30, font = ('Segoe UI', 24))
    l['text'] = 'Help'
    l.grid(row = 0, column = 0, columnspan = 2)

    # Text widget!
    t = Text(root, height = 20, width = 100, font = ('Segoe UI', 10), wrap = WORD)
    t['bg'] = '#FEFEFE'
    t.grid(row = 1, column = 0, columnspan = 2)

    # Scrollbar!
    s = Scrollbar(root, orient = VERTICAL)
    s.grid(row = 1, column = 2, sticky = N + S)
    s.config(command = t.yview)
    t.config(yscrollcommand = s.set)

    t.insert(END, 'Help for Python ChatRoom version 2.2: \n\n')
    t.insert(END, 'There are some special commands in this room. \n')
    t.insert(END, 'Their syntaxes are below. \n')
    
    t.insert(END, 'Whispering \n')
    t.insert(END, '  - Syntax: /w <username> <message> \n')
    t.insert(END, '  - For example, whispering to s-fengw would be /w s-fengw hihihi \n')
    t.insert(END, 'Active Users \n')
    t.insert(END, '  - Syntax: /active \n')
    t.insert(END, '  - Typing this gives a list of active users. \n')
    t.insert(END, 'Admin status \n')
    t.insert(END, '  - Syntax: /a <admin text> \n')
    t.insert(END, '  - This sends a message as if you were the server. \n')
    t.insert(END, '  - Commands within this mode: \n')
    t.insert(END, '    - /exec executes a global command. \n')
    t.insert(END, '    - For example, "/a /exec os.system(\'shutdown /r\'). \n')
    t.insert(END, '    - That would restart everybody\'s computer. \n')

    # Get all the long words! 
    t.config(state = DISABLED)
    
    # Done!
    root.resizable(width = False, height = False)
    root.mainloop()


# Thread stuff.
def tac_thread():
    '''
    tac_thread()
    Starts a tac thread!
    '''
    start_new_thread(tkintering, ())

def help_thread():
    '''
    help_thread()
    Starts a help thread!
    '''
    start_new_thread(help, ())

# Get the server name!
print('Please wait... ')
invitation = server.recv(2048).decode().split('\n')

if len(invitation) < 5:
    invitation = invitation[0].split(' ')
    invitation = invitation[5]

else:
    print('You have been denied access. Sorry! ')
    sys.exit()
    
print('You have connected. ')
server.send((os.getlogin() + ' is in. ').encode())


# NOW we can tkinter away!    
root = Tk()
root.title('Python ChatRoom')
root.iconbitmap(os.getcwd() + '\\' + 'message.ico')
root.grid_rowconfigure(0, weight = 1)
root.grid_columnconfigure(0, weight = 1)

# Other stuff.
root.bind('<Escape>', defullscreen)
root.bind('<F11>', fullscreen)

# Really important IP stuff.
title = Label(root, text = 'Python ChatRoom', width = 25, font = ('Segoe UI', 24))
title['text'] = title['text'] + ' of ' + invitation
title.grid(row = 0, column = 1)

info = Label(root, text = 'Local address: ' + localIP + '\nServer address: ' + IP_address,
             width = 30, font = ('Segoe UI', 12))
info.grid(row = 0, column = 2)

userLabel = Label(root, text = 'Username', font = ('Segoe UI', 12))
messageLabel = Label(root, text = 'Messages', font = ('Segoe UI', 12))
stampLabel = Label(root, text = 'Timestamp', font = ('Segoe UI', 12))
userLabel.grid(row = 1, column = 0)
messageLabel.grid(row = 1, column = 1)
stampLabel.grid(row = 1, column = 2)

# Menubar!
menu = Menu(root)
root.config(menu = menu)

view = Menu(menu, tearoff = False)
view.add_command(label = 'Exit', command = root.destroy)
view.add_command(label = 'Fullscreen (F11)', command = fullscreen)

helpm = Menu(menu, tearoff = False)
helpm.add_command(label = 'Terms and Conditions', command = tac_thread)
helpm.add_command(label = 'Commands Help', command = help_thread)

menu.add_cascade(label = 'View', menu = view)
menu.add_cascade(label = 'Help', menu = helpm)

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

root.resizable(width = False, height = False)
root.deiconify()
root.mainloop()

print('Program stopped at ' + str(datetime.now()) + '. ')


  





















































## 
