import tkinter as tk
root= tk.Tk()

# issue cover only all options for first 3 plays (reduced it only win when normal case 3 first play), require, 4 case, and 5 case, and my performance code helped to start from 3 else no winier
#right top right it was the end of app but this techiniue one by one step !!!! anlysis point number 3 is have something speacial in this game
# this lib could creat right now new tiktaktoe game with unlimted rows, and always 3 cols, next update could make it dynamic cols too and fit the row and col, must if 4 rows, and 4 wins so there are 4 cols or keep 3 np but but better 4 for magicbox achived
# copy right PythonKing, can use only in your products not allowed developer or own for selling another version of this library without permession

#important to pass the async arugment (event_target_prop) within the drawing loop, that used latter in the callback any time in app lifetime
from functools import partial
# called the ez grid tkinter py
index = 0
btns = {}
dic = {}
x = True
plays = []
plays_cords = []
# this dynamic function can draw any number of grid, in html grid is max 12 but here grid max unlimted contrled with width, height you as native match use the valid height, w=width/2, width=50, this how size handled can accept all sizes fit with cells, and cols, and add dynamic custom callback using partials you control, it and get the event listener target class in your cb !!before simplest way to draw grid unlimited rows, col3 , cols can automated to
def dynamicGridDraw(total_rows=3, total_col=3, width=75, h=0, height=50, clickCB=lambda: None):
    global canvas1
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
                btns[rc_string] = {'target': button1, 'row': r, 'col': i, 'w': width/2, 'h': h, 'width': width, 'height': height, 'meta': [], 'canvas': canvas1}
                canvas1.create_window(int(width/2), h, window=button1, width=width, height=height)
                # w
            if i == 1:
                rc_string = 'row{}-{}'.format(r, i)
                button1 = tk.Button(text='', command=partial(clickCB,rc_string), bg='brown',fg='white', font=('helvetica', 15, 'bold'))
                btns[rc_string] = {'target': button1, 'row': r, 'col': i, 'w': width/2, 'h': h, 'width': width, 'height': height, 'meta': [], 'canvas': canvas1}
                canvas1.create_window(int(width/2)*3, h, window=button1, width=width, height=height)
                # w * 3
            if i == 2:
                rc_string = 'row{}-{}'.format(r, i)
                #must int as python deep match so will return bigger numb /2 and in multiple 2 int good, also tkinter need simple 1 , 1,22
                button1 = tk.Button(text='', command=partial(clickCB,rc_string), bg='brown',fg='white', font=('helvetica', 15, 'bold'))                
                btns[rc_string] = {'target': button1, 'row': r, 'col': i, 'w': width/2, 'h': h, 'width': width, 'height': height, 'meta': [], 'canvas': canvas1}
                canvas1.create_window(int(width/2)*5, h, window=button1, width=width, height=height)
                # w * 5
            index += 1
        h += 50
    print('hello')
    print(dic)



# here developer code for create game and use grid drawer, eg tiktaktoe, dynamicGridDraw(total_rows=3, total_col=3, width=75, h=50, height=50, clickCB=clickEventListener)
# dynamicGridDraw(total_rows=3, total_col=3, width=40, h=50, height=50, clickCB=clickEventListener) ledo, chess when complete max 12grid
# x in this simple eg fast, start first so who need x will start first players decide
# this is the main game callback/callbacks, chess maybe need 2 clicks not 1, select, move per player, maybe there lib.createTiktakToe()but this core unique idea using smallest thing in tkinter reading 2 lines from working example of canvas and button, uses Brain RAM to understand more would make bigger lib
def clickEventListener(rc_string):
    global x
    # to prevent duplicate player from break order of switch check if duplicate in begning
    duplicate_play_check = (btns[rc_string]['row'], btns[rc_string]['col'])
    if duplicate_play_check in plays_cords:
        print("dulicate play")
        return False
    currentPlay = 'X'
    if x == True:
        # current play x
        currentPlay = 'X'
        x = False
        
    else:
        # current play o
        currentPlay = 'O'
        x = True

    print(plays)
    print(currentPlay)
    # the asynco part ez set the key value when player play
    btns[rc_string]['target'].config(text=currentPlay)
    # set meta to target ez with grid drawer lol max would tkinter grid do was draw gui dynamic for new games use meta tkinter grid custom
    btns[rc_string]['meta'].append({'play': currentPlay})

    plays.append(btns[rc_string])
    plays_cords.append((btns[rc_string]['row'], btns[rc_string]['col']))
    win_result = verify_win(plays, btns[rc_string]['canvas'])

    # end of game win or no win or continue
    
    if win_result == False and (len(plays) == 9):
        canvas1.delete('all')
        button2 = tk.Button(text='No Winner Play Again', command=partial(repeat, dynamicGridDraw, canvas1, 3, 3, 75, 50, 50, clickEventListener), bg='brown',fg='white', font=('helvetica', 15, 'bold'))
        canvas1.create_window(100, 100, window=button2)
        canvas1.pack(side="top", fill="both", expand=True, padx=2, pady=2, ipadx=2)
    elif win_result == True:
        canvas1.delete('all')
        win_text = '{} Wins Play Again'.format(currentPlay)
        #canvas1.config(width=300)
        button2 = tk.Button(text=win_text, command=partial(repeat, dynamicGridDraw, canvas1, 3, 3, 75, 50, 50, clickEventListener), bg='brown',fg='white', font=('helvetica', 15, 'bold'))
        canvas1.create_window(100, 100, window=button2)            
        #canvas1.place(anchor=tk.NW, relx=0.5, rely=0.5)
        # pack not add only it also fit the canvas
        canvas1.pack(side="top", fill="both", expand=True, padx=1)
    else:
        pass
    print(win_result, 'what noob')
    #print(btns[rc_string])

