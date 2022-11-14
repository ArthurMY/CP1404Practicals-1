"""
CP1404/CP5632 - Practical
Broken program to determine score status

get score
if score < 0 or score > 100
    display Invalid Score
elif score < 50
    display Bad
elif score < 90
    displayPassable
else:
    display Excellent
"""

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid Score")
elif score < 50:
    print("Bad")
elif score < 90:
    print("Passable")
else:
    print("Excellent")