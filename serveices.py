import re
from data_base import project_DB

class Services:
    def __init__(self, user_name):
        self.user_name = user_name
        self.services = {
            "1": self.record_new_goal,
            "2": self.record_progress,
            # "3": self.show_info
        }

        self.window_view()

    def window_view(self):
        the_services = " Services:\n 1. Record a new goal.\n 2. Record a progress in an old goal.\n 3. Show My Information.\n Inter the number of the serviece to choose specific one."
        print(the_services)
        self.choose_the_service()

    def choose_the_service(self):
        the_number_of_the_service = input(' Access the number of choosen service: ')
        try:
            self.services[the_number_of_the_service]()
        except:
            print(' Wrong number !!!,Try again...\n')
            self.choose_the_service()

    def record_new_goal(self):
        user_id = project_DB.search('SELECT id FROM users WHERE name=?', self.user_name)[0][0]
        
        subject = input(' What Do you want to doing (Answer without prefix answer like: playing football or football)? ')
        subject_id = project_DB.search('SELECT id FROM subjects WHERE title=?', subject)
        if len(subject_id) == 0: self.record_new_subject(subject)
        subject_id = project_DB.search('SELECT id FROM subjects WHERE title=?', subject)[0][0]
        
        target_hours = self.get_target_hours(subject)

        project_DB.execute('INSERT INTO goals (user_id, subject_id, target_hours, progress) VALUES (?, ?, ?, ?)', user_id, subject_id, target_hours, 0)
        print(" Your goal is Added \n")
        return self.window_view()

    def record_new_subject(self, subject):
        project_DB.execute("INSERT INTO subjects (title) VALUES (?)", subject)

    def get_target_hours(self, subject):
        try:
            target_hours = float(input(' What is your target hours for ' + subject + "? "))
        except:
            print(' Print a real number, Try Again...')
            self.get_target_hours(subject)
        return target_hours

    def record_progress(self):
        self.show_user_goals()
        goal_id = self.get_goal_id()
        progress_hours = self.get_progress_hours()
        comment = input(" Add your comment about these hours: ")
        self.record_progress_in_db(goal_id, progress_hours, comment)
        print("Your update is done...\n")
        return self.window_view()


    def show_user_goals(self):
        goals = project_DB.search('SELECT goals.id, subjects.title, goals.target_hours, goals.progress FROM goals JOIN subjects ON goals.subject_id = subjects.id JOIN users ON goals.user_id = users.id WHERE users.name = ?', self.user_name)
        if(len(goals) == 0):
            print("You do not have any goal, Try to record new goal.")
            return self.window_view()

        for goal in goals:
            print("- Goal id: " + str(goal[0]) + "\n  Goal Subject: "+ goal[1] + "\n  Goal hours target: " + str(goal[2]) + "\n  Your achievement: " + str(goal[3] * 100 / goal[2])+ "%")

    def get_goal_id(self):
        try:
            goal_id = int(input(' Enter the id of the goal that you achieave a progress in: ' ))
        except:
            print(" Wrong Number, Try Again...")
            return self.get_goal_id()

        goal = project_DB.search('SELECT id FROM goals WHERE id = ?', goal_id)
        if len(goal) == 0:
            print(" You do not have any goal with this Id, Try again...");
            return self.get_goal_id()
        
        return goal_id

    def get_progress_hours(self):
        try:
            progress_hours = float(input(' How much hours did you invest in your goal? '))
            return progress_hours
        except:
            print(" Wrong number, Try again...")
            return self.get_progress_hours()

    def record_progress_in_db(self, goal_id, hours_progress, comment):
        project_DB.execute("INSERT INTO commits (goal_id, hours, comment) VALUES (?, ?, ?)", goal_id, hours_progress, comment)

        hours_achieved = project_DB.search("SELECT progress FROM goals WHERE id = ?", goal_id)[0][0]
        project_DB.execute("UPDATE goals SET progress = ? WHERE id = ?", (hours_progress + hours_achieved), goal_id)

        hours_invested = project_DB.search("SELECT hours FROM users WHERE name = ?", self.user_name)[0][0]
        project_DB.execute("UPDATE users SET hours = ? WHERE name = ?", (hours_progress + hours_invested), self.user_name)

    
        
