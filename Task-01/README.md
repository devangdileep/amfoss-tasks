# Commands I Learned While Doing This Task

This document contains the commands I learned while completing each level of the task

---

## Master

- `touch README.md`  
  Creates a new file in the current directory

- `git add README.md`  
  Adds the specified file to the Git staging area

- `git commit -m "commit message"`  
  Commits the staged changes with a descriptive message

- `git push`  
  Pushes the committed changes from the local repository to the remote GitHub repository

## Commit one file

- `git add A.txt`  
  Adds the specified file to the Git staging area

- `git commit -m "commit message"`  
  Commits the staged changes with a descriptive message

- `git push`  
  Pushes the committed changes from the local repository to the remote GitHub repository

## Commit One File Staged

- `git status`  
  Displays the current status of the Git repository, including staged, unstaged, and untracked files

- `git restore --staged A.txt`  
  Removes `A.txt` from the Git staging area without discarding its changes

- `git commit -m "commit message"`  
  Commits the staged changes with a descriptive message

- `git push`  
  Pushes the committed changes from the local repository to the remote GitHub repository

## ignore-them

- `touch .gitignore`  
  Creates a `.gitignore` file to specify files and folders that Git should ignore

- `git commit -m "commit message"`  
  Commits the staged changes with a descriptive message

- `git push`  
  Pushes the committed changes from the local repository to the remote GitHub repository

## chase-branch

- `git merge <branch-name>`  
  Merges the specified branch into the current branch, combining the changes from both branches

## merge-conflict

- Open the conflicted file

- Locate the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)

- Edit the file and keep the desired changes

- Remove the conflict markers

- `git add <filename>`  
  Stages the resolved file

## save-your-work

- `git stash`  
  Temporarily saves all tracked uncommitted changes and restores the working directory to the last commit

- `git stash pop`  
  Restores the most recently stashed changes and removes them from the stash list

- `git status`  
  Displays the current status of the Git repository

- `git add <filename>`  
  Stages the specified file for the next commit

- `git commit -m "commit message"`  
  Commits the staged changes with a descriptive message

## change-branch-history

- `git checkout <branch-name>`  
  Switches to the specified branch

- `git rebase <branch-name>`  
  Reapplies the current branch commits on top of the specified branch, creating a cleaner and more linear commit history

- `git rebase --continue`  
  Continues the rebase process after resolving merge conflicts

- `git rebase --abort`  
  Cancels the rebase and restores the branch to its original state before the rebase

## remove-ignored

- `git rm --cached <filename>`  
  Removes the specified file from Git tracking without deleting it from the local working directory

- `git commit -m "commit message"`  
  Commits the staged changes with a descriptive message

## case-sensitive-filename

- `git mv <old-name> <new-name>`  
  Renames or moves a tracked file while preserving its history

- `git commit -m "commit message"`  
  Commits the staged changes with a descriptive message

## fix-typo

- `git commit --amend`  
  Modifies the most recent commit by changing its contents and/or commit message

- `git commit --amend --no-edit`  
  Updates the contents of the most recent commit while keeping the existing commit message

- `git add <filename>`  
  Stages the modified file to include it in the amended commit

## forge-date

- `git commit --amend --no-edit --date="1987-09-23"`  
  Rewrites the most recent commit while keeping the existing commit message and sets the author date to the specified date

## fix-old-typo

- `git rebase -i HEAD~2`  
  Starts an interactive rebase for the last two commits, allowing older commits to be edited, reordered, squashed, or removed

- `git commit --amend`  
  Modifies the selected commit during the interactive rebase

- `git add <filename>`  
  Stages the modified file so it can be included in the amended commit

- `git rebase --continue`  
  Continues the interactive rebase after amending a commit or resolving merge conflicts

## commit-lost

- `git reflog`  
  Displays a log of recent updates to `HEAD` and branch references, allowing lost commits to be recovered

