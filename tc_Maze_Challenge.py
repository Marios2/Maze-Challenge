#Please make sure the mazes are in the appropriate format as shown below:
#
#   Maze Example:
#
#   ___XX(\n)
#   S__X_(\n)
#   __XX_(\n)
#   X___G(\n)


#Insert in array txt_files containing maze
#Certain txt files are already inserted for demonstration

# For big mazes, such as the maze in very_big_maze.txt, execution might take a few seconds
global filename
txt_files = ["medium_size_maze.txt", "maze1.txt", "maze2.txt", "very_small_maze.txt","maze3.txt","maze_with_invalid_character.txt","maze_2startingpoints.txt","maze_2goalpoints.txt","no_such_file.txt","maze4.txt"]

for filename in txt_files:
    execfile("Maze_Challenge.py")



#http://stackoverflow.com/questions/10370040/printing-a-readable-matrix-in-ruby
#http://ruby-doc.org/stdlib-2.0.0/libdoc/matrix/rdoc/Matrix.html
#https://en.wikipedia.org/wiki/Maze_solving_algorithm
#https://www.cs.bu.edu/teaching/alg/maze/
#http://www.laurentluce.com/posts/solving-mazes-using-python-simple-recursivity-and-a-search/
