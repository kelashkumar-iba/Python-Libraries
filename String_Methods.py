# 1) Upper

text = "hello, world!"
upper_text = text.upper()
print(upper_text)  # Output: HELLO, WORLD!


# 2) Lower

text = "Hello, World!"
lower_text = text.lower()
print(lower_text)  # Output: hello, world!


# 3) Strip
# Removes whitespace

text = "   Hello, World!   "
stripped_text = text.strip()
print(f"{stripped_text}")  # Output: Hello, World!
# Also Left and Right methods: lstrip, rstrip.


# 4) Replace

text = "Hello, World!"
replaced_text = text.replace("World", "Python")
print(replaced_text)  # Output: Hello, Python!


# 5) Split

text = "Hello, World!"
split_text = text.split(", ")
print(split_text)  # Output: ['Hello', 'World!']
# Split converts the text into a list of strings

# 6) Find

text = "Hello, World!"
index = text.find("World")
print(index)  # Output: 7

# 7) Capitalize

text = "hello, world!"
capitalized_text = text.capitalize()
print(capitalized_text)  # Output: Hello, world!


# 8) Title

text = "hello, world!"
title_text = text.title()
print(title_text)  # Output: Hello, World!

# 9) Join

text = ["Hello", "World"]
joined_text = " ".join(text)
print(joined_text)  # Output: Hello World

# 10) isdigit

text = "123"
is_digit = text.isdigit()
print(is_digit)  # Output: True
