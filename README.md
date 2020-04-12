# Description
Program module for simplest tariffication. Var 4
# Functions
- parse(fileName) - parse CDR file from {fileName}, returns a list of lines
- charge(data) - based on {data} (Which is list of lines from parse function) calculates a price for services. Returns price as float.
# Dependencies
No dependencies
# How to run
 `python3 lab.py`  
 CDR must be in the same folder, named 'data.csv'  
 Program will write a price into output.txt (Create in case it isnt exist)

