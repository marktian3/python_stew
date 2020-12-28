#program that asks user for sandwich preferences
import pyinputplus as pyip 

#menu
costMenu = {
"white": 1,
"whole wheat": 1.5,
"sourdough": 1.5,

"roast beef": 2,
"ham":2,
"turkey":3,

"kraft singles":1,
"swiss":1.5,
"cheddar":1.5,

"veggies":1
}

totalCost = 0
veggiesCost = 0
cheeseCost = 0

print('Welcome to the Marksmunchies Sandwich Shop')

#wanna see the menu?
seeMenu = pyip.inputYesNo(prompt = 'Would you like to see the menu?')
if seeMenu == 'yes': 
  print('Item                      Price')
  for Name, Price in costMenu.items():
    print(Name.ljust(15), end = '')
    print(str(Price).rjust(14))

#bread type using input menu
sandwichTotal = pyip.inputInt(prompt = 'How many sandwiches would you like? (max 3 per order)\n', min = 1, lessThan = 4)

#iteration for each sandwich 
for sandwichNum in range(1,sandwichTotal+1):
  print(f'For order number {sandwichNum}: ')
  breadType = pyip.inputMenu(['white', 'whole wheat', 'sourdough'], prompt = 'What type of bread would you like?\n', numbered = True)

  breadCost = costMenu[breadType]


#protein type using input menu 
  proteinType = pyip.inputMenu(['roast beef', 'ham', 'turkey'], prompt = 'What type of protein would you like? \n', numbered = True)
  proteinCost = costMenu[proteinType]

#cheese? yes/no
  wantCheese = pyip.inputYesNo(prompt = 'Would you like cheese?\n')
  if wantCheese == 'yes':
    cheeseType = pyip.inputMenu(['kraft singles', 'swiss', 'cheddar'], prompt ='What type of cheese would you like? \n', numbered = True)
    cheeseCost = costMenu[cheeseType]

#lettuce and tomato (yes/no)
  wantVeggies = pyip.inputYesNo(prompt = 'Do you want lettuce and tomatoes?\n')
  if wantVeggies == 'yes':
    veggiesCost = costMenu['veggies']

#total cost 
  sandwichCost = breadCost + proteinCost + cheeseCost + veggiesCost
  print(f'The cost of sandwich {sandwichNum} is ${sandwichCost}')
  totalCost = totalCost + sandwichCost 

print(f'The total cost of your order is ${totalCost}')
