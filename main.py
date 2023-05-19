# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_name_0 = 'Ruud Gullit'
scorer_name_1 = 'Marco van Basten'
goal_0= 32
goal_1= 54 
scorers = scorer_name_0 + " " + str( goal_0) + "," + " " + scorer_name_1+ " " + str( goal_1)
print(scorers)

report = scorer_name_0 + " scored in the"+ " " + str(goal_0) + "nd minute" + "," + '\n' + scorer_name_1 + " wincscored in the" + " " + str(goal_1)+ "th minute"
print (report)

player = "Adrie van Tiggelen"
first_name_find= player.find("Adrie")
print(first_name_find)
second_name_find = player.find("van")
print(second_name_find)
first_name = player[0:5]
print (first_name)
last_name_len = "Adrie van Tiggelen"
print (last_name_len, len (last_name_len))
name_short = "T.v.Tiggelen"
print (name_short)
first_name_len = "Adrie"
chant = (first_name+'!'+' ') * len(first_name)
print (chant)
print (len (chant))

good_chant = chant[-2] != " "
print (good_chant)









