#IT Support Ticket Validator and Priority Calculator

ticket_id = input("Enter the ticket ID: ").strip().upper()
description = input("Give the ticket description: ").strip().title()
priority = 0
try:
    severity = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid whole number.")
else:
    if severity >=1 and severity <=4:
      print("Valid severity")
      priority = severity *10
      print(f"For the ID : {ticket_id} the description is {description} and severity is {severity} and the priority score is {priority}")
    else:
      print("Invalid ")

