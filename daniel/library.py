import tkinter as tk
import pandas as pd
import numpy as np
import random
from tkinter import *
from tkinter import ttk
from datetime import datetime
import tkinter.messagebox

class library(tk.Frame):

    def __init__(self, root):
        # create the application
        self.root = root

        # method calls to window manager class
        self.root.title("Rugutt's Library Database Manager")
        self.root.geometry("1280x720+0+0")
        self.root.configure(background='powder blue')

        #========Frame==========#
        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, width=1280, padx=20, bd=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, width=39, font=(
            'arial', 40, 'bold'), text="\tRugutt's Library Management Systems\t", padx=12)
        self.lblTitle.grid()

        ButtonFrame = Frame(MainFrame, bd=20, width=1280,
                            height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail = Frame(MainFrame, bd=20, width=1280,
                            height=50, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=20, width=1230,
                          height=400, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=10, width=800, height=300, padx=20, relief=RIDGE, font=(
            'arial', 12, 'bold'), text="Library Membership Info:",)
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=10, width=450, height=300, padx=20, relief=RIDGE, font=(
            'arial', 12, 'bold'), text="Book Details:",)
        DataFrameRIGHT.pack(side=RIGHT)

        #========Widget==========#
        self.lblMemberType = Label(DataFrameLEFT, font=(
            'arial', 12, 'bold'), text="Member Type:", padx=2, pady=2)
        self.lblMemberType.grid(row=0, column=0, sticky=W)

        self.cboMemberType = ttk.Combobox(DataFrameLEFT, font=(
            'arial', 12, 'bold'), state='readonly', width=23)
        self.cboMemberType['value'] = (
            '', 'Student', 'Lecturer', 'Admin Staff')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=0, column=1)

        self.lblBookID = Label(DataFrameLEFT, font=(
            'arial', 12, 'bold'), text="Book ID:", padx=2, pady=2)
        self.lblBookID.grid(row=1, column=0, sticky=W)
        self.lblBookID = Entry(DataFrameLEFT, font=(
            'arial', 12, 'bold'), width=25)
        self.lblBookID.grid(row=1, column=1)
        
        print(sys.version)
        np_test = np.arange(9)
        print(np_test)
        
        dict = {list:["A", "B", "C", "D", "E"]}
        pd_test = pd.DataFrame(dict)
        print(np_test)

if __name__ == '__main__':
    root = Tk()
    application = library(root)
    root.mainloop()
