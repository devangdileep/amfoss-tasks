package main

import "fmt"

type process struct {
	name      string
	arrival   int
	burst     int
	wait      int
	turnround int
}

func main() {
	var ch, num int
	fmt.Println("=== Pirate King's CPU Scheduler ===")
	fmt.Println("1.FCFS  2.SJF")
	fmt.Print("Enter choice: ")
	fmt.Scan(&ch)
	fmt.Print("How many processes: ")
	fmt.Scan(&num)

	proc := make([]process, num)
	for i := 0; i < num; i++ {
		fmt.Printf("P%d -> Name, ArrivalTime, BurstTime: ", i+1)
		fmt.Scan(&proc[i].name, &proc[i].arrival, &proc[i].burst)
	}

	if ch == 1 {
		// fcfs - sorting by arrival
		for i := 0; i < num; i++ {
			for j := 0; j < num-1-i; j++ {
				if proc[j].arrival > proc[j+1].arrival {
					proc[j], proc[j+1] = proc[j+1], proc[j]
				}
			}
		}
		time := 0
		fmt.Print("\nGantt: |")
		for i := 0; i < num; i++ {
			if time < proc[i].arrival {
				time = proc[i].arrival
			}
			proc[i].wait = time - proc[i].arrival
			time = time + proc[i].burst
			proc[i].turnround = time - proc[i].arrival
			fmt.Printf(" %s |", proc[i].name)
		}
		fmt.Println()
		showResult(proc, num)

	} else if ch == 2 {
		// sjf
		finished := make([]bool, num)
		time := 0
		count := 0
		fmt.Print("\nGantt: |")
		for count < num {
			pos := -1
			small := 99999
			for i := 0; i < num; i++ {
				if finished[i] == false && proc[i].arrival <= time && proc[i].burst < small {
					small = proc[i].burst
					pos = i
				}
			}
			if pos == -1 {
				time++
				continue
			}
			proc[pos].wait = time - proc[pos].arrival
			time = time + proc[pos].burst
			proc[pos].turnround = time - proc[pos].arrival
			finished[pos] = true
			count++
			fmt.Printf(" %s |", proc[pos].name)
		}
		fmt.Println()
		showResult(proc, num)
	}
}

func showResult(proc []process, num int) {
	totWt := 0
	totTat := 0
	fmt.Println("\nName\tAT\tBT\tWT\tTAT")
	for i := 0; i < num; i++ {
		fmt.Printf("%s\t%d\t%d\t%d\t%d\n", proc[i].name, proc[i].arrival, proc[i].burst, proc[i].wait, proc[i].turnround)
		totWt = totWt + proc[i].wait
		totTat = totTat + proc[i].turnround
	}
	fmt.Printf("\nAvg Waiting Time: %.2f\n", float64(totWt)/float64(num))
	fmt.Printf("Avg Turnaround Time: %.2f\n", float64(totTat)/float64(num))
}
