# **Git Version Control**

## 🆚 Initialize Git in Project Repository

1. Ensure Git is installed and check the version:

   ```cmd
   git --version                                            :: Verify Git is installed
   ```

2. Initialize git and track changes:

   ```cmd
   git init                                                 :: Initialize git repo
   git add -A                                               :: Stage all changes
   git commit -m "initial commit"                           :: Commit initial files
   ```

3. [Optional] Create a `.gitignore` file to avoid committing unnecessary files

   ```cmd
   type NUL > .gitignore
   ```

   Common entries for ML projects:

   ```
   venv/
   __pycache__/
   *.pyc
   .DS_Store
   *.ipynb_checkpoints
   data/raw/
   ```

## 🔗 Create a GitHub Repository & Connect Local Repo

1. Ensure GitHub CLI (`gh`) is installed and check the version:

   ```cmd
   gh --version                                             :: Verify Git is installed
   ```

2. Authenticate GitHub CLI:

   ```cmd
   gh auth login                                            :: Log in to your GitHub account
   ```

3. Create a new GitHub repository:

   ```cmd
   gh repo create ML_Project --public --source=. --remote=origin --push
   ```

   - `ML_Project` → name of your GitHub repository
   - `--public` → make the repo public (use --private if you want it private)
   - `--source=.` → use the current directory as the repo source
   - `--remote=origin` → name the remote connection origin
   - `--push` → push the current commits to GitHub immediately

4. Verify remote connection:

   ```cmd
   git remote -v                                            :: Check remote URLs
   ```

## ➡️ Push Future Changes

1. Stage, commit, and push your changes to the remote repository:

   ```cmd
   git add .                                               :: Stage all changes
   git commit -m "Add new feature or update"               :: Commit staged changes
   git push origin main                                    :: Push to the main branch
   ```

## ⬅️ Pull & Work with Feature Branches

1. Regularly pull changes from the remote repository to keep your local repo up-to-date (important when collaborating):

   ```cmd
   git pull origin main                                    :: Update local repo with remote changes
   ```

2. Use feature branches for new work to avoid conflicts and keep main branch stable:

   ```cmd
   git checkout -b feature/new-idea                        :: Create and switch to a new branch
   ```

## 🔍 Useful Git Commands for Daily Workflows

- **Check Repository status** - commands to quickly understand the current state of your repo:

  ```cmd
  git status                                              :: See current branch, staged & unstaged changes
  git log                                                 :: View commit history
  git show <commit-hash>                                  :: Inspect a specific commit
  git diff                                                :: Show changes not yet staged
  ```

- **Branch Management** - commands to create, switch, and manage branches:

  ```cmd
  git branch                                              :: List all local branches
  git branch -r                                           :: List remote branches
  git checkout <branch-name>                              :: Switch to an existing branch
  git checkout -b <new-branch-name>                       :: Create & switch to a new branch
  git merge <branch-name>                                 :: Merge another branch into current branch
  ```

- **Undoing & Resetting Changes** - commands for reverting changes safely:

  ```cmd
  git checkout -- <file>                                  :: Revert unstaged changes in a file
  git reset <file>                                        :: Unstage a file
  git reset --hard <commit-hash>                          :: Reset branch to a specific commit (caution!)
  git revert <commit-hash>                                :: Create a new commit that undoes a previous commit
  ```

- **Stashing Changes** - commands to temporarily save work without committing:

  ```cmd
  git stash                                               :: Save current changes
  git stash list                                          :: View stashed changes
  git stash pop                                           :: Reapply stashed changes
  ```

- **Synchronizing with Remote** - commands to fetch, push, and pull updates from GitHub:

  ```cmd
  git fetch                                               :: Fetch updates from remote without merging
  git pull origin <branch-name>                           :: Pull updates and merge into current branch
  git push origin <branch-name>                           :: Push local commits to remote
  git remote -v                                           :: Check remote URLs
  git remote get-url origin                               :: Get remote URL only
  ```

- **Advanced / Inspection** - commands for deeper inspection and collaboration:

  ```cmd
  git log --oneline --graph --all                         :: Visualize branch history
  git show <branch-name>                                  :: Show details of a branch tip
  git tag                                                 :: List tags
  git diff <commit1> <commit2>                            :: Compare two commits
  ```
