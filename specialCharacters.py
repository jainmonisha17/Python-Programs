text = "Hello@123!"
special_chars = [ch for ch in text if not ch.isalnum()]
print(special_chars)   # ['@', '!']
