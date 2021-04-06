# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 20:43:59 2021

@author: Edward
Problem source: https://adventofcode.com/2020/day/2
Problem:
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. 
For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. 
The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
"""
filename = 'Day2_2020_data.txt'
f = open(filename, 'r')
data_list = []

for line in f:
    data_list.append(line.split()) 
#########################__________PART 1__________############################
def test_password(data_list):
    copy_data = data_list.copy()
    valid_pass_cnt = 0
    
    for l1 in copy_data:
        test_range_low = int(l1[0].split('-')[0])
        test_range_hgh = int(l1[0].split('-')[1])
        test_char = l1[1].split(':')[0]
        test_string = l1[2]
        test_char_count = test_string.count(test_char)
        if test_char_count >= test_range_low and test_char_count <= test_range_hgh:
            valid_pass_cnt +=1
        
        
    return valid_pass_cnt

#########################__________PART 2__________############################
"""
Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. 
(Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter.
 Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
"""
def test_password_new_policy(data_list):
    copy_data = data_list.copy()
    valid_pass_cnt = 0
    invalid_pass_cnt = 0
    
    for l1 in copy_data:
        test_range_low = int(l1[0].split('-')[0])
        test_pos_low = test_range_low - 1
        test_range_hgh = int(l1[0].split('-')[1])
        test_pos_hgh = test_range_hgh - 1
        
        test_char = l1[1].split(':')[0]
        test_string = l1[2]
        try:
            if test_string[test_pos_low] == test_char and test_string[test_pos_hgh] != test_char:
                valid_pass_cnt +=1
            elif test_string[test_pos_hgh] == test_char and test_string[test_pos_low] != test_char:
                valid_pass_cnt +=1
            else:
                invalid_pass_cnt +=1
        except IndexError:
            invalid_pass_cnt +=1
    return valid_pass_cnt



if __name__ == '__main__':
    print("Part 1 result: " + str(test_password(data_list)))
    print("Part 2 result: " + str(test_password_new_policy(data_list)))