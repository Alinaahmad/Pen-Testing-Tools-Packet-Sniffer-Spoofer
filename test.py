import tkinter as tk
import os

class PenTest(tk.Frame):
   def __init__(self, parent):
       tk.Frame.__init__(self, parent)
       self.parent = parent
       self.initialize_user_interface()

   def initialize_user_interface(self):
       self.parent.geometry("1300x600")
       self.parent.title("Pen Testing Tools and Packet Sniffer")
       self.entry=tk.Entry(self.parent)
       self.parent['background']='turquoise'
       
       a=tk.Label(self.parent, text="Pen Testing Tools and Packet Sniffer", font=("Castellar", 24))
       a.grid(row=1,column=2,pady=5)
     
       b=tk.Label(self.parent, text="Please, Choose one of the options below:", font=("Corbel", 16))
       b.grid(row=7, column=1,pady=50)
       
       c=tk.Button(self.parent, text="Packet Sniffer", command=self.PS, height=2, width=35)
       c.grid(row=8,column=2)
       
       d=tk.Button(self.parent, text="Ping Sweep Port Scanner", command=self.PingSweepPS, height=2, width =40)
       d.grid(row=10,column=2,pady=50)
       
       e=tk.Button(self.parent, text="Multi-Threaded Port Scanner", command=self.MultithreadPS, height=2, width =35)
       e.grid(row=12,column=2,padx=50)
       
       f=tk.Button(self.parent, text="Exit",command=self.parent.destroy, height=2, width=8, bg="red")
       f.grid(row=100,column=2)

       g=tk.Label(self.parent, text="Credits: \n\nAlina - A2305217603 \n  Naman Jain - A2305217581 \n Mehul Singh - A2305217XXX", bg='skyblue')
       g.grid(row=30,column=4,sticky=tk.S+tk.W)
       
       
   def PS(self):
       import TCP_sniffer
       os.system('TCP_sniffer.py')

   def PingSweepPS(self):
       import ping_sweep
       os.system('ping_sweep.py')

   def MultithreadPS(self):
       import ThreadedPortScanner
       os.system('ThreadedPortScanner.py')


if __name__ == '__main__':

   root = tk.Tk()
   run = PenTest(root)
   root.mainloop()
