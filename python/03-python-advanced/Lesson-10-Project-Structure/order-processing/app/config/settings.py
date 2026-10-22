from dotenv import load_dotenv
import os

load_dotenv()

class Settings:


    app_name:str = os.getenv(
        "APP_NAME",
        "order_processing"
    )


    debug:bool = os.getenv(
        "DEBUG",
        "false"
    ).lower() == "true"


    api_key:str | None = os.getenv("API_KEY")


