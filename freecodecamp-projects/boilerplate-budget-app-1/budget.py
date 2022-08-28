class Category:
  def __init__ (self, name):
    self.name = name
    self.ledger = list()

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def __str__(self):
    stars = int(15 - (len(self.name) / 2))
    title = ("*" * stars + self.name + "*" * stars)
    items = ""
    total = 0
    for item in self.ledger:
      items += f"{item['description'][0:23]:23}"+ f"{item['amount']:>7.2f}"+"\n"
      total+=item['amount']
    output =title+'\n' + items + "Total: " + str(total)
    return output

  def get_balance(self):
    total_amount =0
    for i in self.ledger:
      total_amount+=i['amount']
    return total_amount
      
  def check_funds(self, amount):
    if (self.get_balance() >= amount):
      return True
    else:
      return False

  def withdraw(self, amount, description=""):
    if (self.check_funds(amount)):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def transfer(self, amount, category):
    if(self.check_funds(amount)):
      self.withdraw(amount, "Transfer to "+ category.name)
      category.deposit(amount, "Transfer from "+self.name)
      return True
    else: 
      return False

def create_spend_chart(categories):
  s= "Percentage spent by category \n"
  cats ={}
  print(categories[0].ledger)
  total=0
  for n in categories:
    for item in n.ledger:
      if item['amount'] <0:
        total+=item['amount']
    cats[n.name]=total
    for key, val in cats.items():
      percent = (val/total) *100
      cats[key] = percent
  for n in range(100, -1, -10):
    s+=f"{str(n)+'|' :>4}"
    for i in cats.values():
      if i >= n:
        s += " o "
    s+='\n'
  length=len(categories)
  lines = ((length*3)+1)* "-"
  s+=f"    {lines}\n"
  x_axis=""
  names=list(cats.keys())
  print(names)
  maximum = max(names, key=len)
  for i in range(len(maximum)):
    temp_str='     '
    for x in names:
      if i >= len(x):
        temp_str+='   '
      else:
        temp_str+=f"{x[i]+'  '}"
    temp_str+="\n"
    x_axis += temp_str
  s+=x_axis
  return s