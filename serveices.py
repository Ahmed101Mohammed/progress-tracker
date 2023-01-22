class Services:
    def __init__(self, user_name):
        self.user_name = user_name
        self.services = {
            
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

        
