from tkinter import *

# ---------------WINDOW----------------------
window = Tk()
window.title('CS7IS2 - Assignment - 1')
window.geometry("380x380+0+0")
window.minsize(width=380, height=380)
window.maxsize(width=380, height=380)
window.config(pady=5)

# ----------------FRAME-----------------------
window.columnconfigure(0, weight=1, minsize=170)
window.rowconfigure(0, weight=1, minsize=200)

rows, cols = (25, 25)
goal_x, goal_y = (1, 1)

frm_maze = Frame(master=window, relief=RIDGE, padx=5, pady=5, highlightbackground="#03cafc", highlightthickness=2)

lbl_maze = Label(master=frm_maze, text='Maze Parameters', font='Helvetica 18 bold', foreground='#03cafc')

lbl_rows = Label(master=frm_maze, text="Rows")
lbl_cols = Label(master=frm_maze, text="Cols")

ent_rows = Entry(master=frm_maze, width=5, highlightthickness=1)
ent_rows.insert(END, string=f'{rows}')
ent_cols = Entry(master=frm_maze, width=5, highlightthickness=1)
ent_cols.insert(END, string=f'{cols}')

lbl_goal = Label(master=frm_maze, text="Goal", font='Helvetica 14 bold', foreground='#03cafc')

lbl_goalX = Label(master=frm_maze, text="X")
lbl_goalY = Label(master=frm_maze, text="Y")

ent_goalX = Entry(master=frm_maze, width=5, highlightthickness=1)
ent_goalX.insert(END, string=f'{goal_x}')
ent_goalY = Entry(master=frm_maze, width=5, highlightthickness=1)
ent_goalY.insert(END, string=f'{goal_y}')

# | DRAW

lbl_maze.grid(row=0, column=0, columnspan=2)

#   | ROW COL
lbl_rows.grid(row=1, column=0, sticky=W, pady=2)
ent_rows.grid(row=1, column=1, pady=2)

lbl_cols.grid(row=2, column=0, sticky=W, pady=2)
ent_cols.grid(row=2, column=1, pady=2)

#   | GOAL
lbl_goal.grid(row=3, column=0, columnspan=2, sticky=W, pady=10)

lbl_goalX.grid(row=4, column=0, sticky=W, pady=2)
ent_goalX.grid(row=4, column=1, pady=2)

lbl_goalY.grid(row=5, column=0, sticky=W, pady=2)
ent_goalY.grid(row=5, column=1, pady=2)

frm_maze.grid(column=0, row=0, sticky='nsew', padx=5)


# ------------SEARCH-ALGORITHM-----------------
window.columnconfigure(1, weight=1, minsize=170)
window.rowconfigure(0, weight=1, minsize=200)

frm_algo = Frame(master=window, relief=RAISED,padx=5, pady=5, highlightbackground="#ecfc03", highlightthickness=2)

lbl_algo = Label(master=frm_algo, text='Search Algorithm', font='Helvetica 18 bold', foreground='#ecfc03')

chk_runMode = Checkbutton(master=frm_algo, text='Run Together')

lbl_algos = Label(master=frm_algo, text='Run Algos', font='Helvetica 14 bold', foreground='#ecfc03')

chk_dfs = Checkbutton(master=frm_algo, text='DFS')
chk_bfs = Checkbutton(master=frm_algo, text='BFS')
chk_aStar = Checkbutton(master=frm_algo, text='AStar')

lbl_algo.grid(column=0, row=0)

chk_runMode.grid(column=0, row=2, sticky='nw')

lbl_algos.grid(column=0, row=3, sticky='nw', pady=10)

chk_dfs.grid(column=0, row=4, sticky='nw')
chk_bfs.grid(column=0, row=5, sticky='nw')
chk_aStar.grid(column=0, row=6, sticky='nw')

frm_algo.grid(column=1, row=0, sticky='nsew', padx=5)

# -------------------MDP-----------------------
window.columnconfigure(0, weight=1, minsize=170)
window.rowconfigure(1, weight=1, minsize=10)

frm_mdp = Frame(master=window, relief=RAISED, padx=5, pady=5, highlightbackground="#ff0000", highlightthickness=2)

lbl_mdp = Label(master=frm_mdp, text='Markov Decision Process', font='Helvetica 18 bold', foreground='#ff0000')

lbl_mdp.grid(column=0, row=0)

frm_mdp.grid(column=0, row=1, sticky='nsew', columnspan=2, padx=5, pady=4)

# -------------------RUN-----------------------
btn_run = Button(text='RUN', fg='green')
btn_run.grid(column=0, row=2, sticky='nsew', columnspan=2)

window.mainloop()