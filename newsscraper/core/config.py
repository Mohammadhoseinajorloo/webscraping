from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")
    RAJA_URL = os.getenv("RAJA_URL")
    ASRIRAN_URL = os.getenv("ASRIRAN_URL")
    LOG_FILE = os.getenv("LOG_FILE")


settings = Settings()
