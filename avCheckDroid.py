import os
import time
import subprocess
import json
import re

CPU_LIMIT = 80
MEMORY_LIMIT = 85
DISK_LIMIT = 90
BATTERY_MIN = 20
NETWORK_LIMIT = 50
CHECK_INTERVAL = 2
LOG_FILE = "/data/data/com.termux/files/home/chkdroid.log"               
def log_error(message):
    with open(LOG_FILE, "a") as log:                                             log.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

def run_command(command):                                                    try:
        return subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL, universal_newlines=True).strip()
    except:
        return None

def send_notification(title, message, notif_id):
    os.system(f"termux-notification --id {notif_id} --title '{title}' --content '{message}' --priority high")

def check_cpu():
    try:
        result = run_command("top -n 1 -b")
        if result:
            match = re.search(r'CPU:\s+(\d+\.\d+)%', result)
            if match:
                usage = float(match.group(1))
                if usage > CPU_USAGE_THRESHOLD:
                    send_notification("High CPU Usage", f"CPU usage is at {usage:.2f}%", 1)
    except Exception as e:
        log_error(f"CPU Error: {e}")

def check_memory():
    try:
        result = run_command("free | grep 'Mem:'")
        if result:
            total, used = map(int, result.split()[1:3])
            usage_percent = (used / total) * 100
            if usage_percent > MEMORY_USAGE_THRESHOLD:
                send_notification("High Memory Usage", f"Memory usage is at {usage_percent:.2f}%", 2)
    except Exception as e:
        log_error(f"Memory Error: {e}")

def check_disk():
    try:
        result = run_command("df -h /data | tail -n 1")
        if result:
            used_percent = int(result.split()[4].replace('%', ''))
            if used_percent > DISK_USAGE_THRESHOLD:
                send_notification("High Disk Usage", f"Disk usage is at {used_percent}%", 3)
    except Exception as e:
        log_error(f"Disk Error: {e}")

def check_battery():
    try:
        result = run_command("termux-battery-status")
        if result:
            battery_info = json.loads(result)
            percent = battery_info.get("percentage", 0)
            plugged = battery_info.get("plugged", False)
            if percent < BATTERY_LOW_THRESHOLD and not plugged:
                send_notification("Low Battery", f"Battery is at {percent}%", 4)
            elif plugged and percent >= 100:
                send_notification("Battery Fully Charged", "You can unplug your charger.", 4)
    except Exception as e:
        log_error(f"Battery Error: {e}")

def check_network():
    try:
        net_before = run_command("cat /proc/net/dev | grep wlan0")
        time.sleep(1)
        net_after = run_command("cat /proc/net/dev | grep wlan0")
        if net_before and net_after:
            recv_before = int(net_before.split()[1])
            recv_after = int(net_after.split()[1])
            download_speed = (recv_after - recv_before) / 1024
            if download_speed < NETWORK_LOW_SPEED:
                send_notification("Low Network Speed", f"Download: {download_speed:.2f} KB/s", 5)
    except Exception as e:
        log_error(f"Network Error: {e}")

def monitor_system():
    os.system("clear")
    print("""

               _____ _     _    _____            _     _
              / ____| |   | |  |  __ \          (_)   | |
   __ ___   _| |    | |__ | | _| |  | |_ __ ___  _  __| |
  / _` \ \ / / |    | '_ \| |/ / |  | | '__/ _ \| |/ _` |
 | (_| |\ V /| |____| | | |   <| |__| | | | (_) | | (_| |
  \__,_| \_/  \_____|_| |_|_|\_\_____/|_|  \___/|_|\__,_|



    """)
    print("Monitoring system health...\n")
    print("Will notify if limits are breached:")
    print(f"CPU > {CPU_LIMIT}%, Memory > {MEMORY_LIMIT}%, Disk > {DISK_LIMIT}%, Battery < {BATTERY_MIN}%, Network < {NETWORK_LIMIT} KB/s\n")
    print("Made w/ <3 by Avery")
    send_notification("System Monitor Started", "Monitoring your device health...", 0)
    while True:
        try:
            check_cpu()
            check_memory()
            check_disk()
            check_battery()
            check_network()
        except Exception as e:
            log_error(f"General Error: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_system()
