import os
import subprocess

# B105: Hardcoded password (Bandit will catch this)
password = "SuperSecret123!"

# B608: SQL Injection (Bandit will flag this)
def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return query

# B602: Shell injection via subprocess (Bandit catches this)
def run_command(user_input):
    subprocess.call(user_input, shell=True)

# B303: Weak hash (MD5 is broken)
import hashlib
def hash_password(pwd):
    return hashlib.md5(pwd.encode()).hexdigest()

# B110: Try-except-pass hides errors (security smell)
try:
    risky_operation()
except:
    pass
