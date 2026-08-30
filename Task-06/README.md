# Pirate King's CPU Scheduler

This is a simple CPU scheduling simulator made in Golang. I made this as my mini project to understand how OS schedules processes. The theme is based on One Piece pirate crews.

## What it does

It takes process details (name, arrival time, burst time) and runs one of these scheduling algorithms:
- FCFS (First Come First Serve)
- SJF (Shortest Job First - Non Preemptive)

Then it shows a gantt chart and calculates waiting time and turnaround time for each process.

## How to run

go run main.go

## Formulas used

- Turnaround Time = Completion Time - Arrival Time
- Waiting Time = Turnaround Time - Burst Time

## Resources

- https://gobyexample.com - for learning go basics
- https://www.geeksforgeeks.org/cpu-scheduling-in-operating-systems/ - for understanding the algorithms
- https://go.dev/tour - go syntax

## What I learned

- How to use structs in golang
- Taking input using fmt.Scan
- Bubble sort for sorting
- How FCFS and SJF actually work
- Difference between preemptive and non preemptive