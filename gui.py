from tkinter import *
import os

rows, cols = (25, 25)
goal_x, goal_y = (1, 1)

run_search_algos = False
SearchAlgoMaze = None


def set_values():
    global rows, cols, goal_x, goal_y, run_search_algos
    # rows, cols = ent_rows.get(), ent_cols.get()
    goal_x, goal_y = ent_goalX.get(), ent_goalY.get()
    run_search_algos = True
    window.destroy()


def check_changed():
    print("Run Together: {}".format(CheckRunMode.get()))
#     if CheckRunMode.get():
#         listbox.configure(state=NORMAL)
#         listbox.configure(exportselection=False)
#     else:
#         AlgoRunning.set("All Search Algorithms \nwill run Individually")
#         listbox.configure(state=DISABLED)


# def listbox_used(event):
#     selected_values = [listbox.get(i) for i in listbox.curselection()]
#     char = ""
#
#     if len(selected_values) > 1:
#         char = "s"
#     AlgoRunning.set("Running Algo{}:\n".format(char) + ", ".join(selected_values))


def algo_listbox(event):
    global SearchAlgoMaze
    SearchAlgoMaze = listbox_Algos.get(listbox_Algos.curselection())


def mdp_listbox(event):
    print(listbox_MDP.get(listbox_MDP.curselection()))

# ---------------WINDOW----------------------
window = Tk()
window.title('CS7IS2 - Assignment - 1')
window.geometry("380x480+0+0")
window.minsize(width=380, height=480)
window.maxsize(width=380, height=480)
window.config(pady=5, bg='#252527')

# -----------------MAZE------------------------
window.columnconfigure(0, weight=1, minsize=170)
window.rowconfigure(0, weight=1, minsize=200)

frm_maze = Frame(master=window, relief=RAISED, padx=5, pady=5, highlightbackground="#03cafc", highlightthickness=2,
                 bg='#252527')

lbl_maze = Label(master=frm_maze, text='Maze Parameters', font='Helvetica 18 bold', foreground='#03cafc', bg='#252527')

"""
lbl_rows = Label(master=frm_maze, text="Rows", bg='#252527', fg='white')
lbl_cols = Label(master=frm_maze, text="Cols", bg='#252527', fg='white')

ent_rows = Entry(master=frm_maze, width=5, highlightthickness=1, highlightcolor='#03cafc', bg='#252527', fg='white')
ent_rows.insert(END, string=f'{rows}')
ent_cols = Entry(master=frm_maze, width=5, highlightthickness=1, highlightcolor='#03cafc', bg='#252527', fg='white')
ent_cols.insert(END, string=f'{cols}')
"""

lbl_goal = Label(master=frm_maze, text="Goal", font='Helvetica 14 bold', foreground='#03cafc', bg='#252527')
lbl_gridSize = Label(master=frm_maze, text="Grid Size", font='Helvetica 14 bold', foreground='#03cafc', bg='#252527')

lbl_goalX = Label(master=frm_maze, text="X", bg='#252527', fg='white')
lbl_goalY = Label(master=frm_maze, text="Y", bg='#252527', fg='white')

ent_goalX = Entry(master=frm_maze, width=5, highlightthickness=1, highlightcolor='#03cafc', bg='#252527', fg='white')
ent_goalX.insert(END, string=f'{goal_x}')
ent_goalY = Entry(master=frm_maze, width=5, highlightthickness=1, highlightcolor='#03cafc', bg='#252527', fg='white')
ent_goalY.insert(END, string=f'{goal_y}')

mazes = os.listdir('SavedMazes/SearchAlgorithms')
listbox_Algos = Listbox(master=frm_maze, height=len(mazes), selectforeground='#252527',
                        selectbackground='#a7faa9', activestyle='none')


for index, element in enumerate(mazes):
    listbox_Algos.insert(index, element)
listbox_Algos.bind('<<ListboxSelect>>', algo_listbox)

btn_runAlgos = Button(master=frm_maze, text='RUN ALGOS', fg='green', command=set_values, bg='#252527',
                      highlightbackground='#252527')

# | DRAW

lbl_maze.grid(row=0, column=0, columnspan=2, sticky='nw')

"""
#   | ROW COL
lbl_rows.grid(row=1, column=0, sticky=W, pady=2)
ent_rows.grid(row=1, column=1, pady=2)

lbl_cols.grid(row=2, column=0, sticky=W, pady=2)
ent_cols.grid(row=2, column=1, pady=2)
"""

#   | GOAL
lbl_goal.grid(row=3, column=0, columnspan=2, sticky=W, pady=10)

lbl_goalX.grid(row=4, column=0, sticky=W, pady=2)
ent_goalX.grid(row=4, column=1, pady=2, sticky=E)

lbl_goalY.grid(row=5, column=0, sticky=W, pady=2)
ent_goalY.grid(row=5, column=1, pady=2, sticky=E)

lbl_gridSize.grid(row=6, column=0, columnspan=2, sticky=W, pady=10)
listbox_Algos.grid(row=7, column=0, columnspan=2)

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
"""
listbox = Listbox(master=frm_algo, height=3, selectmode='multiple', selectforeground='#252527',
                  selectbackground='#a7faa9',
                  activestyle='none')
algos = ['DFS', 'BFS', 'AStar']

for algo in algos:
    listbox.insert(algos.index(algo), algo)
    if algos.index(algo) < 2:
        listbox.selection_set(algos.index(algo))
listbox.bind('<<ListboxSelect>>', listbox_used)
"""

btn_runAlgos = Button(master=frm_algo, text='RUN ALGOS', fg='green', command=set_values, bg='#252527',
                      highlightbackground='#252527')

# | DRAW
lbl_algo.grid(column=0, row=0, sticky='nw')
chk_runMode.grid(column=0, row=2, sticky='nw')
lbl_algos.grid(column=0, row=3, sticky='nw', pady=10)
# listbox.grid(column=0, row=7, sticky='nw')
lbl_algosRunning.grid(column=0, row=8, sticky='nsew')
btn_runAlgos.grid(column=0, row=9, sticky='nsew')

frm_algo.grid(column=1, row=0, sticky='nsew', padx=5)

# -------------------MDP-----------------------
window.columnconfigure(0, weight=1, minsize=170)
window.rowconfigure(1, weight=1, minsize=10)

frm_mdp = Frame(master=window, relief=RAISED, padx=5, pady=5, highlightbackground="#ff0000", highlightthickness=2,
                bg='#252527')

lbl_mdp = Label(master=frm_mdp, text='Markov Decision Process', font='Helvetica 18 bold', foreground='#ff0000',
                bg='#252527')

btn_runMDP = Button(master=frm_mdp, text='RUN Markov', fg='green', command=set_values, width=36,
                    bg='#252527', highlightbackground='#252527')

mazes_mdp = os.listdir('SavedMazes/MDP')

listbox_MDP = Listbox(master=frm_mdp, height=len(mazes_mdp), selectforeground='#252527',
                      selectbackground='#a7faa9', activestyle='none')


for maze in mazes_mdp:
    listbox_MDP.insert(mazes_mdp.index(maze), maze)
listbox_MDP.selection_set(0)
listbox_MDP.bind('<<ListboxSelect>>', mdp_listbox)

lbl_mdp.grid(column=0, row=0, sticky='nw')

window.rowconfigure(1, weight=1)
listbox_MDP.grid(column=0, row=1, sticky='nw')
btn_runMDP.grid(column=0, row=2, sticky='nsew')

frm_mdp.grid(column=0, row=1, sticky='nsew', columnspan=2, padx=5, pady=4)

# -------------------RUN-----------------------

window.mainloop()
