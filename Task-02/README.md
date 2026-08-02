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

---

## Level 2 

### Objective
Unlock the communication vault and find the **Executive Transmission Code**.

### Steps
1. Switched to the `whiskey_peak_investigation` branch.
2. Listed all files including hidden ones in `Whiskey_Peak`.
3. Read `.baroque_works_cache/unlock_vault.sh` to see required inputs.
4. Exported `AWAKENING_SIGNATURE` with the Level 1 flag value.
5. Executed `unlock_vault.sh` to generate the log files.
6. Checked line 42 of `bounty_hunter_feed.log` to get the transmission code.

### Executive Transmission Code
`BAROQUE_DIAL{SPLIT_TIMELINE_MISDIRECTION}`

### Commands Used
- `git checkout whiskey_peak_investigation` – Switches to Level 2 branch.
- `ls -la` – Lists hidden files and cache folders.
- `cat .baroque_works_cache/unlock_vault.sh` – Checks vault script logic.
- `export AWAKENING_SIGNATURE="ONE_PIECE{GITO_GITO_NO_AWAKENING}"` – Sets environment variable.
- `./.baroque_works_cache/unlock_vault.sh` – Runs vault unlock script.
- `sed -n '42p' bounty_hunter_feed.log` – Fetches line 42 containing the code.

---

## Level 3 

### Objective
Find the genuine Baroque Works report and recover the first Poneglyph fragment.

### Steps
1. Switched to the `little_garden` branch.
2. Searched through reports in `Wax_Jungle` for Baroque mentions.
3. Located `agent_manifest.log` deep inside sector beta archive.
4. Read the file to retrieve the encoded `SECURITY_TAG` and Poneglyph fragment.
5. Decoded `SECURITY_TAG` with base64 to verify it matches Level 2 code.

### Poneglyph Fragment I
`KjY2MjF4bW0lKzYqNyBsIS0vbTAtJTcnL`

### Commands Used
- `git checkout little_garden` – Switches to Level 3 branch.
- `grep -r "BAROQUE" GrandLine/Wax_Jungle/` – Finds manifest file mentioning Baroque.
- `cat GrandLine/Wax_Jungle/sector_beta/outpost/watchtower/storage/archive/agent_manifest.log` – Reads hidden manifest file.
- `echo "QkFST1FVRV9ESUFMe1NQTElUX1RJTUVMSU5FX01JU0RJUkVDVElPTn0K" | base64 -d` – Decodes security tag.

---

## Level 4 

### Objective
Recover the second Poneglyph fragment hidden inside the Sea Train blueprints.

### Steps
1. Switched to the `canonical-timeline` branch.
2. Used `file` command on `puffing_tom_blueprints` and found it was a gzip archive.
3. Decompressed the archive to get `step1_blueprints.zip`.
4. Unzipped `step1_blueprints.zip` into `blueprints_extracted` directory.
5. Read `secret_link.txt` to get the second Poneglyph fragment.

### Poneglyph Fragment II
`SwnbzptDiM3JSpvFiMuJ28PJzAlJ28VIzA=`

### Commands Used
- `git checkout canonical-timeline` – Switches to canonical timeline branch.
- `file puffing_tom_blueprints` – Checks real file type of blueprints.
- `tar -xzf puffing_tom_blueprints` – Extracts gzip tar archive.
- `unzip step1_blueprints.zip` – Extracts inner zip archive.
- `cat blueprints_extracted/secret_link.txt` – Reads secret link to get fragment II.

---

## Level 5

### Objective
Recover deleted records from the last peaceful timeline commit and decode the final Poneglyph inscription.

### Steps
1. Switched to the `alternate_timeline` branch.
2. Checked git commit history to find the commit before files were deleted (`d4e7bf5`).
3. Restored `GrandLine/Enies_Lobby` directory from commit `d4e7bf5`.
4. Opened `.cp9_secure_vault/poneglyph.py` decoder script.
5. Combined Poneglyph Fragment I and Fragment II into one string.
6. Ran `poneglyph.py` and provided combined string to get the Level 6 repo link.

### Level 6 Repo Link
`https://github.com/rogueone-x/Laugh-Tale-Merge-War`

### Commands Used
- `git checkout alternate_timeline` – Switches to alternate timeline branch.
- `git log --oneline` – Checks commit history.
- `git checkout d4e7bf5 -- GrandLine/Enies_Lobby` – Restores erased files from pre-Buster Call commit.
- `cat GrandLine/Enies_Lobby/.cp9_secure_vault/poneglyph.py` – Views python decoder script.
- `python3 GrandLine/Enies_Lobby/.cp9_secure_vault/poneglyph.py` – Runs decoder with combined fragment.

---

## Level 6 

### Objective
Merge the two conflicting histories in the Laugh Tale repo and recover the Pirate King's Password.

### Steps
1. Cloned the Level 6 repository (`Laugh-Tale-Merge-War`).
2. Switched to `ancient_history` branch.
3. Merged `pirate_king_path` branch into `ancient_history`.
4. Resolved key file conflicts under `treasure/` directory.
5. Committed merge changes and executed `victory.sh` to reveal the final flag.

### Recovered Password
`TheGrandLineRemembers`

### Level 6 Flag
`FLAG{The_Grand_Line_Remembers_Your_Commit}`

### Commands Used
- `git clone https://github.com/rogueone-x/Laugh-Tale-Merge-War` – Clones Level 6 repository.
- `git checkout ancient_history` – Switched to ancient history branch.
- `git merge pirate_king_path` – Merges pirate king path branch.
- `git add treasure/key_part_1.txt treasure/key_part_2.txt` – Stages resolved key files.
- `git commit -m "Merge ancient history with pirate king path"` – Commits resolved merge.
- `./victory.sh` – Runs verification script to display final flag.
