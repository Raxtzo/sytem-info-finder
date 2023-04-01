import socket
import psutil
import GPUtil
import wmi
import colorama

# Initialize colorama for colored output
colorama.init()

# Get system information
hostname = socket.gethostname()
cpu_count = psutil.cpu_count(logical=False)
cpu_freq = psutil.cpu_freq().current
cpu_percent = psutil.cpu_percent()
gpus = GPUtil.getGPUs()
gpu_name = gpus[0].name
gpu_mem = gpus[0].memoryTotal
mem = psutil.virtual_memory()
ram_total = mem.total
wmi_obj = wmi.WMI()
baseboard = wmi_obj.Win32_BaseBoard()[0]
mb_manufacturer = baseboard.Manufacturer
mb_model = baseboard.Product
mb_serial_number = baseboard.SerialNumber

# Define colors for output
green = colorama.Fore.GREEN
yellow = colorama.Fore.YELLOW
red = colorama.Fore.RED
blue = colorama.Fore.BLUE
reset = colorama.Style.RESET_ALL

# Print system information
print(f"{green}  {hostname}")
print(f"{red}  CPU: {cpu_count} cores @ {cpu_freq} MHz ({cpu_percent}%)")
print(f"{blue}  GPU: {gpu_name} ({gpu_mem} MB)")
print(f"{green}  RAM: {ram_total // (1024 ** 3)} GB")
print(f"{yellow}  Motherboard: {mb_manufacturer} {mb_model} ({mb_serial_number})")
print(reset)
