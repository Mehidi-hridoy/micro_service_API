# reset_django_db.py
import os
import shutil
import subprocess

# --- 1️⃣ Delete old DB files ---
db_files = ['db.sqlite3', 'users_db.sqlite3']

for db_file in db_files:
    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"Deleted {db_file}")

# --- 2️⃣ Delete old migrations for user_service ---
migrations_dir = os.path.join('user_service', 'migrations')
for file in os.listdir(migrations_dir):
    if file != '__init__.py' and file.endswith('.py'):
        os.remove(os.path.join(migrations_dir, file))
        print(f"Deleted migration {file}")

# --- 3️⃣ Make migrations ---
print("\n--- Making migrations for user_service ---")
subprocess.run(['python', 'manage.py', 'makemigrations', 'user_service'])

print("\n--- Making migrations for all apps ---")
subprocess.run(['python', 'manage.py', 'makemigrations'])

# --- 4️⃣ Apply migrations ---
print("\n--- Migrating default DB ---")
subprocess.run(['python', 'manage.py', 'migrate', '--database=default'])

print("\n--- Migrating users_db ---")
subprocess.run(['python', 'manage.py', 'migrate', '--database=users_db'])

# --- 5️⃣ Create superuser for users_db ---
print("\n--- Creating superuser for users_db ---")
subprocess.run([
    'python', 'manage.py', 'createsuperuser',
    '--database=users_db'
])
