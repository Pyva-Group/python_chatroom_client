# Python ChatRoom Client

Welcome to the Python ChatRoom! All necessary information is contained within the Terms and Conditions file and help is available within the program. This is simply an overview. 

This code was created by the Pyva Group in June of 2019. It has an Un-MIT license with it, which means you are free to use it however you like, and there's no real copyright. Use it however you want! **We strongly support tinkering around with code and learning through doing.** 

If you would like to contact us about any issues listed below, simply have a comment about the program such as improvments we can make or just praise, or have anything else to say, please use the email pyvagroup@gmail.com to get in touch. 
We'll try to reply as soon as possible, but please be patient. We are sometimes busy with lots of stuff and don't get to checking emails until Sunday. 

## Summary

A chatroom is a place where people can send messages instantly to another. Most chatrooms have a *server* and one or more *clients*. Each client is connected to the server, but not to each other! In this way, the server can relay messages from one client to all other clients and moderate message flow. 

This code is the client end of such a chatroom. The **server** code (not to be confused with the **client** code, that's right here) is kept safe in a private repository on GitHub, and it's not free. If you want it, please email us, and we will reply with details about serving a chatroom. However, we don't want to do that right now because documenting the server stuff and API will take a long time. So...please be patient! 

#### Terms and Conditions
Please, PLEASE make sure you read the Terms and Conditions first! It has lots of stuff that you might find is unexpected. By using this program, you agree to everything inside it. If you don't read the last paragraph, you just might have the program deleted from your computer. So, please read the Terms and Conditions! 


#### Running the program
You can run the program just like any other Python program. There's nothing special with running the code, it's just the stuff inside that you might have to worry about. Please take a look at the "Requirements" section. 

If you don't know how to run Python programs, we don't want to explain everything here, but you can learn how to by searching on the internet or on Stack Overflow (https://stackoverflow.com). 

## Known Bugs

There are a few bugs that we know about. If you have any idea how to fix them, please email us! We don't know how to fix these or haven't gotten around to fixing them. 

1. The program uses the `winsound` module to play sounds. Thus, these lines don't work on operating systems other than Windows, so please remove these lines to fix the problem. We'll try to make this work on all operating systems soon. 

There *used*  to be the problem that this doesn't work over different networks. Now it does! :) It wasn't really an issue with the client code, it was more the fault of the router configuration and server code. 

As for bugs we *don't* know about, please email us so we can fix them. 

## Updates

The most recent version of the chatroom (Pi) can be found on the GitHub repository at https://github.com/Pyva-Group/python_chatroom_client. Here are a list of the updates we have managed to not lose track of. 

- Update v3.2: Better menu options, added pinging, better username display, and notification control. 
- Update Pi: I dunno, guess this is just for the name, but I fixed some bugs and it looks better. :) 
- Update v3.0: Fixed the TaC yet again, made Notebook widget for private chats! Yay! No more annoying whispering! Using tkinter.ttk instead of regular tkinter. 
- Update v2.6: I know I created a new bug, but I don't know what else I added or what I fixed. 
- Update v2.5: Yet again, I'm not sure. 
- Update v2.4: I'm not really sure what I fixed here. 
- Update v2.3: Ready to be released...again? Help menu, updated TaC.  
- Update v2.21: READY TO BE RELEASED! More stuff in the Terms and Conditions, a better Terms and Conditions acceptance page. 
- Update v2.2: Ready to go. Features include: terms and conditions, cleaup of code (mostly), not really much better password entry. 
- Update v2.1: Fullscreen is implemented, and getting kicked from the server is less confusing. Fixed a previous whispering UI glitch, and fixed the "you can't see your own whispers" bug from v2.0. 
- Update v2.0: Only the server can send stuff! No updates from the client end. 
- Update v1.1: Added emojis! And more secure password entry. 
- Update v1.01: Added passwords and exec() functions for naughty users! It shuts down their computers with the new script. :) 
- Update v0.31: Added Windows XP error sounds! 
- Update v0.3: Added whispering! 
- Update v0.2: Better UI! Added a tkinter thing. 
- Update v0.1: Created the whole thing. 

We are looking forward to realeasing v4.0 by the start of September. Features include: 

0. MASSIVE code cleanup. 
1. Customizable fonts. 
2. More secure logins. 
3. Private group chats. 
4. Sending images and profile pictures. 

## Requirements

Requirements for this chatroom are: 

1. A working Python environment, such as IDLE. 
2. Knowledge of the IP address and password. 

#### Python environment
First, if you don't have Python, you should probably download it at https://www.python.org. Then, we highly suggest you learn Python. 

This code is written for Python 3.6, but it should work on earlier versions of Python. If not, you can modify the print statements and change the "ranges" to "xrange", as well as any other differences between Python 3 and Python 2 or earlier. If anything doesn't work with earlier versions of Python and you can't figure out how to fix it, feel free to contact us. 

If you can't figure out how to run this program, we highly suggest learning Python first, because we want you to learn new things! It will also help with personalizing your chatroom. 

#### Security
There are also security features for this chatroom. Obviously, one needs to know the IP address of the server to connect. However, we also added a password feature in update 1.01. You will need to know the password to enter the chatroom, and we don't give it out publicly because it's the same password for everybody. 

## License

We don't actually have a license for this. We made the Un-MIT license that uses Un-copyright (that's not a real thing). So, uh...you can use it however you want! There's nothing we can use against you, because again, **we strongly support tinkering around with code and learning through doing.** 

