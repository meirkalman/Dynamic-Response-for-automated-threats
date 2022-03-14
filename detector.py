users_fake_db = {}
MAX_ALLOWED_PASSWORD_GUESS = 5


def detect_brute_force_password(email, password):
    if email not in users_fake_db:
        users_fake_db[email] = [password]
    elif len(users_fake_db[email]) > MAX_ALLOWED_PASSWORD_GUESS:
        return True
    else:
        users_fake_db[email].append(password)