# game function used to provide list of plays to verify group of plays in same time according to stati list of wining plays eg tiktaktoe [(0,0), (0,1), (0,2)] in wins=[(0,0), (0,1), (0,2)]
def uniqueListsOf(plays=[], num=3, old_result=[]):
    result = []
    try:
        process = plays.copy()    
        index = 0
            
        current = []
        # (2,2),(1,1),(0,0)
        mini_i = 0
        for pi in range(len(plays)):
            for ai in range(len(plays)):
                play = plays[pi]
                current = [play]
                for proccessI in range(len(process)):
                    processPlay = process[proccessI]
                
                    if processPlay not in current and len(current) != num:                       
                        current.append(processPlay)
                    
                    # print(".", processPlay)
                    if len(current) == num:             
                        # print("hello")
                        if current not in result and current not in old_result:
                            # print(current)
                            result.append(current)
                        current = []
                    
                    if processPlay not in current:
                        # print("?")
                        current.append(processPlay)
                    
        return result
    except Exception as e:
        raise e
    return result

#this function is what used to generate all posibile passes of any character dynamic eg pass of 3, pass of 4, pass of100 will provide all possibile concated string list to fast search in groped list match , pass or plays nice
def getAllposibileLists(wins):
    all_wins = []
    for awin in wins:
        items = uniqueListsOf(awin,3)
        for aitem in items:
            if aitem not in all_wins:
                all_wins.append(aitem)
    # now start actions by each win in beging, 1,2,3
    startByEveryOne = []
    for awin in all_wins:
        items = uniqueListsOf(awin,3, all_wins)
        for aitem in items:
            if aitem not in all_wins:
                all_wins.append(aitem)
    return all_wins

#it build in conispet static check but it dynamic list and 3 nested loops magic box and other math rules checked this alot by many until return rule maybe with 1 loop instead of 3 but both fast and same game and dynamic 1 if statment only with includes to check all options for win I even not calcuated yet how many options
#python king not need magicbox maybe later he read it while understanding logic and provide solution for performance only
wins = [
       [(0,0,),(1,1,),(2,2,)],
       [(2,0,),(1,1,),(0,2,)],
       # sid2 magicbox lets call it same col rule sure have same row rule (later can anlsysised and got 1 list repeated for generate 3 mixed with reverse row will be generate 6 from 1
       [(0,0,),(1,0,),(2,0,)],
       [(0,1,),(1,1,),(2,1,)],
       [(0,2,),(1,1,),(2,0,)],
       # i did not do this part or complete js magicbox 4 years ago (also can use flask live app send request to make it multiple no need socket both open, create url for game request, save in db, send request for this url, send saved for x and o for each new play the online tkinter simple no socet if requests avail
       [(0,0,),(0,1,),(0,2,)],
       [(1,0,),(1,1,),(1,2,)],
       [(2,0,),(2,1,),(2,2,)]
    ]
#       [(0,2),(1,1),(2,0)]

