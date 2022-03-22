from datetime import datetime, timedelta
from time import sleep

password_brute_force_db = {}
dos_attack_db = {}
MAX_ALLOWED_PASSWORD_GUESS = 5
MAX_ALLOWED_REQUESTS = 5
INTERVAL_OF_TIME = 2


def detect_brute_force_password(email, password, sender_ip):
    if sender_ip not in password_brute_force_db:
        password_brute_force_db[sender_ip] = {email: [password]}
    elif email not in password_brute_force_db[sender_ip]:
        password_brute_force_db[sender_ip][email] = [password]
    elif len(password_brute_force_db[sender_ip][email]) >= MAX_ALLOWED_PASSWORD_GUESS:
        return True
    else:
        password_brute_force_db[sender_ip][email].append(password)
        return False


def detect_dos_attack(sender_ip):
    current_time = datetime.now()
    if sender_ip not in dos_attack_db:
        dos_attack_db[sender_ip] = [current_time]
    else:
        dos_attack_db[sender_ip].append(current_time)
        if len(dos_attack_db[sender_ip]) >= MAX_ALLOWED_REQUESTS:
            delta_of_time = dos_attack_db[sender_ip][len(dos_attack_db[sender_ip])-1] - \
                            dos_attack_db[sender_ip][len(dos_attack_db[sender_ip])-5]
            if delta_of_time / timedelta(minutes=1) < INTERVAL_OF_TIME:
                return True
            return False


for x in range(10):
    detect_dos_attack("sss")
