import requests

def is_username_available(username):
    url = f"https://medium.com/@{username}"
    response = requests.get(url)
    return response.status_code == 404

def main():
    available_usernames = []
    try:
        with open('wordlist.txt', 'r') as file:
            usernames = file.read().splitlines()
    except FileNotFoundError:
        print("Error: The file 'wordlist.txt' does not exist.")
        return

    for username in usernames:
        if is_username_available(username):
            print(f"{username} is available!")
            available_usernames.append(username)
        else:
            print(f"{username} is not available.")
    
    with open('make.txt', 'w') as file:
        for username in available_usernames:
            file.write(username + "\n")

    print(f"Available usernames have been written to make.txt")

if __name__ == '__main__':
    main()
