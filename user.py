class User(object):
    def __init__(self, email, name, password, current_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def print_user_info(self):
        print(f"User {self.name} current job is {self.current_job_title}, you can contact by email {self.email}")

