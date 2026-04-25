import pyshorteners

s = pyshorteners.Shortener()
# making long to short
user_url = input("Enter the url to shorten:\n")
short_url = s.tinyurl.short(user_url)
print(short_url)

# making short to long
# long_url = s.tinyurl.expand("https://www.google.com")
# print(long_url)