"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
score = float(input("Enter score: "))
if 0 <= score <= 100:
    if score >= 90:
        print("excellent")
    elif score >= 50:
        print("passible")
    else:
        print("Bad")