from datetime import datetime, timedelta
from time import sleep

password_brute_force_db = {}
dos_attack_db = {}
scraping_db = {}
MAX_ALLOWED_PASSWORD_GUESS = 5
MAX_ALLOWED_LOGIN_REQUESTS = 5
MAX_ALLOWED_SCRAPING_ATTEMPTS = 2
# amount of minutes for interval of login attempts that allowed and not detected as DOS attack
INTERVAL_OF_TIME = 2


def detect_brute_force_password(email, password, sender_ip):
    if sender_ip not in password_brute_force_db:
        password_brute_force_db[sender_ip] = {email: [password]}
    elif email not in password_brute_force_db[sender_ip]:
        password_brute_force_db[sender_ip][email] = [password]
    elif len(password_brute_force_db[sender_ip][email]) >= MAX_ALLOWED_PASSWORD_GUESS:
        return True
    else:
        if password not in password_brute_force_db[sender_ip][email]:
            password_brute_force_db[sender_ip][email].append(password)
        return False


def detect_dos_attack(sender_ip, path):
    if path != "":
        return False
    current_time = datetime.now()
    if sender_ip not in dos_attack_db:
        dos_attack_db[sender_ip] = [current_time]
    else:
        dos_attack_db[sender_ip].append(current_time)
        if len(dos_attack_db[sender_ip]) > MAX_ALLOWED_LOGIN_REQUESTS:
            delta_of_time = dos_attack_db[sender_ip][len(dos_attack_db[sender_ip]) - 1] - \
                            dos_attack_db[sender_ip][len(dos_attack_db[sender_ip]) - 5]
            if delta_of_time / timedelta(minutes=1) < INTERVAL_OF_TIME:
                return True
            return False


def detect_scraping(sender_ip, path):
    if "api/BasketItems" not in path:
        return False
    current_time = datetime.now()
    if sender_ip not in scraping_db:
        scraping_db[sender_ip] = [current_time]
    else:
        scraping_db[sender_ip].append(current_time)
        if len(scraping_db[sender_ip]) > MAX_ALLOWED_SCRAPING_ATTEMPTS:
            delta_of_time = scraping_db[sender_ip][len(scraping_db[sender_ip]) - 1] - \
                            scraping_db[sender_ip][len(scraping_db[sender_ip]) - 3]
            if delta_of_time / timedelta(minutes=1) < INTERVAL_OF_TIME:
                return True
            return False
