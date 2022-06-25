from post import Post


class User:
    def __init__(self, email, name, password, job_title):
        self.email = email
        self.name = name
        self.password = password
        self.job_title = job_title
        self.post_list = []

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.job_title = new_job_title

    def get_user_info(self):
        print(f"User's name is {self.name} works as {self.job_title}")

    def add_post(self, message):
        self.post_list.append(Post(message))

    def get_all_posts(self):
        for post in self.post_list:
            post.get_message()
