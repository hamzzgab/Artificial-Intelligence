from tkinter import *
import os

rows, cols = (25, 25)
goal_x, goal_y = (1, 1)

run_search_algos = False
run_mdp_algo = False
SearchAlgoMaze = None

AlgoRun = []
SetDeterministic = True


def set_values():
    global rows, cols, goal_x, goal_y
    rows, cols = ent_rows.get(), ent_cols.get()
    goal_x, goal_y = ent_goalX.get(), ent_goalY.get()


def run_search_algo():
    global run_search_algos
    set_values()
    run_search_algos = True
    window.destroy()


def run_search_mdp():
    global run_mdp_algo
    set_values()
    run_mdp_algo = True
    window.destroy()


def check_changed():
    global AlgoRun, SetDeterministic
    AlgoRun =[CheckRunDFS.get(), CheckRunBFS.get(), CheckRunAStar.get()]
    SetDeterministic = CheckDeterministic.get()


# ---------------WINDOW----------------------
window = Tk()
window.title('CS7IS2 - Assignment - 1')
window.geometry("410x410+0+0")
window.minsize(width=410, height=410)
# window.maxsize(width=410, height=410)
window.config(pady=5, bg='#252527')

# -----------------MAZE------------------------
window.columnconfigure(0, weight=1, minsize=170)
window.rowconfigure(0, weight=1, minsize=200)

frm_maze = Frame(master=window, relief=RAISED, padx=5, pady=5, highlightbackground="#03cafc", highlightthickness=2,
                 bg='#252527')

lbl_maze = Label(master=frm_maze, text='Maze Parameters', font='Helvetica 18 bold', foreground='#03cafc', bg='#252527')


lbl_rows = Label(master=frm_maze, text="Rows", bg='#252527', fg='white')
lbl_cols = Label(master=frm_maze, text="Cols", bg='#252527', fg='white')

ent_rows = Entry(master=frm_maze, width=5, highlightthickness=1, highlightcolor='#03cafc', bg='#252527', fg='white')
ent_rows.insert(END, string=f'{rows}')
ent_cols = Entry(master=frm_maze, width=5, highlightthickness=1, highlightcolor='#03cafc', bg='#252527', fg='white')
ent_cols.insert(END, string=f'{cols}')


lbl_goal = Label(master=frm_maze, text="Goal", font='Helvetica 14 bold', foreground='#03cafc', bg='#252527')
lbl_gridSize = Label(master=frm_maze, text="Grid Size", font='Helvetica 14 bold', foreground='#03cafc', bg='#252527')

lbl_goalX = Label(master=frm_maze, text="X", bg='#252527', fg='white')
lbl_goalY = Label(master=frm_maze, text="Y", bg='#252527', fg='white')

ent_goalX = Entry(master=frm_maze, width=5, highlightthickness=1, highlightcolor='#03cafc', bg='#252527', fg='white')
ent_goalX.insert(END, string=f'{goal_x}')
ent_goalY = Entry(master=frm_maze, width=5, highlightthickness=1, highlightcolor='#03cafc', bg='#252527', fg='white')
ent_goalY.insert(END, string=f'{goal_y}')

"""
mazes = os.listdir('SavedMazes/SearchAlgorithms')
listbox_Algos = Listbox(master=frm_maze, height=len(mazes), selectforeground='#252527',
                        selectbackground='#a7faa9', activestyle='none', exportselection=False)


for index, element in enumerate(mazes):
    listbox_Algos.insert(index, element)
listbox_Algos.bind('<<ListboxSelect>>', algo_listbox)

btn_runAlgos = Button(master=frm_maze, text='RUN ALGOS', fg='green', command=set_values, bg='#252527',
                      highlightbackground='#252527')
"""
# | DRAW

lbl_maze.grid(row=0, column=0, columnspan=2, sticky='nw')

#   | ROW COL
lbl_rows.grid(row=1, column=0, sticky=W, pady=2)
ent_rows.grid(row=1, column=1, pady=2)

lbl_cols.grid(row=2, column=0, sticky=W, pady=2)
ent_cols.grid(row=2, column=1, pady=2)

#   | GOAL
lbl_goal.grid(row=3, column=0, columnspan=2, sticky=W, pady=10)

lbl_goalX.grid(row=4, column=0, sticky=W, pady=2)
ent_goalX.grid(row=4, column=1, pady=2, sticky=E)

lbl_goalY.grid(row=5, column=0, sticky=W, pady=2)
ent_goalY.grid(row=5, column=1, pady=2, sticky=E)

lbl_gridSize.grid(row=6, column=0, columnspan=2, sticky=W, pady=10)
# listbox_Algos.grid(row=7, column=0, columnspan=2)

