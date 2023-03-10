# Search and MDPs

For the purpose of this assignment I have used the open source [github](https://github.com/MAN1986/pyamaze) repository `pyamaze`


## Documentation
```
https://github.com/hamzzgab/Artificial-Intelligence.git # CLONE
cd Assignment-1                                        # MAIN FOLDER
pip install -r requirements.txt                        # INSTALL
```

If the requirements.txt doesn't work the `pyamaze` library can be simply installed by using
```
pip install pyamaze
```

### Commands
1. To run the code simply run the main.py file
```
python main.py
```

The code will display a _GUI_ where parameters can be changed such as:
1. Grid Size
2. Goal Location
3. The algorithms to run together

<img src="./images/GUI.png" height="400">

### Defaults
Grid:
1. `Rows - 25`
2. `Cols - 25`
3. `Goal - (1, 1)` (Top Left) 

Search Algorithm:
The selected algorithms will run together
1. `DFS - Selected`
2. `BFS - Selected`
3. `AStar - Selected`

Markov Decision Process:
The selected algorithms will run together
1. `Value Iteration - Selected`
2. `Policy Iteration - Selected`

### Search Algorithms

To run the select the checkboxes from the Search Algorithm section and click on the Run Algos button. It will run the selected algorithm using the rows, cols as the grid size and the reach to the specified goal.

#### Analysis Parameters
To compare the 3 algorithms I have used 3 metrics
1. Final Path
2. Searched Path
3. Time Taken

#### 1. Depth First Search
- Select only the DFS checkbox
- Click on `RUN ALGOS`

<img src="./images/GUI-DFS.png" height="400">

- The code will open a new window on which the DFS Algorithm will run
<img height="400" src="./images/DFS.png"/>


