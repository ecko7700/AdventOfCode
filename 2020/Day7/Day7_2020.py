# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 20:31:31 2021

@author: Edward
Problem source:https://adventofcode.com/2020/day/7
Problem:
--- Day 7: Handy Haversacks ---
You land at the regional airport in time for your next flight.
 In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; 
bags must be color-coded and must contain specific quantities of other color-coded bags. 
Apparently, nobody responsible for these regulations considered how long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags. {LR: [1 BW, 2MY]} - CAN CONTAIN SG
dark orange bags contain 3 bright white bags, 4 muted yellow bags. {DO: [3 BW, 4MY]} - CAN CONTAIN 3 SG
bright white bags contain 1 shiny gold bag. {BW : [1 SG]} - CAN CONTAIN 1 SG - BASE CASE
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags. {MW : [2SG, 9 FB]}  - CAN CONTAIN 2 SG

shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags. {SG : [1 DO, 2 VP]} - Can Contain NO SG
dark olive bags contain 3 faded blue bags, 4 dotted black bags. {DO : [3 FB, 4DB]} - Can Contain NO SG
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags. {VP : [5 FB, 6 DB]} - Can Contain NO SG
faded blue bags contain no other bags. {FB : []} - Can Contain NO SG
dotted black bags contain no other bags. {DB : []} - Can Contain NO SG

These rules specify the required contents for 9 bag types. 
In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. 
If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? 
(In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

A bright white bag, which can hold your shiny gold bag directly.
A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)
"""
filename = 'Day7_data.txt'

def loaddata(filename):
    bag_data = []
    f = open(filename, 'r')
    for line in f:
        bag_data.append(line.rstrip())
    return bag_data

def countSG():
    bag_list = loaddata(filename)
    result = 0
    test_string = 'shiny gold'
    for bags in bag_list:
        if test_string in bags:
            result += 1
    return result

def bag_dict_build():
    bag_list = loaddata(filename)
    bag_dict = {}
    bag_key = ''
    contain_find = 0
    
    for bags in bag_list:
        contain_find = bags.find('contain')
        bag_key = bags[:contain_find-1]
        bag_values = '' # NEED TO COMPLETE CODE FOR BAG VALUES
        bag_dict[bag_key] = ''
        
    return bag_dict

#TEST 
if __name__ =='__main__':
    print(countSG())
    print(bag_dict_build())