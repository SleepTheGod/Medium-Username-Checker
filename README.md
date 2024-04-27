# Medium-Username-Checker
This tool will automate a way to check Medium.com usernames that are not taken at a mass scale


How the Script Works

The script reads usernames from wordlist.txt.
For each username, it makes a GET request to https://medium.com/@username.
If the response status code is 404, the username is considered available.
The script collects all available usernames and writes them to make.txt.

Notes

Rate Limiting and Compliance: This script does not implement any delay between requests, which might lead to IP blocking by Medium due to aggressive behavior. Use with caution.
Proxy Usage: If you're concerned about privacy or IP blocking, consider using proxies. However, managing proxies goes beyond this simple script and can complicate matters significantly, especially in terms of legality and ethical usage.
Legality and Ethics: Always ensure that your actions comply with the website's terms of service. This script is for educational purposes, and you should use it responsibly.
This script provides a basic structure. Depending on your specific needs and the scale of your operations, consider implementing additional features such as concurrent requests using threading or asyncio for efficiency, or using rotating proxies if you are doing extensive scanning.

How to install this tool 

This tool requires a wordlist of common words that you will have to find yourself

git clone https://github.com/SleepTheGod/Medium-Username-Checker/


cd Medium-Username-Checker

pip install -r requirements.txt

chmod +x main.py

nano wordlist.txt  (this command will allow you to add the list you want and paste it)

ctrl +x to save the wordlist you just added

now we type ./main.py to make the script run yes it has to be "./main.py"
