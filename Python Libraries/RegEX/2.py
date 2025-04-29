import re
text = "Hello. My name is Aryan Shah. I have an issue with my order. The reference number is order # 901451941. My friend also has an issue. His order number is 1234567890"
pattern = r"order [^\d]*(\d*)"
matches = re.findall(pattern,text)
print(matches)