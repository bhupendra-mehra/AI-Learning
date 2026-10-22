
from config import Settings


load_dotenv()

settings = Settings()

print(settings.app_name)
print(settings.debug)
print(settings.api_key)