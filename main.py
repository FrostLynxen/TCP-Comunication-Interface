# gui_client.py
import socket
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class TCPClientGUI:
    def __init__(self, master):
        self.master = master
        master.title("TCP/IP Chat Client")

        # Create a scrollable text area for displaying messages.
        self.chat_log = ScrolledText(master, state='disabled', width=60, height=20)
        self.chat_log.pack(padx=10, pady=10)

        # Entry widget for typing messages.
        self.entry_field = tk.Entry(master, width=50)
        self.entry_field.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))
        self.entry_field.bind("<Return>", lambda event: self.send_message())

        # Button to send messages.
        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=(10, 10), pady=(0, 10))

        # Set up the TCP client socket.
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_host = "192.168.1.120"  # Change as needed.
        self.server_port = 8500       # Change as needed.
        try:
            self.socket.connect((self.server_host, self.server_port))
        except Exception as e:
            self.append_message("Connection error: " + str(e))
            return

        self.running = True
        # Start a background thread to receive messages.
        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.daemon = True
        self.receive_thread.start()

    def send_message(self):
        message = self.entry_field.get()
        if message:
            try:
                self.socket.sendall(message.encode("utf-8"))
            except Exception as e:
                self.append_message("Send error: " + str(e))
            self.entry_field.delete(0, tk.END)

    def receive_messages(self):
        while self.running:
            try:
                data = self.socket.recv(1024)
                if data:
                    message = data.decode("utf-8")
                    self.append_message(message)
                else:
                    self.append_message("Disconnected from server.")
                    self.running = False
                    break
            except Exception as e:
                self.append_message("Receive error: " + str(e))
                self.running = False
                break

    def append_message(self, message):
        self.chat_log.config(state='normal')
        self.chat_log.insert(tk.END, message + "\n")
        self.chat_log.config(state='disabled')
        self.chat_log.yview(tk.END)

    def on_close(self):
        self.running = False
        try:
            self.socket.close()
        except Exception:
            pass
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    client_gui = TCPClientGUI(root)
    root.protocol("WM_DELETE_WINDOW", client_gui.on_close)
    root.mainloop()