frm_maze.grid(column=0, row=0, sticky='nsew', padx=5)

# ------------SEARCH-ALGORITHM-----------------
window.columnconfigure(1, weight=1, minsize=170)
window.rowconfigure(0, weight=1, minsize=200)

frm_algo = Frame(master=window, relief=RAISED, padx=5, pady=5, highlightbackground="#ecfc03", highlightthickness=2,
                 bg='#252527')

lbl_algo = Label(master=frm_algo, text='Search Algorithm', font='Helvetica 18 bold', foreground='#ecfc03', bg='#252527')
lbl_algos = Label(master=frm_algo, text='Run Algos', font='Helvetica 14 bold', foreground='#ecfc03', bg='#252527')

AlgoRunning = StringVar(value="Running Algos:\nDFS, BFS")
lbl_algosRunning = Label(master=frm_algo, textvariable=AlgoRunning, font='Helvetica 14', foreground='#ecfc03',
                         height=6, bg='#252527')

CheckRunMode = IntVar(value=1)
chk_runMode = Checkbutton(master=frm_algo, text='Run Together', variable=CheckRunMode, onvalue=1, offvalue=0,
                          command=check_changed, bg='#252527', fg='white')


CheckRunDFS = IntVar(value=1)
chk_runDFS = Checkbutton(master=frm_algo, text='DFS', variable=CheckRunDFS, onvalue=1, offvalue=0,
                          command=check_changed, bg='#252527', fg='white')

CheckRunBFS = IntVar(value=1)
chk_runBFS = Checkbutton(master=frm_algo, text='BFS', variable=CheckRunBFS, onvalue=1, offvalue=0,
                          command=check_changed, bg='#252527', fg='white')

CheckRunAStar = IntVar(value=1)
chk_runAStar = Checkbutton(master=frm_algo, text='AStar', variable=CheckRunAStar, onvalue=1, offvalue=0,
                          command=check_changed, bg='#252527', fg='white')

btn_runAlgos = Button(master=frm_algo, text='RUN ALGOS', fg='green', command=run_search_algo, bg='#252527',
                      highlightbackground='#252527')

# | DRAW
lbl_algo.grid(column=0, row=0, sticky='nw')
# chk_runMode.grid(column=0, row=2, sticky='nw')
lbl_algos.grid(column=0, row=1, sticky='nw', pady=10)
chk_runDFS.grid(column=0, row=2, sticky='nw')
chk_runBFS.grid(column=0, row=3, sticky='nw')
chk_runAStar.grid(column=0, row=4, sticky='nw')
btn_runAlgos.grid(column=0, row=9, sticky='nsew')

frm_algo.grid(column=1, row=0, sticky='nsew', padx=5)

# -------------------MDP-----------------------
window.columnconfigure(0, weight=1, minsize=170)
window.rowconfigure(1, weight=1, minsize=10)

frm_mdp = Frame(master=window, relief=RAISED, padx=5, pady=5, highlightbackground="#ff0000", highlightthickness=2,
                bg='#252527')

lbl_mdp = Label(master=frm_mdp, text='Markov Decision', font='Helvetica 18 bold', foreground='#ff0000',
                bg='#252527')

CheckDeterministic = IntVar(value=1)
chk_deterministic = Checkbutton(master=frm_mdp, text='Deterministic', variable=CheckDeterministic, onvalue=1, offvalue=0,
                          command=check_changed, bg='#252527', fg='white')


btn_runMDP = Button(master=frm_mdp, text='RUN MARKOV', fg='green', command=run_search_mdp, width=12,
                    bg='#252527', highlightbackground='#252527')

"""
mazes_mdp = os.listdir('SavedMazes/MDP')
listbox_MDP = Listbox(master=frm_mdp, height=len(mazes_mdp), selectforeground='#252527',
                      selectbackground='#a7faa9', activestyle='none', exportselection=False)


for maze in mazes_mdp:
    listbox_MDP.insert(mazes_mdp.index(maze), maze)
listbox_MDP.selection_set(0)
listbox_MDP.bind('<<ListboxSelect>>', mdp_listbox)
"""

lbl_mdp.grid(column=0, row=0, sticky='nw')

window.rowconfigure(1, weight=1)
# listbox_MDP.grid(column=0, row=1, sticky='nw')
chk_deterministic.grid(column=0, row=1, sticky='nw')
btn_runMDP.grid(column=0, row=2, sticky='nsew')

frm_mdp.grid(column=0, row=1, sticky='nsew', columnspan=1, padx=5, pady=4)
# -------------------RUN-----------------------

window.mainloop()
