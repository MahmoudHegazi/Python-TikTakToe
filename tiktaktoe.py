import tkinter as tk
root= tk.Tk()


# copy right PythonKing, can use only in your products not allowed developer or own for selling another version of this library without permession

#important to pass the async arugment (event_target_prop) within the drawing loop, that used latter in the callback any time in app lifetime
from functools import partial
# called the ez grid tkinter py
index = 0
btns = {}
dic = {}
# this dynamic function can draw any number of grid, in html grid is max 12 but here grid max unlimted contrled with width, height you as native match use the valid height, w=width/2, width=50, this how size handled can accept all sizes fit with cells, and cols, and add dynamic custom callback using partials you control, it and get the event listener target class in your cb !!before simplest way to draw grid unlimited rows, col3 , cols can automated to
def dynamicGridDraw(total_rows=3, total_col=3, width=75, h=0, height=50, clickCB=lambda: None):
    global index
    global btns
    # me and html grid reached same consipet must be max size for rows in the grid, currently is 3 max you can have from unlimit rows, and until 3 max cells , can be 1,2,3,0, in future will increased to 12 but unlike grid 12 and unlimited rows
    # next level control the canvas height and width to fit dynamic shape, sure for tkinter must be limit, or make size very small but require math to know the valid arugment 25, 50 for height
    canvas1 = tk.Canvas(root, width = width*3, height = (h*total_rows)+h, scrollregion=(0,0,0,int((h*total_rows)+h)))

    table_frame = tk.Frame(canvas1, pady=10, padx=5, background="yellow")
    vsb = tk.Scrollbar(root, orient="vertical", command=canvas1.yview, )
    canvas1.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas1.pack(side="top", fill="both", expand=True)
    canvas1.create_window((4,4), window=table_frame, anchor="nw")
    
    #canvas1.pack()
    for r in range(total_rows):        
        for i in range(total_col):
            if i == 0:
                rc_string = 'row{}-{}'.format(r, i)
                button1 = tk.Button(text='', command=partial(clickCB,rc_string), bg='brown',fg='white', font=('helvetica', 15, 'bold'))
                # add even data (need create event data returned cp
                btns[rc_string] = {'target': button1, 'row': r, 'col': i, 'w': width/2, 'h': h, 'width': width, 'height': height, 'meta': []}
                canvas1.create_window(int(width/2), h, window=button1, width=width, height=height)
                # w
            if i == 1:
                rc_string = 'row{}-{}'.format(r, i)
                button1 = tk.Button(text='', command=partial(clickCB,rc_string), bg='brown',fg='white', font=('helvetica', 15, 'bold'))
                btns[rc_string] = {'target': button1, 'row': r, 'col': i, 'w': width/2, 'h': h, 'width': width, 'height': height, 'meta': []}
                canvas1.create_window(int(width/2)*3, h, window=button1, width=width, height=height)
                # w * 3
            if i == 2:
                rc_string = 'row{}-{}'.format(r, i)
                #must int as python deep match so will return bigger numb /2 and in multiple 2 int good, also tkinter need simple 1 , 1,22
                button1 = tk.Button(text='', command=partial(clickCB,rc_string), bg='brown',fg='white', font=('helvetica', 15, 'bold'))                
                btns[rc_string] = {'target': button1, 'row': r, 'col': i, 'w': width/2, 'h': h, 'width': width, 'height': height, 'meta': []}
                canvas1.create_window(int(width/2)*5, h, window=button1, width=width, height=height)
                # w * 5
            index += 1
        h += 50
    print('hello')
    print(dic)



# here developer code for create game and use grid drawer, eg tiktaktoe, dynamicGridDraw(total_rows=3, total_col=3, width=75, h=50, height=50, clickCB=clickEventListener)
# dynamicGridDraw(total_rows=3, total_col=3, width=40, h=50, height=50, clickCB=clickEventListener) ledo, chess when complete max 12grid
# x in this simple eg fast, start first so who need x will start first players decide

x = True
plays = []
def clickEventListener(rc_string):
    global x
    currentPlay = 'X'
    if x == True:
        # current play x
        currentPlay = 'X'
        x = False
        
    else:
        # current play o
        currentPlay = 'O'
        x = True

    print(currentPlay)
    # the asynco part ez set the key value when player play
    btns[rc_string]['target'].config(text=currentPlay)
    # set meta to target ez with grid drawer lol max would tkinter grid do was draw gui dynamic for new games use meta tkinter grid custom
    btns[rc_string]['meta'].append({'play': currentPlay})

    plays.append(btns[rc_string])
    print(verify_win(plays))
    #print(btns[rc_string])

wins = [
      [((1,2),(5,4),(7,8),)],
      [((1,2),(5,4),(7,8),)]
    ]
#python king not need magicbox maybe later he read it while understanding logic and provide solution for performance only
t = [
       [(0,0,),(1,1,),(2,2,)],
       [(2,0,),(1,1,),(0,2,)]

    ]
#       [(0,2),(1,1),(2,0)]
# the idea  basicest need the 3 check and empty
def verify_win(plays):
    x_l = []
    o_l = []
    for item in plays:
        if item['meta'][0]['play'] == 'X':
            x_l.append((item['row'],item['col'],))

        if item['meta'][0]['play'] == 'O':
            o_l.append((item['row'],item['col'],))
            
    x_can_win = len(x_l) >= 3
    o_can_win = len(o_l) >= 3

    # here knows each player played atleast 3plays need check wining (very hardthing called magicbox math rule premade years ago or big math topic), numpy can help for create arrays or () to loop on all possible options, require math detect rule for this type of game
    if x_can_win == True:
        print("X can be winner")

        for p in x_l:
            x_win = []
            old_x_win = []
            for win in t:
                for p_a in x_l:
                    print(p_a)
                    print(p_a in win and p_a not in old_x_win)


                    if p_a in win and p_a not in old_x_win:
                        print("hi")
                        x_win.append(p_a)
                        old_x_win.append(p_a)
                        

                print(p_a in win)
                print("#########")
            print("####!")
            # numpy 3 loops nested hard to asumlaite without desgin also remaing if worked good in other reverse
            print('imthe target', x_win)
            print("###!")
            if len(x_win) == 3:
                print("X Win Nice")
                x_win = []
                break
            else:
                x_win = []

    if o_can_win == True:
        print("O can be winner")
        
    return x_l

# win 1
#(0, 0), (1, 1), (2,2)
# win 1 reverse
# (0,2), (1, 1), (2,0)





dynamicGridDraw(total_rows=3, total_col=3, width=75, h=50, height=50, clickCB=clickEventListener)
root.mainloop()
