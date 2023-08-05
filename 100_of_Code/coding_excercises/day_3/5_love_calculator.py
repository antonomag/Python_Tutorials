# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = (name1+ name2).lower()

# name_t = name.count('t')
# name_r = name.count('r')
# name_u = name.count('u')
# name_e = name.count('e')
# name_l = name.count('l')
# name_o = name.count('o')
# name_v = name.count('v')

# score1 = str(name_t + name_r + name_u + name_e)
# score2 = str(name_l + name_o + name_v + name_e)
# score1 = sum(true)
# score2 = sum(love)
#print('Your score is ' + true + love + '.')

#solution with lists and sum()
t = name.count('t')
r = name.count('r')
u = name.count('u')
e = name.count('e')
l = name.count('l')
o = name.count('o')
v = name.count('v')

true = (t,r,u,e)
love = (l,o,v,e)
score = int(str(sum(true))+str(sum(love)))

if score < 10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif score >= 40 and score <= 50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}.')
