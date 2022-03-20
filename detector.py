users_fake_db = {}
MAX_ALLOWED_PASSWORD_GUESS = 5


def detect_brute_force_password(email, password, sender_ip):
    if sender_ip not in users_fake_db:
        users_fake_db[sender_ip] = {email: [password]}
    elif email not in users_fake_db[sender_ip]:
        users_fake_db[sender_ip][email] = [password]
    elif len(users_fake_db[sender_ip][email]) >= MAX_ALLOWED_PASSWORD_GUESS:
        return True
    else:
        users_fake_db[sender_ip][email].append(password)
        return False
