TCP Echo Server and Tkinter GUI TCP Client
This project demonstrates a basic TCP/IP echo server and a simple GUI-based TCP client built using Python and Tkinter. The server listens for incoming connections, receives messages, and echoes them back. The client connects to the server, allows the user to type messages, and displays both sent and received messages in a scrollable text area.

Echo Server:
Listens on a specified host and port.
Receives data from a client and echoes the same data back.

GUI Client:
Built with Tkinter, featuring a scrollable chat log.
Provides an input field and send button for user messages.
Runs a background thread to receive messages asynchronously.
Displays messages in real time.

Requirements
Python 3.x
Tkinter (usually bundled with Python, but ensure it is installed on your system)
A basic understanding of sockets and GUI programming in Python

Files
main_server.py
Contains the server code that sets up a TCP socket, listens for a connection, and echoes any received message.

main.py
Contains the client code that creates a Tkinter-based GUI. It connects to the server, sends messages typed by the user, and displays any messages received from the server.
