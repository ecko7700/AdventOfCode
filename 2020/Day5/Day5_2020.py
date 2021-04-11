# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 17:38:32 2021

@author: Edward
Problem source:https://adventofcode.com/2020/day/5
Problem:
--- Day 5: Binary Boarding ---
You board your plane only to discover a new problem: you dropped your boarding pass! 
You aren't sure which seat is yours, and all of the flight attendants are busy with the flood of people that suddenly made it through passport control.

You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input); 
perhaps you can find your seat through process of elimination.

Instead of zones or groups, this airline uses binary space partitioning to seat people. 
A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".

The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). 
Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; 
the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). 
The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

For example, consider just the first seven characters of FBFBBFFRLR:

Start by considering the whole range, rows 0 through 127.
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44.
The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). 
The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.

For example, consider just the last 3 characters of FBFBBFFRLR:

Start by considering the whole range, columns 0 through 7.
R means to take the upper half, keeping columns 4 through 7.
L means to take the lower half, keeping columns 4 through 5.
The final R keeps the upper of the two, column 5.
So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.

Here are some other boarding passes:

BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.
As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?
"""
def loadData():
    filename = 'Day5_data.txt'
    f = open(filename, 'r')
    input_list =[]
    for line in f:
        input_list.append(line.split())
        
    return input_list

def getSeatID(encryptedSeat, seat_range_back=127, seat_range_front=0, col_up=7, col_low=0):
    copy_seat = encryptedSeat
    try:
        char = copy_seat[0]
        if char =='F':
            seat_range_front = seat_range_front
            seat_range_back = (seat_range_back + seat_range_front)//2
        elif char =='B':
            seat_range_front = ((seat_range_front + seat_range_back)//2)+1
            seat_range_back = seat_range_back
        elif char =='L':
            col_up = ((col_up + col_low)//2)
            col_low = col_low
        elif char =='R':
            col_up = col_up
            col_low = ((col_up + col_low)//2)+1
        return getSeatID(copy_seat[1:],seat_range_back, seat_range_front, col_up, col_low)
    except IndexError:
        result = seat_range_back * 8 + col_up
        return result

def getAllSeatID():
    input_list = loadData()
    decrypted_dict = {}
    for seat in input_list:
        decrypted_dict[seat[0]] = getSeatID(seat[0])
    return decrypted_dict

print(getAllSeatID())
print(getSeatID('FBFBBFFRLR'))
if __name__ =='__main__':
    test_seat_IDs = {567 : 'BFFFBBFRRR', 119 : 'FFFBBBFRRR', 820 : 'BBFFBBFRLL'}
    for test_ID in test_seat_IDs:
        if getSeatID(test_seat_IDs[test_ID]) == test_ID:
            print("Unit test passed for Seat ID: " + str(test_ID))
        else:
            print("Unit test FAILED for Seat ID: " + str(test_ID))