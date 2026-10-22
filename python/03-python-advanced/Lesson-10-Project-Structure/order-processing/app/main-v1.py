from app.config.settings import Settings
from app.utils.helpers import format_currency


settings = Settings()

print(settings.api_key)

print(format_currency(23343.99))
print(format_currency(25999))