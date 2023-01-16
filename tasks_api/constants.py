# .env file constants : The saved ones should be in capital letters like
import os
from dotenv import load_dotenv

load_dotenv()
ALGORITHM = os.getenv('ALGORITHM')
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
JWT_REFRESH_SECRET_KEY = os.getenv('JWT_REFRESH_SECRET_KEY')
JWT_FORGOT_PASSWORD_SECRET_KEY = os.getenv('JWT_FORGOT_PASSWORD_SECRET_KEY')

ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
FORGOT_PASSWORD_EXPIRE_MINUTES = 10
RESET_PASSWORD_LINK = os.getenv('RESET_PASSWORD_LINK')

EMAIL_REGEX = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$"
PASSWORD_REGEX = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,12}$"

INVALID_EXPIRED_TOKEN_MSG = "Invalid/Expired Token"
USER_NOT_FOUND_OF_TOKEN_MSG = "There is no any user of this token!"

PASSWORD_RESET_SUBJECT = "Password Reset"
PASSWORD_RESET_MAIL_LINK_MSG = "click on the link below to reset your password."
PASSWORD_RESET_MAIL_MSG = "Mail is send on your email. kindly look into it."

ERR_USERNAME_WRONG = "Please enter valid username!"
ERR_PASSWORD_WRONG = "Please enter valid password!"
ERR_EMAIL_WRONG = "Please enter valid email!"
ERR_PASSWORD_INCORRECT = "Current password not matching with user password"
ERR_PASSWORD_NOT_MATCH = "Confirm Password not matching"
ERR_SQL_ALCHEMY_ERROR = "Error in storing database."
ERR_EMAIL_ALREADY_TAKEN = "The Email {} is already registered plz use another email."

MSG_REGISTER_USER_SUCCESSFULLY = "Hey {} you registered successfully."
MSG_PASSWORD_RESET = "Successfully password reset."
MSG_USER_NOT_AVAILABLE = "User with the id {} is not available"
MSG_INVALID_CREDENTIALS = "Username(Email id) not found! Invalid Credentials"
MSG_INVALID_PASSWORD = "Incorrect password"
MSG_UPDATE_PASSWORD = "Password has been changed Successfully!"
MSG_USER_CREATED = "User Created Successfully!"

MSG_TASK_LIST_NOT_FOUND = "There is no any task list of task list id {}"
MSG_TASK_LIST_UPDATED = "Task list updated Successfully"
MSG_TASK_LIST_DELETED = "Task list deleted Successfully"
EMAIL_NOT_EXIST = "Email {} does not exist!"

MSG_TASK_LIST_NOT_FOUND2 = "User have not any task list of id {}"
MSG_TASK_NOT_FOUND = "There is no any task of task id {}"
MSG_TASK_UPDATED = "Task updated Successfully"
MSG_TASK_DELETED = "Task deleted Successfully"

MSG_TASK_NOT_FOUND2 = "There is no any sub task of task id {}"
MSG_SUB_TASK_NOT_FOUND = "There is no any sub task of sub task id {}"
MSG_SUB_TASK_UPDATED = "Sub task updated Successfully"
MSG_SUB_TASK_DELETED = "Sub task deleted Successfully"

TASK_ALERT_SUBJECT = "Task alert for you Google task"
SUB_TASK_ALERT_SUBJECT = "Sub Task alert for you Google task"

TASK_ALERT_MSG_BEFORE = "This is your task notification which you had been created on given date having remaining 15m "
TASK_ALERT_MSG_CURRENT = "This is your task notification which you had been created on given date having over"
TASK_ALERT_DEADLINE_MSG = "Sorry Your Task Deadline has been Over! which you had been created on given date"

SUB_TASK_ALERT_MSG_BEFORE = "This is your task notification which you had been created on given date having remaining 15m"
SUB_TASK_ALERT_MSG_CURRENT = "This is your task notification which you had been created on given date having over"
SUB_TASK_ALERT_DEADLINE_MSG = "Sorry Your Task Deadline has been Over! which you had been created on given date"