wins = getAllposibileLists(wins)
#as mentioned simplest check win for tiktaktoe ignore perpeation of data base is final result play of 3 dicts in wins [(),(),()] in [[(),(),()],[(),(),()]] (heavy anslysis list done before game start)
# found nested 3 loops in normal not required also loop size must match the len of plays, 4 need 4 unique lists and loop on them and check if any one in wins (case win in play 4)
# now app not uses cases but some options missing (solve cases 4, 5)
# !!!!! new 3 dicts array of all posibiole unique options play 1,2,3, !!---len(4-plays) [1,2,3], [1,2,4], [1,3,4], [2,3,4]!!!!--- 5max [1,2,3], [1,2,4], [1,2,5], [1,4,5], [3,4,5]
# anlysis function inspered from reverse numpy actioin uses 3 nested loop for search instead of make math static numpy nested arrays and do a check
def player_win(plays_list=[], play_title=''):
    win_or_not = False
    global plays
    list_numpy = []
    global canvas1
    # new 3 dicts array of all posibiole unique options play 1,2,3, !!---len(4-plays) [1,2,3], [1,2,4], [1,3,4], [2,3,4]!!!!--- 5max [1,2,3], [1,2,4], [1,2,5], [1,4,5], [3,4,5]
    allPosible3Plays = getAllposibileLists(uniqueListsOf(plays_list))
    # single in check for win validate by group of 3||infinty plays not play,play->loop    
    for posiblePlay in allPosible3Plays:
        if posiblePlay in wins:
            win_or_not = True
            break
        
    return win_or_not

# the idea  basicest need the 3 check and empty
def verify_win(plays, canvas):
    x_l = []
    o_l = []
    for item in plays:
        if item['meta'][0]['play'] == 'X':
            x_l.append((item['row'],item['col'],))

        if item['meta'][0]['play'] == 'O':
            o_l.append((item['row'],item['col'],))
            
    x_can_win = len(x_l) >= 3
    o_can_win = len(o_l) >= 3

    playerWon = False
    # here knows each player played atleast 3plays need check wining (very hardthing called magicbox math rule premade years ago or big math topic), numpy can help for create arrays or () to loop on all possible options, require math detect rule for this type of game
    if x_can_win == True:
        print("X can be winner")
        
        # chess will request hard nested must done with some algo or numpy or right number or loops nested or steps instead by trak king (thats when make compo vs player normal chess easy alotwith this lib, diffrent only game callback
        # this first loop for inital the arrays this the most top important like numpy but in loops one by one can allow all magicbox values as array instead of if and hard math rules simple as hello world and fast, also using tkinter_grid lib is make everything easy and accept all techniuqes for this game and chess later
        playerWon = player_win(plays_list=x_l, play_title='X')
        print("did you check this first", len(plays), playerWon)

    # check for win of o only if x not win already also x here plays first but this check dynamic if switched assign x and y
    if playerWon == False and o_can_win == True:
        print("O can be winner")
        playerWon = player_win(plays_list=o_l, play_title='O')
        #canvas.delete('all')
        #o_had_win = player_win(plays_list=o_l, wins_rules=wins)
        #if o_had_win:
        #print("O Win python king")
    
    return playerWon

# win 1.. core magicbox
#(0, 0), (1, 1), (2,2)
# win 1 reverse
# (0,2), (1, 1), (2,0)

""" dead but diffrent type of possibilties
# game function used to provide list of plays to verify group of plays in same time according to stati list of wining plays eg tiktaktoe [(0,0), (0,1), (0,2)] in wins=[(0,0), (0,1), (0,2)]
def uniqueListsOf(plays=[], num=3):
    result = []
    try:
        process = plays.copy()    
        index = 0
    
        if len(plays) == num:
            result.append(plays)
            return result
        if len(plays) < num:
            return result
    
        current = []
        for pi in range(len(plays)):
            play = plays[pi]
            current = [play]
            for proccessI in range(len(process)):
                if pi == proccessI:
                    continue
                processPlay = process[proccessI]
                # order important               
                if len(current) >= num:
                    result.append(current)
                    current = []

                if processPlay not in current:
                    current.append(processPlay)
                    
        return result
    except:
        print("error")
    return result
"""

def repeat(mainfun, canvas, total_rows=3, total_col=3, width=75, h=50, height=50, clickCB=clickEventListener):
    global canvas1
    global index
    global btns
    global root
    global x
    global plays
    global plays_cords
    canvas.delete('all')
    index = 0
    btns = {}
    dic = {}
    x = True
    plays = []
    plays_cords = []
    root.destroy()
    root= tk.Tk()
    mainfun(total_rows, total_col, width, h, height, clickCB)
    
# this app consider begning of create your own tiktaktoe game with rules, eg valid 4 cols, valid 4-infinty, provide easy positions using col,row as it handsontable not pycanvas
dynamicGridDraw(total_rows=3, total_col=3, width=75, h=50, height=50, clickCB=clickEventListener)
root.mainloop()
