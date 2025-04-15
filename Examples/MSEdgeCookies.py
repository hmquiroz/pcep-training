import sqlite3
import json
import os

def decode_edge_cookies(cookie_file):
    # Connect to the cookies database
    conn = sqlite3.connect("file:{}?mode=ro".format(cookie_file), uri=True)
    cursor = conn.cursor()

    # Query the cookies table
    cursor.execute("SELECT * FROM cookies")
    cookies = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Convert cookies to JSON format
    json_cookies = []
    for cookie in cookies:
        json_cookie = {
            "domain": cookie[1],
            "hostOnly": bool(cookie[2]),
            "httpOnly": bool(cookie[3]),
            "name": cookie[4],
            "path": str(cookie[5]),
            "sameSite": cookie[6],
            "secure": bool(cookie[7]),
            "session": bool(cookie[8]),
            "storeId": cookie[9],
            "value": cookie[12]
        }
        if cookie[10] != 0:
            json_cookie["expirationDate"] = cookie[10]
        json_cookies.append(json_cookie)

    return json.dumps(json_cookies, indent=4)

# Path to the Edge cookies file
cookie_file = "C:\\Users\\s95830\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Network\\Cookies"

# Verify the physical file exists on disk 
assert os.path.isfile(cookie_file)

# Decode and convert cookies to JSON format
json_cookies = decode_edge_cookies(cookie_file)

# Print the JSON cookies
print(json_cookies)
