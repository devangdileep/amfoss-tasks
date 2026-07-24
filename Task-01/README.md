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