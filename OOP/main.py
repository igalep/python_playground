from user import User

user_1 = User("aa@aa.com" , "Igal Ep", "12346", "Eng")
user_1.get_user_info()
user_1.add_post("I'm a Eng !!")

user_1.change_job_title("Director")
user_1.get_user_info()
user_1.add_post("I'm a Director !!")

user_1.get_all_posts()


