# from collections import ChainMap

# default_config = {
#     "timeout": 30,
#     "language": "en",
#     "theme": "light"
# }

# user_config = {
#     "timeout": 60,
#     "theme": "dark"
# }

# config = ChainMap(user_config, default_config)

# print(config["timeout"])
# print(config["language"])
# print(config["theme"])

from collections import ChainMap

default_config = {
    "timeout": 30,
    "language": "en",
    "theme": "light"
}

user_config = {
    "timeout": 60
}

config = ChainMap(user_config, default_config)

print("Timeout:", config["timeout"])
print("Language:", config["language"])
print("Theme:", config["theme"])