import re
text="Hello! My name is Aryan Patel, and I was born on 14/02/2000. I currently live in Ahmedabad, Gujarat. You can reach me at aryan.patel007@gmail.com or aryan@company.co.in. My backup email is contact_me123@yahoo.com. I usually work from 9:00 AM to 5:30 PM, Monday to Friday. My contact numbers are: +91-9876543210, 079-26543210, and (123)-456-7890. My website: https://www.aryanpatel.dev and my blog: http://blog.aryanwrites.com I recently bought these items: 1. USB Cable - ₹299 2. Bluetooth Speaker - ₹1,299 3. Monitor Stand - ₹899 Meeting scheduled on: 04-04-2025, 2025/04/10, and April 15, 2025."
pattern = r"\d{10}|\(\d{3}\)-\d{3}-\d{4}"
pattern2 = r"[a-zA-z0-9_]*@[a-zA-Z0-9]*\.com|[a-zA-z0-9_]*@[a-zA-Z0-9]*\.co.in"
matches = re.findall(pattern2,text)
print(matches)