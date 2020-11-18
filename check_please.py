def split_check(total, number_of_people):
  cost_per_person = total / number_of_people
  return cost_per_person

amount_due = split_check(84.97, 4)
print(f'Each person owes ${amount_due}')