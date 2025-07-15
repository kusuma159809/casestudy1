import os
import platform

def print_system_uptime():
    system = platform.system()

    if system == "Windows":
        # On Windows, use 'net stats srv' and parse output
        try:
            output = os.popen('net stats srv').read()
            for line in output.splitlines():
                if "Statistics since" in line:
                    print("System uptime (since):", line.replace("Statistics since", "").strip())
                    return
            print("Could not determine uptime on Windows.")
        except Exception as e:
            print("Error:", e)
    else:
        # On Unix-like systems, use 'uptime -p'
        try:
            output = os.popen('uptime -p').read().strip()
            print("System uptime:", output)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    print_system_uptime()
