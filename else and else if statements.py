age = 12

if age >= 13:
    print("Access granted.")
else:
    print("Sorry, you must be 13 or older to watch this movie.")


#example 2
credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
    print("Congratulations. You meet the graduation requirements")
else:
    print("You do not meet the requirements to graduate.")


#Example 3:
donation = 5000
print("Thank you for your donation!")

if donation >=1000:
    print("You've achieved platinum donor status")
elif donation >= 500:
    print("You've achived gold donor status")
elif donation >= 100:
    print("You've achieved silver donor status")
else:
    print("You've achieved bronze donor status")