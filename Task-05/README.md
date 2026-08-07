# Grand Line Guardian

A simple terminal-based system monitor written in Python. It keeps track of running processes on the system

### Features

The program displays:

* Process ID (PID)
* Process Name
* CPU Usage
* Memory Usage
* Total Active Process Count

### How It Works

1. Reads total system memory from `/proc/meminfo`
2. Finds running processes from `/proc`
3. Reads process information from `/proc/[PID]/stat`
4. Calculates CPU usage
5. Calculates memory usage
6. Sorts processes by CPU usage
7. Displays the top 20 processes
8. Refreshes every 0.5 seconds

### Run the Program

```bash
python3 monitor.py
```

### Stop the Monitor

Press:

```text
Ctrl + C
```

to stop the program

### Resources Used

* Operating System Concepts
* Linux `/proc` documentation
* Python standard library documentation

### Concepts Learned

* Linux `/proc` filesystem
* Process monitoring
* CPU usage
* Memory usage
* Python `os`, `sys`, and `time` modules
