#  Automated Marksheet Generator

A simple Python project that reads student marks from a CSV file and automatically generates their marksheet with Total, Percentage, Grade and Pass / Fail status.

##  Features
- Reads student data from a CSV file using Pandas
- Calculates Total and Percentage for each student
- Assigns Grade based on Percentage
- Automatically checks Pass / Fail
- Shows in which subject the student failed

##  Files in this Project
- `one.py` - Main Python code
- `marks.csv` - CSV file containing student marks

##  Subjects
- Maths
- Physics
- Programming

##  Grading System

| Percentage | Grade |
| --- | --- |
| 90 and above | A+ |
| 80 and above | A |
| 70 and above | B |
| 60 and above | C |
| 50 and above | D |
| 40 and above | E |
| Below 40 | F |

**Pass Rule:** Student must score 40 or more in all subjects to pass.

##  How to Run

1. Make sure Python is installed
2. Install the required library:

```bash
pip install pandas
