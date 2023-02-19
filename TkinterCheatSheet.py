#let's build a program with all the available widgets in TK with copy to clipboard buttons
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
root = tk.Tk()
root.title("Tkinter Cheatsheet by AgresszivKenomajas")


#Init setup, creating scrollable frame
class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self,width=650, height=800)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas, )

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw",)

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True,)
        scrollbar.pack(side="right", fill="y")

def dummyCommand(*args,**kwargs):
    pass
frame = ScrollableFrame(root)
frame.pack()


#Title

mainTitle = ttk.Label(frame.scrollable_frame,text="TK Cheatsheet",font=("Arial",20))
mainTitle.grid(row=1, column=2, padx=100, )
frame.scrollable_frame.columnconfigure(3, weight=1)
#***************************************
#           Clipboard content          *
#***************************************
def tkButtonCopy ():
    root.clipboard_clear()
    root.clipboard_append("""
button1 = tk.Button(
    root,
    text="button text",
    font=("Arial",10),
    width=12,
    height= 1,
    state="normal",
    command=lambda: print("Im a button"))
""")

def ttkButtonCopy ():
    root.clipboard_clear()
    root.clipboard_append("""
button1 = ttk.Button(
    root,
    text="button text",
    state="normal",
    command=lambda: print("Im a button"))
""")

def tkCheckButtonCopy():
    root.clipboard_clear()
    root.clipboard_append("""
Choice = tk.StringVar()
checkbox1 = tk.Checkbutton(root, text='Check button',
	    command=lambda:print("checkbox"), variable=Choice,
	    onvalue='On', offvalue='off')
    
    """)

def ttkCheckButtonCopy():
    root.clipboard_clear()
    root.clipboard_append("""
Choice = tk.StringVar()
checkbox1 = ttk.Checkbutton(root, text='Check button',
	    command=lambda:print("checkbox"), variable=Choice,
	    onvalue='On', offvalue='off')

    """)

def boilerPlateCopy():
    root.clipboard_clear()
    root.clipboard_append("""
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
root = tk.Tk()
root.title("Window Title Goes Here")

#your code goes here

if __name__ == "__main__":
    root.mainloop()
    """)

def tkRadioCopy():
    root.clipboard_clear()
    root.clipboard_append("""
RadioButtonChoice = tk.StringVar()
RadioButtonChoice.set('op1')
option1 = tk.Radiobutton(root, text='Option1', variable=RadioButtonChoice, value='op1')
option2 = tk.Radiobutton(root, text='Option2', variable=RadioButtonChoice, value='op2')
option3 = tk.Radiobutton(root, text='Option3', variable=RadioButtonChoice, value='op3')
    
    """)

def ttkRadioCopy():
    root.clipboard_clear()
    root.clipboard_append("""
RadioButtonChoice = tk.StringVar()
RadioButtonChoice.set('op1')
option1 = ttk.Radiobutton(root, text='Option1', variable=RadioButtonChoice, value='op1')
option2 = ttk.Radiobutton(root, text='Option2', variable=RadioButtonChoice, value='op2')
option3 = ttk.Radiobutton(root, text='Option3', variable=RadioButtonChoice, value='op3')

    """)

def tkEntryCopy():
    root.clipboard_clear()
    root.clipboard_append("""
entryVar = tk.StringVar()
entry1 = tk.Entry(root, textvariable=entryVar)    
    """)

def ttkEntryCopy():
    root.clipboard_clear()
    root.clipboard_append("""
entryVar = tk.StringVar()
entry1 = ttk.Entry(root, textvariable=entryVar)    
    """)

def comboboxCopy():
    root.clipboard_clear()
    root.clipboard_append("""combo = ttk.Combobox(root,
                     textvariable=combovar,
                     values= combolist,
                     state="normal") #state could also be disabled or readonly""")

def listboxCopy():
    root.clipboard_clear()
    root.clipboard_append("""
listboxFrame = tk.Frame(root) #separate frame needed
choiceslistbox = ["list", "goes", "here"]
choicesvar = tk.StringVar(value=choiceslistbox) #needs to convert list so tk could handle it
l = tk.Listbox(listboxFrame, listvariable=choicesvar)
l.pack(side="left", fill="both")
scrollbarListbox = ttk.Scrollbar(listboxFrame)
scrollbarListbox.pack(side="right", fill="both")
l.config(yscrollcommand = scrollbarListbox.set)
scrollbarListbox.config(command = l.yview)
listboxFrame.pack() #or grid """)

def scrollbarCopy ():
    root.clipboard_clear()
    root.clipboard_append("""
s = ttk.Scrollbar(root, orient="horizontal", command=lambda :print("scrollbar!"))
s.pack(fill="both") #example
""")

