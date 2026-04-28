## Python List Practice

Given List
emp_ids = [101, 1012, 104, 104, 101, 102, 1012]
Find Unique Employee IDs
emp_ids = [101, 1012, 104, 104, 101, 102, 1012]

unique_ids = list(set(emp_ids))

print(unique_ids)
Count How Many Times Each ID Appears
emp_ids = [101, 1012, 104, 104, 101, 102, 1012]

for emp in set(emp_ids):
print(emp, "appears", emp_ids.count(emp), "times")
Output
101 appears 2 times
102 appears 1 times
104 appears 2 times
1012 appears 2 times 3. Alphabetize Strings
Question

Sort a given string alphabetically.

## Example

string = "PythonRocks"
Output
PRchknoosty
Code
string = "PythonRocks"

result = ''.join(sorted(string))

print(result)

## Explanation

sorted(string) sorts every character
Capital letters come before lowercase letters because of ASCII values
''.join() joins the sorted characters back into a string 4. ASCII Values

ASCII gives each character a numeric value.

Important values:

A = 65
Z = 90
a = 97
z = 122

That is why uppercase letters come before lowercase letters when sorting.

## Example

print(ord('A'))
print(ord('Z'))
print(ord('a'))
print(ord('z'))
Output
65
90
97
122

## 5. More String Practice

## Example 1

string = 'axbyacd'

result = ''.join(sorted(string))

print(result)
Output
aabcdxy
Example 2
s = "escapevelocity"

result = ''.join(sorted(s))

print(result)
Output
acceeeilopstvy
