# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
price = 15
if size == 'S':
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            price +=3            
        else:
            price +=2            
    else:
        if extra_cheese == 'Y':
            price +=1
        else:
            price +=0      
elif size == 'M':
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            price +=9            
        else:
            price +=8            
    else:
        if extra_cheese == 'Y':
            price +=6
        else:
            price +=5
if size == 'L':
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            price +=14            
        else:
            price +=13            
    else:
        if extra_cheese == 'Y':
            price +=11
        else:
            price +=10
print(f'Your final bill is ${price}.')