def textboxCopy ():
    root.clipboard_clear()
    root.clipboard_append("""
textboxFrame = tk.Frame(root) #separate frame needed for handling
t = tk.Text(textboxFrame, width=25, height=10)
t.pack(side="left", fill="both")
textboxScrollbar = ttk.Scrollbar(textboxFrame)
textboxScrollbar.pack(side="right", fill="both")
textboxScrollbar.config(command = t.yview)
t.config(yscrollcommand = textboxScrollbar.set)
textboxFrame.pack() #or grid..
""")

def tkScaleCopy():
    root.clipboard_clear()
    root.clipboard_append("""
s = tk.Scale(root, orient="horizontal", length=200, from_=1.0, to=100.0)
    """)

def ttkScaleCopy():
    root.clipboard_clear()
    root.clipboard_append("""
s = ttk.Scale(root, orient="horizontal", length=200, from_=1.0, to=100.0)
    """)

def tkSpinboxCopy():
    root.clipboard_clear()
    root.clipboard_append("""
spinval = tk.StringVar()
s = tk.Spinbox(root, from_=1.0, to=100.0, textvariable=spinval)
    """)

def ttkSpinboxCopy():
    root.clipboard_clear()
    root.clipboard_append("""
spinval = tk.StringVar()
s = ttk.Spinbox(root, from_=1.0, to=100.0, textvariable=spinval)
       """)

def progbarCopy():
    root.clipboard_clear()
    root.clipboard_append("""
p = ttk.Progressbar(root, orient="horizontal", length=200, mode='determinate', value=40)
       """)

def copyOpenFileDialog():
    root.clipboard_clear()
    root.clipboard_append("""
def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )

openfiledialogButton = ttk.Button(root,text="Open a file", command=select_file)
""")

def copyOpenFilesDialog():
    root.clipboard_clear()
    root.clipboard_append("""
def select_files():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected Files',
        message=filenames
    )

openfiledialogButton = ttk.Button(root,text="Open a file", command=select_files)
""")
#***************************************
#           Sample widgets             *
#***************************************
#Boilerplate
boilerplateButton = ttk.Button(frame.scrollable_frame,text="Copy boilerplate", command=boilerPlateCopy)
boilerplateButton.grid(row=1,column=1)
#tk button
frame.scrollable_frame.rowconfigure(2, weight=1)
buttonLabel = tk.Label(frame.scrollable_frame, text="TK button")
buttonLabel.grid(row=2, column=1)
tkbutton = tk.Button(frame.scrollable_frame,text="I'm a tk button")
tkbutton.grid(row=2,column=2,  pady=40)
tkbuttoncopy = ttk.Button(frame.scrollable_frame, text="Copy to clipboard", command=tkButtonCopy)
tkbuttoncopy.grid(row=2,column=3)


#ttk button
frame.scrollable_frame.rowconfigure(3, weight=1)
buttonLabel = tk.Label(frame.scrollable_frame, text="Ttk button")
buttonLabel.grid(row=3, column=1)
tkbutton = ttk.Button(frame.scrollable_frame,text="I'm a ttk button")
tkbutton.grid(row=3,column=2,  pady=40)
ttkbuttoncopy = ttk.Button(frame.scrollable_frame, text="Copy to clipboard", command=ttkButtonCopy)
ttkbuttoncopy.grid(row=3,column=3)


#TK checkbutton
Choice = tk.StringVar()
checkboxLabel = tk.Label(frame.scrollable_frame,text="TK Checkbox")
checkboxLabel.grid(row=4, column=1)
checktk = tk.Checkbutton(frame.scrollable_frame, text='Check button',
	    command=dummyCommand, variable=Choice,
	    onvalue='On', offvalue='off')
checktk.grid(row=4, column=2,  pady=40)
tkcheckbuttoncopy = ttk.Button(frame.scrollable_frame,text="Copy to clipboard", command=tkCheckButtonCopy)
tkcheckbuttoncopy.grid(row=4,column=3, )


#TtK checkbutton
ttkChoice = tk.StringVar()
checkboxLabel2 = tk.Label(frame.scrollable_frame,text="TtK Checkbox")
checkboxLabel2.grid(row=5, column=1)
checkttk = ttk.Checkbutton(frame.scrollable_frame, text='Check button',
	    command=dummyCommand, variable=ttkChoice,
	    onvalue='On', offvalue='off')
checkttk.grid(row=5, column=2,  pady=40)
ttkcheckbuttoncopy = ttk.Button(frame.scrollable_frame,text="Copy to clipboard",command=ttkCheckButtonCopy)
ttkcheckbuttoncopy.grid(row=5,column=3)


