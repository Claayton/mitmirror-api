import os
from dotenv import load_dotenv

load_dotenv()

email_infos = {
    'email': os.getenv('EMAIL_MITMIRROR_TESTS'),
    'password': os.getenv('PASSWORD_MITMIRROR_TESTS')
}
