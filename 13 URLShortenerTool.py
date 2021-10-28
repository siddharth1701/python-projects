# pip install pyshorteners

import pyshorteners as sh

print("Welcome to URL Shortener")

url = input("Enter the URL: ")
# s = sh.Shortener()
# short_url = (s.tinyurl.short(url))

# print("Short URL: ", short_url)


# One-liner
print("Short URL: ",sh.Shortener().tinyurl.short(url))