#tk radio button
tkradioFrame = tk.Frame(frame.scrollable_frame)
tkradioFrame.grid(row=6, column=2,  pady=40)
tkRadioLabel = tk.Label(frame.scrollable_frame, text="TK radio buttons")
tkRadioLabel.grid(row=6,column=1)
tkRadio = tk.StringVar()
tkRadio.set('op1')
option1tkr = tk.Radiobutton(tkradioFrame, text='Option1', variable=tkRadio, value='op1')
option2tkr = tk.Radiobutton(tkradioFrame, text='Option2', variable=tkRadio, value='op2')
option3tkr = tk.Radiobutton(tkradioFrame, text='Option3', variable=tkRadio, value='op3')
option1tkr.grid(row=1, column=1, padx=20)
option2tkr.grid(row=2, column=1, padx=20)
option3tkr.grid(row=3, column=1, padx=20)
tkradiocopybutton = ttk.Button(frame.scrollable_frame,text="Copy to clipboard",command=tkRadioCopy)
tkradiocopybutton.grid(row=6,column=3)


#ttk radio button
ttkradioFrame = tk.Frame(frame.scrollable_frame)
ttkradioFrame.grid(row=7, column=2, pady=40)
ttkRadioLabel = tk.Label(frame.scrollable_frame, text="TTK radio buttons")
ttkRadioLabel.grid(row=7,column=1)
ttkRadio = tk.StringVar()
ttkRadio.set('op1')
option1ttkr = tk.Radiobutton(ttkradioFrame, text='OptionA', variable=ttkRadio, value='op1')
option2ttkr = tk.Radiobutton(ttkradioFrame, text='OptionB', variable=ttkRadio, value='op2')
option3ttkr = tk.Radiobutton(ttkradioFrame, text='OptionC', variable=ttkRadio, value='op3')
option1ttkr.grid(row=1, column=1, padx=40)
option2ttkr.grid(row=2, column=1, padx=20)
option3ttkr.grid(row=3, column=1, padx=20)
tkradiocopybutton = ttk.Button(frame.scrollable_frame,text="Copy to clipboard",command=ttkRadioCopy)
tkradiocopybutton.grid(row=7,column=3)


#tk entry
username = tk.StringVar()
entrylabel = tk.Label(frame.scrollable_frame, text="TK Entry")
entrylabel.grid(row=8, column=1)
name = tk.Entry(frame.scrollable_frame, textvariable=username)
name.grid(row=8, column=2, pady=40)
tkEntryCopyButton = ttk.Button(frame.scrollable_frame, text="Copy to clipboard", command=tkEntryCopy)
tkEntryCopyButton.grid(row=8,column=3)


#ttk entry
username2 = tk.StringVar()
entrylabel = tk.Label(frame.scrollable_frame, text="TTK Entry")
entrylabel.grid(row=9, column=1)
name = ttk.Entry(frame.scrollable_frame, textvariable=username2)
name.grid(row=9, column=2, pady=40)
ttkEntryCopyButton = ttk.Button(frame.scrollable_frame, text="Copy to clipboard", command=ttkEntryCopy)
ttkEntryCopyButton.grid(row=9,column=3)


#combo box
comboboxLabel = tk.Label(frame.scrollable_frame, text="Combo box")
comboboxLabel.grid(row=10, column=1)
combolist = ["one", "two", "three", "four", "five"]
combovar = tk.StringVar()
combo = ttk.Combobox(frame.scrollable_frame, textvariable=combovar, values= combolist)
combo.grid(row=10,column= 2, pady=40)
comboboxCopyButton = ttk.Button(frame.scrollable_frame, text="Copy to clipboard", command=comboboxCopy)
comboboxCopyButton .grid(row=10,column=3)


#listbox
listboxLabel = tk.Label(frame.scrollable_frame, text="Listbox with scrollbar")
listboxLabel.grid(row=11, column=1)
listboxFrame = tk.Frame(frame.scrollable_frame)
listboxFrame.grid(row=11, column=2,pady=40)
choiceslistbox = ["apple", "orange", "banana","pear","pineapple", "figs", "walnut","almond", "plum","grapes","kiwi","papaya","avocado","mango"]
choicesvar = tk.StringVar(value=choiceslistbox)
l = tk.Listbox(listboxFrame, listvariable=choicesvar)
l.pack(side="left", fill="both")
scrollbarListbox = ttk.Scrollbar(listboxFrame)
scrollbarListbox.pack(side="right", fill="both")
l.config(yscrollcommand = scrollbarListbox.set)
scrollbarListbox.config(command = l.yview)
listboxCopyButton= ttk.Button(frame.scrollable_frame,text="Copy to clipboard",command=listboxCopy)
listboxCopyButton.grid(row=11, column=3)


#scrollbar
scrollbarLabel = tk.Label(frame.scrollable_frame, text="Scrollbar")
scrollbarLabel.grid(row=12, column=1)
s = ttk.Scrollbar( frame.scrollable_frame, orient="horizontal", command=dummyCommand)
s.grid(row=12, column=2, pady=40)
scrollbarButton= ttk.Button(frame.scrollable_frame,text="Copy to clipboard",command=scrollbarCopy)
scrollbarButton.grid(row=12, column=3)

