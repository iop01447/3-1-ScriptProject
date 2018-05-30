# imports
# Use Tkinter for python 2, tkinter for python 3
import tkinter as tk
import tkinter.scrolledtext as tkst
import tkinter.messagebox as tkmb
from tkinter import ttk
# Define a ManagerApp class
class ManagerApp(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.connection = None
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.labelReader = ttk.Label(self, text='Reader')
        self.labelReader.grid(column=0, row=0)

        self.reader_name = tk.StringVar()  # String variable
        self.comboReader = ttk.Combobox(self, width=30, state='readonly'
                                        , textvariable=self.reader_name)  # Create a combobox
        self.comboReader.grid(column=1, row=0)
        self.comboReader['values'] = readers()
        try:
            self.comboReader.current(0)
        except:
            pass

        self.buttonReset = ttk.Button(self, text='Reset...', command=self.clickReset)  # Create a button
        self.buttonReset.grid(column=2, row=0)

        self.stLog = tkst.ScrolledText(self, width=50, height=20, wrap=tk.WORD)  # Create a scrolledtext
        self.stLog.grid(column=0, row=1, columnspan=3)

        self.entryCommand = tk.Entry(self, width=40)  # Create a entry
        self.entryCommand.grid(column=0, row=2, columnspan=2)
        self.entryCommand.focus_set()

        self.buttonCommand = ttk.Button(self, text='Send...', command=self.clickSend)  # Create a button
        self.buttonCommand.grid(column=2, row=2)

    # Click a reset button
    def clickReset(self):
        if self.connection is not None:
            self.connection.disconnect()
            self.connection = None

        try:
            for r in readers():
                if r.name == self.reader_name.get():
                    self.connection = r.createConnection()
                    self.connection.connect()
                    self.stLog.insert(tk.END, 'ATR: '
                                      + toHexString(self.connection.getATR()) + '\n')
                    self.stLog.see(tk.END)
                    break
        except:
            tkmb.showinfo('Error', 'Please check a card or readers...')

    # Click a send button
    def clickSend(self):
        apdu = toBytes(self.entryCommand.get())
        response, sw1, sw2 = self.connection.transmit(apdu)
        # print('response: ', response, ' status words: ', "%x %x" % (sw1, sw2))
        capdu = '< ' + toHexString(apdu) + '\n'
        rapdu = ('> ' + toHexString(response) + '\n> {:02X}'.format(sw1)
                 + ' {:02X}'.format(sw2) + '\n')
        self.stLog.insert(tk.END, capdu + rapdu)
        self.stLog.see(tk.END)

        if (sw1 == 0x61):  # Get Response
            getResponse = '00C00000' + '{:02X}'.format(sw2)
            apdu = toBytes(getResponse)
            response, sw1, sw2 = self.connection.transmit(apdu)
            # print('response: ', response, ' status words: ', "%x %x" % (sw1, sw2))
            capdu = '< ' + toHexString(apdu) + '\n'
            rapdu = ('> ' + toHexString(response) + '\n> {:02X}'.format(sw1)
                     + ' {:02X}'.format(sw2) + '\n')
            self.stLog.insert(tk.END, capdu + rapdu)
            self.stLog.see(tk.END)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Manager')  # Add a title
    ManagerApp(root).pack(side="top", fill="both", expand=True)

    root.resizable(0, 0)  # Disable resizing the GUI
    root.mainloop()  # Start GUI