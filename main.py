from data_base import project_DB
from data_base_structure import data_structure
from sign_or_register import sign_or_register
# create the base of dataBase of the program:
project_DB.excute_data_base_structure(data_structure)

# welcome window:
welcome_sentence = "\n Welcome My Boy to progress tracker program.\n This program will help you to tracke your progress in your goals.\n You will select the thing that you want to do,\n and number of hours you want to do the thing in it.\n Like 10000 hours for learning some thing you want to be legend in it\n Or 20 hours for soft skill...\n You can start now...\n "
print(welcome_sentence)

# sign Or register:

sign_or_register()