#text
textlabel= tk.Label(frame.scrollable_frame,text="text")
textlabel.grid(row=13,column=1)
textboxFrame = tk.Frame(frame.scrollable_frame) #separate frame needed for handling
t = tk.Text(textboxFrame, width=25, height=10)
t.pack(side="left", fill="both")
textboxScrollbar = ttk.Scrollbar(textboxFrame)
textboxScrollbar.pack(side="right", fill="both")
textboxScrollbar.config(command = t.yview)
t.config(yscrollcommand = textboxScrollbar.set)
textboxFrame.grid(row=13, column=2,pady=40)
textboxButton= ttk.Button(frame.scrollable_frame, text="Copy to clipboard", command=textboxCopy)
textboxButton.grid(row=13,column=3)


#TK scale
scaleLabel= tk.Label(frame.scrollable_frame, text="TK Scale")
scaleLabel.grid(row=14, column=1)

s = tk.Scale(frame.scrollable_frame, orient="horizontal", length=200, from_=1.0, to=100.0)
s.grid(row=14,column=2, pady=40)
tkscaleCopyButton= ttk.Button(frame.scrollable_frame,text="Copy to clipboard", command=tkScaleCopy)
tkscaleCopyButton.grid(row=14,column=3)
#TTK scale
scaleLabel2= tk.Label(frame.scrollable_frame, text="TTK Scale")
scaleLabel2.grid(row=15, column=1)
s2 = ttk.Scale(frame.scrollable_frame, orient="horizontal", length=200, from_=1.0, to=100.0)
s2.grid(row=15,column=2, pady=40)
ttkscaleCopyButton= ttk.Button(frame.scrollable_frame,text="Copy to clipboard", command=ttkScaleCopy)
ttkscaleCopyButton.grid(row=15,column=3)


#TK spinbox
tkspinlabel= tk.Label(frame.scrollable_frame,text="TK spinbox")
tkspinlabel.grid(row=16, column=1)
spinval = tk.StringVar()
s = tk.Spinbox(frame.scrollable_frame, from_=1.0, to=100.0, textvariable=spinval)
s.grid(row=16,column=2, pady=40)
tkSpinboxCopyButton =ttk.Button(frame.scrollable_frame,text="Copy to clipboard", command=tkSpinboxCopy)
tkSpinboxCopyButton.grid(row=16,column=3)


#TTK spinbox
ttkspinlabel= tk.Label(frame.scrollable_frame,text="TTK spinbox")
ttkspinlabel.grid(row=17, column=1)
spinval2 = tk.StringVar()
s2 = ttk.Spinbox(frame.scrollable_frame, from_=1.0, to=100.0, textvariable=spinval2)
s2.grid(row=17,column=2, pady=40)
ttkSpinboxCopyButton =ttk.Button(frame.scrollable_frame,text="Copy to clipboard", command=ttkSpinboxCopy)
ttkSpinboxCopyButton.grid(row=17,column=3)

#Progressbar
tkprogbarlabel = tk.Label(frame.scrollable_frame, text="Progressbar")
tkprogbarlabel.grid(row=18,column=1)
p = ttk.Progressbar(frame.scrollable_frame, orient="horizontal", length=200, mode='determinate', value=40)
p.grid(row=18,column=2,pady=40)
progbarCopyButton =ttk.Button(frame.scrollable_frame,text="Copy to clipboard", command=progbarCopy)
progbarCopyButton.grid(row=18,column=3)

#open file dialog
openfiledialoglabel = tk.Label(frame.scrollable_frame, text="Open file dialog")
openfiledialoglabel.grid(row=19,column=1)
def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )

openfiledialogButton = ttk.Button(frame.scrollable_frame,text="Open a file", command=select_file)
openfiledialogButton.grid(row=19,column=2,pady=40)
copyOpenFileDialogButton= ttk.Button(frame.scrollable_frame,text="Copy to clipboard", command=copyOpenFileDialog )
copyOpenFileDialogButton.grid(row=19, column=3)

#open files dialog
openfilesdialoglabel = tk.Label(frame.scrollable_frame, text="Open files dialog")
openfilesdialoglabel.grid(row=20,column=1)
def select_files():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected Files',
        message=filenames
    )
openfilesdialogButton = ttk.Button(frame.scrollable_frame,text="Open files", command=select_files)
openfilesdialogButton.grid(row=20,column=2,pady=40)
copyOpenFilesDialogButton= ttk.Button(frame.scrollable_frame,text="Copy to clipboard", command=copyOpenFilesDialog )
copyOpenFilesDialogButton.grid(row=20, column=3)

if __name__ == "__main__":
    root.mainloop()