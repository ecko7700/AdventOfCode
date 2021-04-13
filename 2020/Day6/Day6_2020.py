# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 17:39:02 2021

@author: Edward
Problem source:https://adventofcode.com/2020/day/6
Problem:
--- Day 6: Custom Customs ---
As your flight approaches the regional airport where you'll switch to a much larger plane, customs declaration forms are distributed to the passengers.

The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify the questions for which anyone in your group answers "yes".
 Since your group is just you, this doesn't take very long.

However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. 
For each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:

abcx
abcy
abcz
In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. 
(Duplicate answers to the same question don't count extra; each question counts at most once.)

Another group asks for your help, then another, and eventually you've collected answers from every group on the plane (your puzzle input). 
Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

The first group contains one person who answered "yes" to 3 questions: a, b, and c.
The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
The last group contains one person who answered "yes" to only 1 question, b.
In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?
"""
filename = 'Day6_data.txt'

def loadfile(filename):
    f = open(filename, 'r')
    temp = []
    quest_dict = {}
    cnt = 0
    for line in f:
        if line !='\n':
            temp.append(line.rstrip())
        else:
            cnt += 1
            quest_dict[cnt] = temp
            temp = []
    quest_dict[cnt+1] = temp        
    return quest_dict

def countQuestions(quest_dict):
    score_dict = {}
    for ID in quest_dict:
        score = 0
        temp_list = []
        for value in quest_dict[ID]:
            for char in value:
                if char not in temp_list:
                    temp_list.append(char)
                    score += 1
        score_dict[ID] = score 
    return sum(list(score_dict.values()))

#NEED TO FIX:__________________________
def countQuestionsPart2(quest_dict):
    score_dict = {}
    for ID in quest_dict:
        score = 0
        temp_list = []
        for value in quest_dict[ID]:
            print(value)
            for char in value:
                if char not in temp_list:
                    temp_list.append(char)
        score +=1
        print(temp_list)
        score_dict[ID] = score 
    return sum(list(score_dict.values()))

#Unit Test
test_dict = {1 : ['abc'], 2 : ['ab' , 'ac'], 3: ['a','b','c'], 4: ['a','a','a','a'], 5 : ['b']}
print(countQuestions(test_dict))
print(countQuestionsPart2(test_dict)) #3 + 1 + 0 + 1 + 1 = 6


if __name__ == '__main__':
    print(countQuestions(loadfile(filename)))
    