import os
import sqlite3
app_path = os.path.dirname(os.path.abspath(__file__))
print(app_path)
con = sqlite3.connect(os.path.join(app_path, 'main.db'))