# import user
from user import User
from post import Post

user1 = User("xxxxx@126.com", "Hook", "123456", "QA")
user1.print_user_info()
user1.change_password("111222")
user1.change_job_title("Teacher")
user1.print_user_info()

post = Post("some messages", user1.name)
post.get_post_info()