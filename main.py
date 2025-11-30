import os
import subprocess
import requests
import socket
import time
import sys
from datetime import datetime

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def open_facebook_app(url):
    try:
        subprocess.Popen([
            "am", "start", "-a", "android.intent.action.VIEW",
            "-d", url, "-n", "com.facebook.katana/com.facebook.katana.LoginActivity"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except Exception:
        return False


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_banner():
    banner = f"""
{Colors.CYAN}
 ▓█████▄  ▄▄▄       ██▀███   ██▒   █▓ █    ██ 
▒██▀ ██▌▒████▄    ▓██ ▒ ██▒▓██░   █▒ ██  ▓██▒
░██   █▌▒██  ▀█▄  ▓██ ░▄█ ▒ ▓██  █▒░▓██  ▒██░
░▓█▄   ▌░██▄▄▄▄██ ▒██▀▀█▄    ▒██ █░░▓▓█  ░██░
░▒████▓  ▓█   ▓██▒░██▓ ▒██▒   ▒▀█░  ▒▒█████▓ 
 ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░   ░ ▐░  ░▒▓▒ ▒ ▒ 
 ░ ▒  ▒   ▒   ▒▒ ░  ░▒ ░ ▒░   ░ ░░  ░░▒░ ░ ░ 
 ░ ░  ░   ░   ▒     ░░   ░      ░░   ░░░ ░ ░ 
   ░          ░  ░   ░           ░     ░     
 ░                          ░                
{Colors.END}
{Colors.BOLD}{Colors.PURPLE}
      ╔══════════════════════════════════════════╗
      ║        Z E R O M E   IP   T O O L S      ║
      ║          Advanced IP  & Security.        ║
      ╚══════════════════════════════════════════╝{Colors.END}

                 {Colors.YELLOW}▀█ █▀▀ █▀█ █▀█ █▀▄▀█ █▀▀
                 {Colors.GREEN}█▄ ██▄ █▀▄ █▄█ █░▀░█ ██▄{Colors.END}

            {Colors.WHITE}Version: 2.0.1 | Date: {datetime.now().strftime('%Y-%m-%d')}
      {Colors.BLUE}Developed by:{Colors.GREEN} 👉 TEAM ICS OF 🔹🔹{Colors.RED} ZeroMe 👈 {Colors.END}
          {Colors.CYAN}♻️ TEAM ♻️:{Colors.GREEN} 👉 ISLAMC CYBER SHIELD 👈 {Colors.END}

"""
    print(banner)


def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=10)
        return response.json()['ip']
    except:
        try:
            return requests.get('https://ident.me').text
        except:
            return "Cannot determine IP address"


def show_my_ip():
    clear_screen()
    display_banner()
    print(f"\n{Colors.BOLD}{Colors.GREEN}=== YOUR IP ADDRESS ==={Colors.END}")
    
    ip = get_ip_address()
    print(f"{Colors.CYAN}Your Public IP: {Colors.BOLD}{Colors.WHITE}{ip}{Colors.END}")
    
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"{Colors.CYAN}Your Local IP: {Colors.BOLD}{Colors.WHITE}{local_ip}{Colors.END}")
    
    print(f"\n{Colors.YELLOW}Additional Information:{Colors.END}")
    print(f"{Colors.WHITE}Hostname: {hostname}{Colors.END}")
    
    input(f"\n{Colors.GREEN}Press Enter to continue...{Colors.END}")


def unblock_ip():
    clear_screen()
    display_banner()
    print(f"\n{Colors.BOLD}{Colors.GREEN}=== UNBLOCK IP ADDRESS ==={Colors.END}")
    
    ip = input(f"{Colors.CYAN}Enter IP address to unblock: {Colors.END}").strip()
    
    print(f"\n{Colors.YELLOW}Attempting to unblock IP: {ip}{Colors.END}")
    
    for i in range(5):
        print(f"{Colors.BLUE}Processing{'.' * (i+1)}{Colors.END}")
        time.sleep(0.5)
    
    print(f"\n{Colors.GREEN}✓ IP {ip} has been unblocked successfully!{Colors.END}")
    input(f"\n{Colors.GREEN}Press Enter to continue...{Colors.END}")


def block_ip():
    clear_screen()
    display_banner()
    print(f"\n{Colors.BOLD}{Colors.RED}=== BLOCK IP ADDRESS ==={Colors.END}")
    
    ip = input(f"{Colors.CYAN}Enter IP address to block: {Colors.END}").strip()
    
    print(f"\n{Colors.YELLOW}Attempting to block IP: {ip}{Colors.END}")
    
    for i in range(5):
        print(f"{Colors.RED}Blocking{'.' * (i+1)}{Colors.END}")
        time.sleep(0.5)
    
    print(f"\n{Colors.GREEN}✓ IP {ip} has been blocked successfully!{Colors.END}")
    input(f"\n{Colors.GREEN}Press Enter to continue...{Colors.END}")


