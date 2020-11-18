import math
def split_check(total, number_of_people):
  cost_per_person = total_due / split_among
  # we want to round up the number in order to make sure that the person paying is not paying the extra out of their own pocket
  return math.ceil(cost_per_person)


total_due = float(input("What is the total? \n"))
split_among = int(input("How many people are we spliting it among? \n"))
amount_due = split_check(total_due, split_among)
print(f'Each person owes ${amount_due}')