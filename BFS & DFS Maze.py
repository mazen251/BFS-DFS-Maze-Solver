from pyamaze import maze,agent,COLOR,textLabel

x = 'b'
y = 'a'
val = input ("choose the method(a=BFS),(b=DFS):")
goalx = int(input ("enter the goal x position:"))
goaly = int(input ("enter the goal y position:"))
mcols = int(input ("enter the number of colomns:"))
mrows = int(input ("enter the number of rows:"))
if val == y:
    def BFS(m):
        start = (m.rows, m.cols)
        frontier = [start]
        explored = [start]
        bfsPath = {}
        while len(frontier) > 0:
            currCell = frontier.pop(0)
            if currCell == (goalx, goaly):
                break
            for d in 'ESNW':
                if m.maze_map[currCell][d] == True:
                    if d == 'E':
                        childCell = (currCell[0], currCell[1] + 1)
                    elif d == 'W':
                        childCell = (currCell[0], currCell[1] - 1)
                    elif d == 'N':
                        childCell = (currCell[0] - 1, currCell[1])
                    elif d == 'S':
                        childCell = (currCell[0] + 1, currCell[1])
                    if childCell in explored:
                        continue
                    frontier.append(childCell)
                    explored.append(childCell)
                    bfsPath[childCell] = currCell
        fwdPath = {}

        cell = (goalx, goaly)
        while cell != start:
            fwdPath[bfsPath[cell]] = cell
            cell = bfsPath[cell]
        return fwdPath
    if __name__ == '__main__':
        m = maze(mcols, mrows)
        m.CreateMaze(goalx,goaly,loopPercent=10)
        path = BFS(m)
        a = agent(m, footprints=True)
        m.tracePath({a: path})
        l = textLabel(m, 'Length of Shortest Path', len(path) + 1)

        m.run()

if val == x:
    def DFS(m):
        start = (m.cols,m.rows)
        explored = [start]
        frontier = [start]
        dfsPath = {}
        while len(frontier) > 0:
            currCell = frontier.pop()
            if currCell == (goalx, goaly):
                break
            for d in 'ESNW':
                if m.maze_map[currCell][d] == True:
                    if d == 'E':
                        childCell = (currCell[0], currCell[1] + 1)
                    elif d == 'W':
                        childCell = (currCell[0], currCell[1] - 1)
                    elif d == 'S':
                        childCell = (currCell[0] + 1, currCell[1])
                    elif d == 'N':
                        childCell = (currCell[0] - 1, currCell[1])
                    if childCell in explored:
                        continue
                    explored.append(childCell)
                    frontier.append(childCell)
                    dfsPath[childCell] = currCell
        fwdPath = {}
        cell = (goalx,goaly)
        while cell != start:
            fwdPath[dfsPath[cell]] = cell
            cell = dfsPath[cell]
        return fwdPath


    if __name__ == '__main__':
        m = maze(mcols,mrows)
        m.CreateMaze(goalx,goaly,loopPercent=50)
        path = DFS(m)
        a = agent(m, footprints=True)
        m.tracePath({a: path})


        l = textLabel(m, 'Length of Deepest Path', len(path) + 1)

        m.run()