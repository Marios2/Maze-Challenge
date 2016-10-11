#Initiate directions array which contains the different directions the actor will follow. 4 patterns of traversing the maze are deifined, as shown in directions array.
directions = []
directions.append(["-1,0","0,1","1,0","0,-1"]) # Pattern 1: Actor moves always North. If he gets stuck, he moves East. If he gets stuck stuck he moves South. If he gets stuck again, he moves West
directions.append(["-1,0","0,-1","1,0","0,1"]) #Pattern 2: In the same manner as above, Actor moves North, West, South, East
directions.append(["1,0","0,-1","-1,0","0,1"]) #Pattern 3: In the same manner as above, Actor moves South, West,North, East
directions.append(["1,0","0,1","-1,0","0,-1"]) #Pattern 4: In the same manner as above, Actor moves South, East, North, West


# Create class Actor which handles the movement of the actor in the maze
class Actor:
    #attr_reader :x_point, :y_point, :goal_path
    rec_counter = 0
    #constructor
    def __init__(self, x_point,y_point,goal_path):
        self.rec_counter = 0
        self.x_point=x_point
        self.y_point=y_point
        self.goal_path=goal_path



    # recursive algorithm for finding the goal_path
    def find_path(self,x,y,x_goal,y_goal,rows,cols,dir):

        # if outside the bounds return False
        if (x<0 or x==rows or y<0 or y==cols):
            return False

        # if actor has reached the goal, enter the last coordinates in array "goal_path" and return True
        if (x==x_goal and y==y_goal):
            goal_path.append("%s,%s(G)"%(x,y))
            return True

        # if actor meets block or a square where he had been before, then return False
        if ("%s,%s"%(x,y)) in block_array or ("%s,%s"%(x,y)) in goal_path:
            return False
        # goal_path cannot be larger than rows*cols
        self.rec_counter += 1
        if self.rec_counter >=rows*cols :
            return False


        goal_path.append("%s,%s"%(x,y))

        # Check which direction the actor can follow, and call the recursive
        if self.find_path(x + int(dir[0].split(",")[0]),y + int(dir[0].split(",")[1]),x_goal,y_goal, rows, cols,dir):
            return True

        if self.find_path(x + int(dir[1].split(",")[0]),y + int(dir[1].split(",")[1]),x_goal,y_goal, rows, cols,dir):
            return True

        if self.find_path(x + int(dir[2].split(",")[0]),y + int(dir[2].split(",")[1]),x_goal,y_goal, rows, cols,dir):
            return True

        if self.find_path(x + int(dir[3].split(",")[0]),y + int(dir[3].split(",")[1]),x_goal,y_goal, rows, cols,dir):
            return True

        goal_path.pop()
        return False




# print the 2D maze in the console
def print_maze(temp_array,cols):
    i = 0
    for cell in range(len(temp_array)):
        print temp_array[cell] + " ",
        i+= 1
        if i == cols:
            print "\n"
            i = 0


    print"\n"

#Each text file must contain a maze in the format, as presented below:
#
#
#   ___XX (\n)
#   S__X_ (\n)
#   __XX_ (\n)
#   X___G (\n) <--


#Rows and Columns of the Maze
rows = 0
cols = 0
# Filenames are populated in file "c_Maze_Challenge.rb"
message = "File %s does not exist\n" %filename
try:
    print "Please enter the filename (.txt) containing the Maze: \n"
    print "%s\n" %filename
    print "\n"

            # Create a temporary array that will include the content of the maze ("_","S","G","X")
    temp_array=[]   #create the maze and initialize with 0
    with open (filename) as f:
        while True:
            c=f.read(1)
                # These characters below are the accepted characters in a txt containing maze
            if c=="_" or c=="X"or c=="S" or c=="G" or c=="\n":
                if c!="\n":
                    temp_array.append(c)
                    cols+=1
                else:
                    rows+=1
            elif c=='':
                break
            else:
                message =("File %s has invalid character '%s'!" %(filename, c))
                raise
        cols=cols/rows
    print "Rows: %s Columns: %s\n\n Matrix \n\n" %(rows,cols)

            # Print the Maze in order for the user to check it in the console
    print_maze(temp_array,cols)


            #Create a 2D array (maze) and initialize with "0"
    maze= [[0 for x in range(cols)] for y in range(rows)]
            # Create an array which will contain the coordinates of blocks inside the maze ("X")
    block_array=[]

            # g_exists and s_exists in order to check if the input mazes do have one Start and one Goal square
    g_exists = 0
    s_exists = 0
    k=0
    for i in range(0,rows):
        for j in range(0,cols):
            maze[i][j]=temp_array[k]   #put the content of temp_array in the maze
            if maze[i][j] == "S":
                x_position = i          # Take the coordinates of the "S" square
                y_position = j
                s_exists += 1
            if maze[i][j] == "G":
                goal_x_position = i     # Take the coordinates of the "G" sqaure
                goal_y_position = j
                g_exists += 1

            if maze[i][j] =="X":
                block_array.append("%s,%s"%(i,j))   # Take the coordinates of the "X" squares

            k+=1


    if s_exists!=1 or g_exists!=1:
        message = "Maze is invalid as it does not contain 1 Start and 1 Goal!\nPlease modify the maze in order to include exactly 1 S and 1 G square.\n"
        raise
    else:
                # Initiate array all_paths that will contain all paths from Start to Goal
        all_paths = []
                    # Traverse with all direction algorithms defined at the top of the code
        for i in range(0,len(directions)):
            goal_path=[]
            actor=Actor(x_position, y_position,goal_path)
            goal_path.append("%s,%s(S)"%(x_position,y_position))
            if actor.find_path(x_position,y_position,goal_x_position,goal_y_position,rows,cols,directions[i]):
                actor.goal_path.pop(1) # in order to hold the coordinate with the symbol "S" that shows the Start point
                all_paths.append(actor.goal_path)


        if not all_paths:
            print "There is no path from Start to Goal square for this maze!\n"
        else:
            goal_path=[list(x) for x in set(tuple(x) for x in all_paths)]
            for i in range(0,len(goal_path)):
                print "A path from the Start to the Goal Point is :\n"
                print goal_path[i]
                print "\n"


        print("\n")


except:
   print message
