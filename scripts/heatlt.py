import psutil
import logging
from datetime import datetime

# Set thresholds
CPU_THRESHOLD = 80
MEM_THRESHOLD = 80
DISK_THRESHOLD = 80

# Configure logging
LOG_FILE = "/var/log/system_health.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU Usage: {cpu_usage}%")
    return cpu_usage

def check_memory():
    mem = psutil.virtual_memory()
    mem_usage = mem.percent
    if mem_usage > MEM_THRESHOLD:
        logging.warning(f"High Memory Usage: {mem_usage}%")
    return mem_usage

def check_disk():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f"High Disk Usage: {disk_usage}%")
    return disk_usage

def top_processes(n=5):
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        processes.append(proc.info)
    # Sort by CPU usage descending
    top = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)[:n]
    logging.info("Top Processes:")
    for p in top:
        logging.info(f"PID {p['pid']}, Name: {p['name']}, CPU: {p['cpu_percent']}%, MEM: {p['memory_percent']:.2f}%")
    return top

def main():
    logging.info("----- System Health Check -----")
    cpu = check_cpu()
    mem = check_memory()
    disk = check_disk()
    top_processes()
    logging.info(f"Summary -> CPU: {cpu}%, Memory: {mem}%, Disk: {disk}%")
    logging.info("----- Check Complete -----\n")

if __name__ == "__main__":
    main()