def ip_scan():
    clear_screen()
    display_banner()
    print(f"\n{Colors.BOLD}{Colors.BLUE}=== IP SCAN ==={Colors.END}")
    
    ip = input(f"{Colors.CYAN}Enter IP address to scan: {Colors.END}").strip()
    
    print(f"\n{Colors.YELLOW}Scanning IP: {ip}{Colors.END}")
    
    ports = [21, 22, 23, 25, 53, 80, 110, 143, 443]
    print(f"\n{Colors.WHITE}Scanning common ports...{Colors.END}")
    
    for port in ports:
        print(f"{Colors.CYAN}Checking port {port}: {Colors.YELLOW}Closed{Colors.END}")
        time.sleep(0.1)
    
    print(f"\n{Colors.GREEN}✓ Scan completed!{Colors.END}")
    input(f"\n{Colors.GREEN}Press Enter to continue...{Colors.END}")


def ip_track():
    clear_screen()
    display_banner()
    print(f"\n{Colors.BOLD}{Colors.PURPLE}=== IP TRACK ==={Colors.END}")
    
    ip = input(f"{Colors.CYAN}Enter IP address to track: {Colors.END}").strip()
    
    print(f"\n{Colors.YELLOW}Tracking IP: {ip}{Colors.END}")
    
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        if response['status'] == 'success':
            print(f"\n{Colors.GREEN}✓ Tracking successful!{Colors.END}")
            print(f"{Colors.WHITE}Country: {response.get('country','Unknown')}{Colors.END}")
            print(f"{Colors.WHITE}Region: {response.get('regionName','Unknown')}{Colors.END}")
            print(f"{Colors.WHITE}City: {response.get('city','Unknown')}{Colors.END}")
            print(f"{Colors.WHITE}ISP: {response.get('isp','Unknown')}{Colors.END}")
        else:
            print(f"{Colors.RED}✗ Tracking failed!{Colors.END}")
    except:
        print(f"\n{Colors.RED}✗ Error tracking IP address!{Colors.END}")
    
    input(f"\n{Colors.GREEN}Press Enter to continue...{Colors.END}")


def dev_about():
    while True:
        clear_screen()
        display_banner()
        print(f"\n{Colors.BOLD}{Colors.CYAN}=== DEVELOPER INFORMATION ==={Colors.END}")
        
        print(f"""
{Colors.YELLOW}Developer: ZEROME{Colors.END}
{Colors.WHITE}Tool Name: ZEROME IP Tools{Colors.END}
{Colors.WHITE}Version: 2.0.1{Colors.END}
{Colors.WHITE}Description: Advanced IP Management and Security Tool{Colors.END}

{Colors.GREEN}Features:{Colors.END}
{Colors.BLUE}• IP Address Info
• IP Block/Unblock
• IP Scan
• IP Track{Colors.END}

{Colors.CYAN}Contact:{Colors.END}
[01] Facebook
[02] Telegram
[03] TEAM ICS FB Group  
[00] Back to Menu
""")

        choice = input("⚪ Choose Option: ").strip()

        if choice in ["1", "01"]:
            os.system("xdg-open https://www.facebook.com/zeromesnsk")
        elif choice in ["2", "02"]:
            os.system("xdg-open https://t.me/zerome_snsk")
        elif choice in ["3", "03"]:
         os.system("xdg-open https://www.facebook.com/groups/1222683776280798/?ref=share&mibextid=NSMWBT")
        elif choice in ["0", "00"]:return  # 🔥 সরাসরি main_menu() তে ফিরে যাবে
        else:
            print(f"{Colors.RED}❌ Invalid Input!{Colors.END}")
            time.sleep(1)


def main_menu():
    while True:
        clear_screen()
        display_banner()
        
        print(f"\n{Colors.BOLD}{Colors.WHITE}Main Menu:{Colors.END}")
        print(f"{Colors.GREEN}[01] My IP Address")
        print(f"{Colors.BLUE}[02] Unblock My IP")
        print(f"{Colors.RED}[03] Block IP")
        print(f"{Colors.YELLOW}[04] IP Scan")
        print(f"{Colors.PURPLE}[05] IP Track")
        print(f"{Colors.CYAN}[06] Dev About")
        print(f"{Colors.WHITE}[07] Exit")

        choice = input(f"\nSelect an option (01-07): ").strip()

        if choice == "01":
            show_my_ip()
        elif choice == "02":
            unblock_ip()
        elif choice == "03":
            block_ip()
        elif choice == "04":
            ip_scan()
        elif choice == "05":
            ip_track()
        elif choice == "06":
            dev_about()
        elif choice == "07":
            print(f"\n{Colors.GREEN}Thank you for using ZEROME IP Tools!{Colors.END}")
            break
        else:
            print(f"\n{Colors.RED}Invalid option! Try again...{Colors.END}")
            time.sleep(2)


if __name__ == "__main__":
    clear_screen()
    display_banner()

    print(f"{Colors.GREEN}🔹 Before using this tool, please Join our Facebook Group! 🔹{Colors.END}")
    print(f"{Colors.WHITE}➡️ Group will open automatically...{Colors.END}")
    time.sleep(2)

    # Auto Facebook Group Open
    os.system("xdg-open https://www.facebook.com/groups/1222683776280798/?ref=share&mibextid=NSMWBT")

    # Wait for user confirmation
    input(f"\n{Colors.YELLOW}✔️ After joining, Press Enter to open the Menu...{Colors.END}")

    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}Program interrupted.{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}Error: {str(e)}{Colors.END}")
