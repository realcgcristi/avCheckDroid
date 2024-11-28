---

# avCheckDroid

## That one check light Python script for PC, kinda ported to mobile

A simple yet effective script that monitors various system metrics such as CPU usage, memory, disk, battery, and network speed. Initially created for desktop environments, it has been ported and optimized for Android through Termux. Perfect for monitoring your mobile device's health in real-time.


---

# Features:

CPU Usage Monitoring: Alerts when CPU usage exceeds 80%.

Memory Usage Monitoring: Notifies when RAM usage surpasses 85%.

Disk Usage Monitoring: Alerts when disk usage crosses 90%.

Battery Monitoring: Sends alerts when battery is below 20%.

Network Monitoring: Notifies if network download speed falls below 50 KB/s.

Real-time Monitoring: Continuously checks system health every 2 seconds.



---

# Requirements:

Termux: A Linux environment for Android, required for running the script.

Python 3: The script is written in Python and requires Python 3 to run.

termux-notification: Used for sending system notifications (installed in Termux by default).

termux-battery-status: For battery status checks, available via Termux.



---

# Installation:

1. Install Termux and Termux:API from F-Droid </br>
-> https://f-droid.org/packages/com.termux </br>
-> https://f-droid.org/packages/com.termux.api/

2. Set Up Python 3 and Dependencies

After installing Termux, open the app and run the following commands to set up Python and other dependencies:

``pkg update`` </br>
``pkg install python`` </br>
``pkg install termux-api`` </br>


3. Clone the Repository or Download the Script

Clone this repository or download the script directly:

``git clone`` </br>
``https://github.com/realcgcristi/avCheckDroid.git`` </br>
``cd avCheckDroid`` </br>

4. Grant Necessary Permissions

Make sure Termux has permission to send notifications and access the necessary system information. If not already set up, run:

``pkg install termux-api``

5. Run the Script

Once everything is set up, you can run the script using:

``python3 avCheckDroid.py``


---

# How it Works:

The script continuously checks the health of your device's CPU, memory, disk, battery, and network every 2 seconds.

It sends real-time notifications if any of these metrics exceed preset thresholds (e.g., CPU usage over 80%, battery below 20%).

Logs any errors to a local file (chkdroid.log) for debugging and record-keeping.



---

# Configuration:

You can easily configure the thresholds for each system metric by modifying the values in the script:

``CPU_USAGE_THRESHOLD = 80        # CPU usage threshold in percentage
MEMORY_USAGE_THRESHOLD = 85     # Memory usage threshold in percentage
DISK_USAGE_THRESHOLD = 90       # Disk usage threshold in percentage
BATTERY_LOW_THRESHOLD = 20      # Battery low threshold in percentage
NETWORK_LOW_SPEED = 50          # Minimum network speed in KB/s
CHECK_INTERVAL = 2              # Interval to check metrics (in seconds)``

