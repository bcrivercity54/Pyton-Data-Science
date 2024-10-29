from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from openpyxl import Workbook
import openpyxl
#import sleep

# create the root window
root = tk.Tk()
root.title('Tkinter File Dialog')
root.resizable(False, False)
root.geometry('500x550')


fileList = []

def select_files():
    filetypes = (('Work Instructions files', '*.xlsx'),('All files', '*.*'))   

    path = fd.askopenfilenames(title='Open files',initialdir='C:\\Users\\brian\Documents\\Spreadsheets\\Work_Instructions\\GE_HC_OEM',filetypes=filetypes)
    #print("file type",type(filetypes))
    #print(path)
    fileList.append(path)
    #print(type(fileList))
    #returnSelectedWorkInstructions(fileList)
    #showinfo(title='Selected Files',message=filenames)

    for i in fileList:
        file = i
        #print("file",file)
        findMissedSignOffs(file)
        #print(file)
       

def findMissedSignOffs(fileList):
    
    outStringList = []
    
    for x in fileList:
        #print("x",x)
        
        wb = openpyxl.load_workbook(x, read_only=False)
        ws = wb.active
##
        for row in ws.iter_rows(2):
             for cell in row:
                 #print("cell value",cell.value)
                 if cell.value == "Tech Initial:" and cell.offset(row=0, column=1).value is  None:
                     print("cell value",cell.value)
                     #rowNum ="row("+row+")"
                     rowNum = str((row[0:1]))
                     sRowNum = rowNum.replace("<Cell 'Sheet1'.",'')
                     sRowNum = sRowNum.replace(">,",'')
                     print("Row num",sRowNum)
                     #print(row,cell.value,cell.offset(row=0, column=1).value)
                     outStringList.append(sRowNum) #label.config(text=sRowNum, font=('Courier 13 bold'))
                     updateOutLabel(outStringList)

def updateOutLabel(inList):

    var =StringVar()
    var.set("Results")
    #print("i",i)
    l = Label(root,textvariable = var)
    l.pack()
     
    for i in inList:
        #sleep(1)
        var.set(i)
        root.update_idletasks()
        
       
    
##
##   txt= file.read()
##   label.config(text=txt, font=('Courier 13 bold'))
    
# open button
open_button = ttk.Button(root,text='Open Files',command=select_files)
open_button.place(x=200,y=5)                         


open_button.pack(expand=True)
label= Label(root,text="test ", font=('Courier 13 bold'))
label.place(x=100,y=100)
label.pack()

root.mainloop()
