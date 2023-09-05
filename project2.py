#the dressing choice
def dressing():
  dressing_choice = input("Please choose a dressing: vinaigrette, ranch, blue cheese, lemon: ")
  return dressing_choice

#the salad choice
def salad():
  salad_choice = input("Would you like a garden salad or greek salad?: ")
  return f"a {salad_choice} salad with {dressing()} dressing"
  

def toppings():
  topping_list = []
  more = True
  while more:
    topping_choice = input("Add toppings: pepperoni, mushrooms, spinach, or say 'done': ")
    if topping_choice != "done":
      topping_list.append(topping_choice)
    else:
      more = False
  topping_string = " and ".join(topping_list)
  return topping_string

def pizza():
  pizza_choice = input("Please choose size: small, medium or large: ")
  
  #accounting for when user wants no toppings
  
  addition = toppings()
  if addition == "":
    return f"a {pizza_choice} pizza"
  return f"a {pizza_choice} pizza with {addition}"
  

def select_meal():
  request = True
  order = ""
  
  while request:
    start = input("Hello, would you like pizza or salad?: ")
    if start == "pizza":
      if order == "":
        order = pizza()
      else:
        order = order + " and " + pizza()
      
      print(f"You ordered {order}. Place another order or say 'done")
      
    elif start == "salad":
      if order == "":
        order = salad()
      else:
        order = order + " and " + salad()
      

      print(f"You ordered {order}. Place another order or say 'done")
      
    else:
      print("Your order has been placed. Goodbye.")
      request = False

select_meal()



