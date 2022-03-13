users_fake_db = {}


def detect_brute_force_password(email, password):
    if email not in users_fake_db:
        users_fake_db[email] = [password]
    elif len(users_fake_db[email]) > 5:
        return True
    else:
        users_fake_db[email].append(password)
