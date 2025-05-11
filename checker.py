import requests
import json
import os

# Made by Vyxon
class V:
    def __init__(self, cookie: str):
        self.url = "https://usermoderation.roblox.com/v1/not-approved"
        self.session = requests.Session()
        self.session.headers.update({
            "accept": "application/json, text/plain, */*",
            "origin": "https://www.roblox.com",
            "referer": "https://www.roblox.com/",
            "user-agent": "Mozilla/5.0",
            "cookie": cookie
        })
    # Made by Vyxon
    def cc(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    # Made by Vyxon
    def cs(self):
        try:
            response = self.session.get(self.url)
            if response.status_code != 200:
                # print(f"[ERROR] HTTP {response.status_code}")
                return

            text = response.text
            data = json.loads(text)
            rows = []

            if "delete" in text.lower() and text.upper():
                rows.append(["[WRN] Warning", "Next Ban is a Termination\n"])
            else:
                rows.append(["[INF] Status", "Next ban is not termination-related\n"])

            for key, value in data.items():
                formatted_value = json.dumps(value) if isinstance(value, (dict, list)) else str(value)
                rows.append([key.title(), formatted_value])

            self.cc()
            for label, val in rows:
                print(f"{label:<25} | {val}")

        except Exception as e:
            print(f"[ERROR] {str(e)}")
# Made by Vyxon
if __name__ == "__main__":
    # Account Cookie
# Made by Vyxon
    COOKIE = ""
    V(COOKIE).cs()
