# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 18:01:07 2021

@author: Edward
Problem source: https://adventofcode.com/2020/day/3
Problem:
With the toboggan login problems resolved, you set off toward the airport. 
While travel by toboggan might be easy, it's certainly not safe: there's very minimal steering and the area is covered in trees. 
You'll need to see which angles will take you near the fewest trees.

Due to the local geology, trees in this area only grow on exact integer coordinates in a grid.
You make a map (your puzzle input) of the open squares (.) and trees (#) you can see. For example:

..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times:

..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); 
start by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1. 
Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
In this example, traversing the map using this slope would cause you to encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
"""

def create_expanded_slope():
    file_name_1 = 'day3_2020_data.txt'
    file_name_2 = 'day3_data_expanded.txt'
    f1 = open(file_name_1, 'r')
    f2 = open(file_name_2,'w')
    for line in f1:
        f2.write(line.split()[0]*100 + '\n')
     
    f1.close()
    f2.close()

def read_slope():
    file_name_1 = 'day3_data_expanded.txt'
    f1 = open(file_name_1, 'r')
    slope_list = []
    
    for line in f1:
        slope_list.append(line.split())
    
    f1.close()
    return slope_list

def TobogganRoute(slope_list):
    sidecount = 0
    tree_count = 0
    file_name3 = 'day3_output.txt'
    f3 = open(file_name3, 'w')
    for L_count,slope in enumerate(slope_list):
        sidecount +=3
        try:
            if slope_list[L_count+1][0][sidecount:sidecount+1] =='#':
                tree_count +=1
                newslope = slope_list[L_count+1][0][:sidecount]+'X'+slope_list[L_count+1][0][sidecount+1:]
                f3.write(newslope + '\n')
            else:
                newslope = slope_list[L_count+1][0][:sidecount]+'O'+slope_list[L_count+1][0][sidecount+1:]
                f3.write(newslope + '\n')
        except IndexError:
            break
    print("Trees hit: " + str(tree_count))
    f3.close()
    return tree_count


#Unit Test
# test_list = []
# test_file = 'test_data.txt'
# g = open(test_file, 'r')
# for slope in g:
#     test_list.append(slope.split())

if __name__ == '__main__':
    TobogganRoute(read_slope())
