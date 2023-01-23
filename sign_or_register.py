from data_base import project_DB
from end import end_program

def sign_or_register():
    user_name = input(' What is your name: ')
    end_program.end(user_name)
    result = project_DB.search("SELECT name FROM users WHERE name = ?", user_name)
    if len(result) < 1:
        project_DB.execute("INSERT INTO users (name, hours) VALUES (?,?)", user_name, 0)
        print(" You'r a new user! Welcome with us...\n")
    else:
        sure = input(" you are not a new user, Right? (y/n) ")
        end_program.end(sure)
        if(sure == "y"):
            print(" Welcome again, I wish you have a progress in your life's goals...\n")
        else:
            print(" The name is taken before, choose a new one...")
            sign_or_register()
    return user_name
            