import os
import sys
import time

def get_total_system_memory():
    try:
        with open('/proc/meminfo', 'r') as f:
            for line in f:
                if line.startswith('MemTotal:'):
                    return int(line.split()[1]) * 1024
    except Exception:
        pass
    return 1


def read_single_process_info(pid, total_system_memory, previous_cpu_ticks, time_delta):
    stat_path = f"/proc/{pid}/stat"

    with open(stat_path, 'r') as f:
        content = f.read()

    left_paren = content.find('(')
    right_paren = content.rfind(')')

    process_name = content[left_paren + 1:right_paren]
    rest_of_fields = content[right_paren + 2:].split()

    user_time_ticks = float(rest_of_fields[11])
    kernel_time_ticks = float(rest_of_fields[12])
    total_cpu_ticks = user_time_ticks + kernel_time_ticks

    rss_pages = int(rest_of_fields[21])
    memory_bytes = rss_pages * 4096

    previous_ticks = previous_cpu_ticks.get(pid, total_cpu_ticks)
    ticks_difference = total_cpu_ticks - previous_ticks
    previous_cpu_ticks[pid] = total_cpu_ticks

    cpu_usage_percent = (ticks_difference / 100.0) / time_delta * 100.0
    memory_usage_percent = (memory_bytes / total_system_memory) * 100.0

    return {
        'pid': pid,
        'name': process_name,
        'cpu': max(0.0, cpu_usage_percent),
        'mem': max(0.0, memory_usage_percent)
    }


def get_all_processes(total_system_memory, previous_cpu_ticks, last_sample_time):
    current_time = time.time()
    time_delta = max(0.001, current_time - last_sample_time)

    processes = []
    all_proc_entries = os.listdir('/proc')

    for entry in all_proc_entries:
        if entry.isdigit():
            pid = int(entry)
            try:
                proc_info = read_single_process_info(pid, total_system_memory, previous_cpu_ticks, time_delta)
                processes.append(proc_info)
            except Exception:
                continue

    processes.sort(key=lambda item: item['cpu'], reverse=True)
    return processes, current_time


def main():
    total_system_memory = get_total_system_memory()
    previous_cpu_ticks = {}
    last_sample_time = time.time()

    refresh_interval_seconds = 0.5

    try:
        while True:
            processes, last_sample_time = get_all_processes(total_system_memory, previous_cpu_ticks, last_sample_time)

            if '--test' not in sys.argv:
                os.system('clear')

            print("Total Active Process Count:", len(processes))
            print("=" * 60)
            print(f"{'PID':>8}   {'PROCESS NAME':<25}   {'CPU %':>7}   {'MEM %':>7}")
            print("-" * 60)

            for proc in processes[:20]:
                print(f"{proc['pid']:>8}   {proc['name'][:25]:<25}   {proc['cpu']:>7.1f}   {proc['mem']:>7.1f}")

            if '--test' in sys.argv:
                break

            time.sleep(refresh_interval_seconds)

    except KeyboardInterrupt:
        print("\nStopped process monitor.")


if __name__ == '__main__':
    main()
