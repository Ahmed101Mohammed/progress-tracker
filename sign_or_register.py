import imp


from data_base import project_DB

def sign_or_register():
    user_name = input(' What is your name: ')
    result = project_DB.search("SELECT name FROM users WHERE name = ?", user_name)
    if len(result) < 1:
        project_DB.execute("INSERT INTO users (name, hours) VALUES (?,?)", user_name, 0)
        print(" You'r a new user! Welcome with us...")
    else:
        sure = input(" you are not a new user, Right? (y/n) ")
        if(sure == "y"):
            print(" Welcome again, I wish you have a progress in your life's goals...")
        else:
            print(" The name is taken before, choose a new one...")
            sign_or_register()
            