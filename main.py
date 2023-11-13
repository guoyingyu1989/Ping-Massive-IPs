import concurrent.futures
import threading
from ping import ping_ip
from file_io import read_ips_from_file, write_results_to_file

# 全局变量用于跟踪已完成的任务数量
completed_tasks = 0
completed_tasks_lock = threading.Lock()

def ping_ip_and_update_progress(ip_address):
    result = ping_ip(ip_address)
    # 更新已完成的任务数量，并打印进度条
    with completed_tasks_lock:
        global completed_tasks
        completed_tasks += 1
        print(f'Progress: {(completed_tasks/len(ip_addresses))*100:.2f}%')
    return result

# 使用你的文件名替换下面的字符串
ip_addresses = read_ips_from_file("ip_addresses.txt")

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(ping_ip_and_update_progress, ip_addresses))

write_results_to_file("ping_results.txt", results)