- `git reset --hard <commit-hash>`  
  Restores the repository to the specified commit by updating the branch, staging area, and working directory

## split-commit

- `git reset HEAD^`  
  Moves `HEAD` to the previous commit while keeping its changes in the working directory

- `git add first.txt`  
  Stages `first.txt` for the next commit

- `git commit -m "commit message"`  
  Creates a new commit with the staged changes

- `git add second.txt`  
  Stages `second.txt` for the next commit

- `git commit -m "commit message"`  
  Creates another commit with the remaining staged changes, effectively splitting the original commit into two commits

## too-many-commits

- `git log -2`  
  Displays the last two commits in the current branch

- `git rebase -i HEAD~2`  
  Starts an interactive rebase for the last two commits

- `squash` (`s`)  
  Combines the selected commit with the previous commit into a single commit

## executable

- `git update-index --chmod=+x <filename>`  
  Sets the executable permission for the specified tracked file in Git's index so it is checked out as executable on Unix-like systems

- `git commit -m "commit message"`  
  Commits the staged permission change to the repository history

## commit-parts

- `git add -p file.txt`  
Starts interactive staging, allowing only selected parts of `file.txt` to be added to the staging area. I used `s` to split the changes into smaller hunks, then `y` to stage the Task 1 changes and `n` to skip the remaining changes.

- `git commit -m "Add Task 1 changes"`  
Creates a commit containing only the staged Task 1 changes.

- `git add file.txt`  
Stages the remaining changes in the file.

- `git commit -m "Add remaining changes"`  
Creates another commit containing the rest of the changes.

### Interactive options used

- `y` – Stage this hunk.
- `n` – Do not stage this hunk.
- `s` – Split the hunk into smaller hunks.

## pick-your-features

- `git cherry-pick feature-a`  
Copies the commit from the `feature-a` branch to the current branch.

- `git cherry-pick feature-b`  
Copies the commit from the `feature-b` branch to the current branch.

- `git cherry-pick feature-c`  
Copies the commit from the `feature-c` branch, but a merge conflict occurs.

- Resolve the merge conflict in `program.txt`.

- `git add program.txt`  
Stages the resolved file.

- `git commit -m "main"`  
Completes the cherry-pick after resolving the conflict.

### Why I used these commands

I used `git cherry-pick` to bring commits from the three feature branches into the `pick-your-features` branch. When `feature-c` caused a merge conflict, I fixed it manually, staged the file, and completed the cherry-pick.

## rebase-complex

- `git log rebase-complex`  
Used to view the commit history and identify the commit before the bug fix commits.

- `git rebase --onto your-master d5653fa5f724058fac4f2e3b0c791543d3305604 rebase-complex`  
Moves all commits after `d5653fa5f724058fac4f2e3b0c791543d3305604` from the `rebase-complex` branch onto the `your-master` branch.

### Why I used these commands

The goal was to move only the bug fix commits from the `rebase-complex` branch to the `your-master` branch using a single rebase command. I first checked the commit history to find the correct commit hash, then used `git rebase --onto` to rebase only the required commits.

## invalid-order

- `git rebase -i HEAD~2`  
Starts an interactive rebase for the last two commits.

- Swap the order of the two commits in the editor, then save and close it.

### Why I used this command

The goal of this exercise was to change the order of the last two commits. I used interactive rebase to reorder the commits without changing their contents.

## find-swearwords

- `git log -S "shit"`  
Searches the commit history to find commits that added or removed the word "shit".

- `git rebase -i`  
Starts an interactive rebase to edit the commits containing the unwanted word.

- Edit the files and remove the swear word.

- `git add <file>`  
Stages the modified file.

- `git commit --amend`  
Updates the current commit with the corrected changes.

- `git rebase --continue`  
Continues the rebase until all the required commits are fixed.

### Why I used these commands

I first searched the commit history to find the commits containing the swear word. Then I used interactive rebase to edit those commits, removed the unwanted word, amended each commit, and continued the rebase until all the commits were updated.