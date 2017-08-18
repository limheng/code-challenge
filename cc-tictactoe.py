from tkinter import *

def clearMoves():
    global moves
    global xoro
    moves['O'] = set()
    moves['X'] = set()
    xoro = 'O'

def buttonsAll(onoroff = False, clear = False):
    for but in buttons:
        if clear:
            but['text'] = ''
            but['bg'] = 'SystemButtonFace'
        but['state'] = 'normal' if onoroff else 'disabled'
    label2['text'] = 'Welcome! Goodluck!'

def onWin(winning):
    for i in winning:
        buttons[i]['bg'] ='yellow'
    buttonsAll()
    clearMoves()
    return True

def checkWon(arr):
    win = [{0,1,2},{0,3,6},{0,4,8},{3,4,5},{6,7,8},{1,4,7},{2,5,8},{2,4,6}]
    if len(arr) > 2:
        for x in win:
            sect = arr & x
            if len(sect) > 2:
                return onWin(x)
    if len(arr) > 4:
        label2['text'] = 'No Winners! Try Again?'
    return False

def onClick(i):
    # global buttons
    global xoro
    buttons[i]['text'] = xoro
    button['state'] = 'normal'
    buttons[i]['state'] = 'disabled'
    moves[xoro].add(i)
    if checkWon(moves[xoro]):
        label2['text'] = '{} Wins! Try Again?'.format(xoro)
    else:
        xoro = 'X' if xoro == 'O' else 'O'

def onRestart(event):
    clearMoves()
    buttonsAll(True, True)
    button['state'] = 'disabled'


buttons = []
xoro = 'O'
moves = dict()
clearMoves()

row = [0,0,0,1,1,1,2,2,2]
col = [0,1,2,0,1,2,0,1,2]

win = Tk()

label = Label(win, text='Tic Tac Toe', font = "Verdana 20 bold italic")
label.pack()
button = Button(win, text='Restart', font = "Verdana 10", state='disabled')
button.bind('<Button-1>', onRestart)
button.pack(side=BOTTOM)
label2 = Label(win, text='Welcome! Good Luck!', font = "Verdana 10")
label2.pack(side=BOTTOM)
frame = Frame(win)
frame.pack()

for i in range(9):
    but = Button(frame, text='', font = "Verdana 20 bold", command=lambda i=i: onClick(i), width=4, height=2)
    but.grid(row=row[i], column=col[i])
    buttons.append(but)

win.mainloop()
