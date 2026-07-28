# One Piece Terminal Adventure

## Level 1 

### Objective
Find the real **Gito Gito no Mi** among the Devil Fruit files.

### Steps
1. Listed all the Devil Fruit files in the reef sectors.
2. Checked file details and compared contents across sectors.
3. Read the `eat.sh` script to understand how it checks the fruit file.
4. Confirmed that `eat.sh` validates if the file has write permissions (`-w`).
5. Passed `sector_C/devil_fruit_6.txt` into `eat.sh` to obtain the Level 1 flag.

### Correct File
`sector_C/devil_fruit_6.txt`

### Level 1 Flag
`ONE_PIECE{GITO_GITO_NO_AWAKENING}`

### Commands Used
- `find . -name "devil_fruit_*.txt"` – Lists all Devil Fruit files.
- `find . -name "devil_fruit_*.txt" -printf "%M %p\n"` – Checks permissions of each file.
- `cat eat.sh` – Reads the script to see validation logic.
- `./eat.sh ./sector_C/devil_fruit_6.txt` – Runs script with the target fruit file to get the flag.
