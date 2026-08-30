# Task 10: Surprise Us - Open Source Bug Fix

For Task 10, I worked on an open-source project named **CCExtractor / sample-platform**. I found a real performance bug, figured out why the server was crashing, fixed the code, and submitted my changes through a Pull Request on GitHub.

##  What was the problem?

* **Project:** CCExtractor / sample-platform
* **Issue:** [GET /samples/{id}/history times out (504) on production data #1161](https://github.com/CCExtractor/sample-platform/issues/1161)

When users asked the server for the history of a test sample (for example, asking for just 5 items), the server took more than 70 seconds and failed with a **504 Gateway Timeout** error.


## Why was it taking so long?

The code was doing extra work that was not needed:

1. **Loading Too Much Data:** Even if a user asked for 5 items, the server loaded **all 10,000+ past runs** from the database into Python memory.
2. **Extra Processing:** It loaded files and timestamps for all 10,000 runs.
3. **Late Slicing:** Only at the very end did Python cut out the 5 items that were actually asked for.

Because it processed 10,000 items every single time, the server got slow and timed out.

## How I fixed it and my approach

I fixed the problem in 4 simple steps:

### Step 1: Fetching only what is needed from the Database
Instead of loading all 10,000 items into Python memory, I updated the database query to use `.offset()` and `.limit()`. Now the database only returns the 5 items asked for. All extra work for loading files and timestamps now runs for 5 items instead of 10,000.

### Step 2: Keeping status filters working
If a user specifically asks to filter by status (like `?status=fail`), the status is calculated in Python. I made sure the code still handles this correctly so the results remain accurate.

### Step 3: Cleaning up the code for automated checks
When I tested the code, the automated tool (SonarCloud) warned that code was being repeated. To fix this, I moved the repeated code into a small helper function called `_build_history_entries()`. This made the code clean and passed all automated checks with a 100% green pass.

### Step 4: Keeping Git history clean
I updated my commit message and used `git commit --amend` and `git push --force`. This kept all my changes inside **1 single clean commit** instead of multiple messy commits, which is the standard way to contribute to open source.

## What I Learned from This Project
Through this open-source contribution, I gained practical hands-on experience:
1. **Database vs. Memory Performance:** I learned why database-level filtering (`LIMIT` / `OFFSET` in SQL) is much faster than loading large datasets into Python memory.
2. **Debugging Real Production Code:** I learned how to navigate a large open-source codebase, trace API endpoints, find performance bottlenecks, and fix real production bugs.
3. **Automated Code Quality Tools:** I learned how CI tools like SonarCloud check for code duplication and complexity, and how refactoring code into helper functions keeps code clean.
4. **Professional Git & Open Source Workflow:** I learned how to fork repositories, work with feature branches, amend commits to maintain a clean git history, and communicate effectively in GitHub Pull Requests.

## Results

* **Server Response:** Changed from `504 Timeout` to `200 OK`.
* **Speed:** Time dropped from **70+ seconds down to less than 50 milliseconds**.
* **Code Checks:** Passed all automated SonarCloud quality checks.

## Important Links

* **Main Project:** [CCExtractor/sample-platform](https://github.com/CCExtractor/sample-platform)
* **Issue Link:** [Issue #1161](https://github.com/CCExtractor/sample-platform/issues/1161)
* **My Code Branch:** [fix/paginate-sample-history-sql](https://github.com/devangdileep/sample-platform/tree/fix/paginate-sample-history-sql)
