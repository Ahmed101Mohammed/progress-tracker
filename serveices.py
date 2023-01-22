from data_base import project_DB

class Services:
    def __init__(self, user_name):
        self.user_name = user_name
        self.services = {
            "1": self.record_new_goal,
            # "2": self.record_progress,
            # "3": self.show_info
        }

        self.window_view()

    def window_view(self):
        the_services = " Services:\n 1. Record a new goal.\n 2. Record a progress in an old goal.\n 3. Show My Information.\n Inter the number of the serviece to choose specific one."
        print(the_services)
        self.choose_the_service()

    def choose_the_service(self):
        the_number_of_the_service = input(' Access the number of choosen service: ')
        self.services[the_number_of_the_service]()
        # try:
        #     self.services[the_number_of_the_service]()
        # except:
        #     print(' Wrong number !!!,Try again...\n')
        #     self.choose_the_service()

    def record_new_goal(self):
        user_id = project_DB.search('SELECT id FROM users WHERE name=?', self.user_name)[0][0]
        
        subject = input(' What Do you want to doing (Answer without prefix answer like: playing football or football)? ')
        subject_id = project_DB.search('SELECT id FROM subjects WHERE title=?', subject)
        if len(subject_id) == 0: self.record_new_subject(subject)
        subject_id = project_DB.search('SELECT id FROM subjects WHERE title=?', subject)[0][0]
        
        target_hours = self.get_target_hours(subject)

        project_DB.execute('INSERT INTO goals (user_id, subject_id, target_hours, progress) VALUES (?, ?, ?, ?)', user_id, subject_id, target_hours, 0)

    def record_new_subject(self, subject):
        project_DB.execute("INSERT INTO subjects (title) VALUES (?)", subject)

    def get_target_hours(self, subject):
        try:
            target_hours = float(input(' What is your target hours for ' + subject + "? "))
        except:
            print(' Print a real number, Try Again...')
            self.get_target_hours(subject)
        return target_hours


    
        
