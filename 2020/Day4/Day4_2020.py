# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:26:47 2021

@author: Edward
Problem source:https://adventofcode.com/2020/day/4
Problem:
--- Day 4: Passport Processing ---
You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport. While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't actually valid documentation for travel in most of the world.

It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport scanners, and the delay could upset your travel itinerary.

Due to some questionable network security, you realize you might be able to solve both of these problems at the same time.

The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. 
Passports are separated by blank lines.

Here is an example batch file containing four passports:

ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt (the Height field).

The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials, not a passport at all! 
Surely, nobody would mind if you made the system temporarily ignore missing cid fields. Treat this "passport" as valid.

The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not, so this passport is invalid.

According to the above rules, your improved system would report 2 valid passports.

Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?
"""
def load_batch_data():
    file_name = 'Day4_data.txt'
    f1 = open(file_name,'r')
    dict_passports = {}
    passports = []
    pass_port_count = 0
    for line in f1:
        temp_string=''
        if line!='\n':
            for char in line:
                temp_string = temp_string+char
            passports.append(temp_string.split())
        else:
            dict_passports[pass_port_count] = passports
            passports = []
            pass_port_count +=1
    dict_passports[pass_port_count] = passports
    return dict_passports

def load_test_data():
    test_file ='Day4_testdata.txt'
    f2 = open(test_file,'r')
    dict_passports = {}
    passports = []
    pass_port_count = 0
    for line in f2:
        temp_string=''
        if line!='\n':
            for char in line:
                temp_string = temp_string+char
            passports.append(temp_string.split())
        else:
            dict_passports[pass_port_count] = passports
            passports = []
            pass_port_count +=1
    dict_passports[pass_port_count] = passports
    return dict_passports
    
def checkPassports(dict_passports):
    print("Number of passports to test: "+ str(len(dict_passports.keys())))
    valid_count = 0
    valid_passports = {}
    for passport_ID in dict_passports:
        check_dict = {'byr' : False, 'iyr' : False, 'eyr': False, 'hgt': False, 'hcl': False, 'ecl': False, 'pid': False, 'cid':False}
        for line in dict_passports[passport_ID]:
            for fields in line:
                check_attribute = fields[0:3]
                if check_attribute in check_dict:
                    check_dict[check_attribute] = True
        if (check_dict['byr'] == True) and (check_dict['iyr'] == True) and (check_dict['hgt'] == True) and (check_dict['eyr'] == True) and (check_dict['hcl'] == True) and (check_dict['ecl'] == True) and (check_dict['pid'] == True):
            valid_count += 1
            valid_passports[passport_ID] = "Valid"
            print(dict_passports[passport_ID])
    
    return valid_count

if __name__ == '__main__':
    print(str(checkPassports(load_batch_data()))+ " Valid passports")
    print("Running Unit Test")
    test = checkPassports(load_test_data())
    if test == 2:
        print("Unit Test succesful")
        print(test)
    else:
        print("Unit test failed")
    
            
        

