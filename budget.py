class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []

  def __str__(self):    
    title = '{:*^30s}'.format(self.category)
    for entry in self.ledger:
      amount = f"{entry['amount']:0.2f}"
      title += '\n' + '{:<23s}'.format(f"{entry['description'][0:23]}") + '{:>7s}'.format(f"{amount}")
    title += "\n" + f"Total: {self.get_balance()}"
    return title # f'${price:0.2f}'

  def deposit (self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw (self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": amount * -1, "description": description})
    return self.check_funds(amount)

  def get_balance(self):
    balance = 0
    for entry in self.ledger:
      balance += entry["amount"]
    return balance

  def transfer(self, amount, transfer):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {transfer.category}")
      transfer.deposit(amount, f"Transfer from {self.category}")
    return self.check_funds(amount)
    

  def check_funds(self, amount):
    return self.get_balance() >= amount

def create_spend_chart(categories):
  title = 'Percentage spent by category\n'
  wd = []
  string = ''
  
  for category in categories:
    total = 0
    for entry in category.ledger:
      if entry["amount"] < 0:
        total += entry["amount"]
    wd.append(total)

  total = sum(wd)

  percentages = [(x / total * 100) for x in wd]
  #s=lambda x:x*x
  for x in range(100, -10, -10):
    title += '{:>3s}'.format(f"{x}") + "|"
    for pers in percentages:
      if pers < x:
        title += " " * 3
      elif pers >= x:
        title += " o "
    title += " " + "\n"

  title += "    -" + "---" * len(categories)

  lens = [len(x.category) for x in categories]
  length = max(lens)

  for i in range(length):
    string += "\n    "
    for category in categories:
      if i >= len(category.category):
        string += ' ' * 3
      else:
        string += ' ' + category.category[i] + ' '
    string += ' '
      
  return title + string.rstrip("\n")