# **Quickstart - EZ Flow Supervised ML Pipeline**

## 🚀 Create new project folder from template:

### A. If template is on desktop:

1.  Duplicate the project folder with `CTRL + C → CTRL + V`

2.  Rename the project folder - choose a clear, descriptive name for your new project.

3.  Remove the existing Git history / `.git` folder to avoid linking tothe original repository.

4.  Open the project in VS Code:

    - Right Click → Open in Terminal

    - Type the below command:

      ```
      code .                                          :: Opens the current project folder in VS Code
      ```

### B. If template is NOT on desktop / download from GitHub:

1.  Open Command Prompt quickly:

    ```
    Press Win
    Type "cp" and press Enter                            :: Opens the Windows Command Prompt
    ```

2.  Navigate to Desktop inside OneDrive (common storage location):

    ```cmd
    cd OneDrive                                          :: Navigate to the OneDrive folder (Desktop is located here)
    cd Desktop                                           :: Change directory to the Desktop
    ```

3.  Clone and reset git history:

    ```cmd
    git clone https://github.com/username/template-repo.git new-repo            :: Clone the template repo
    cd new-repo                                                                 :: Enter the folder
    rmdir /s .git                                                               :: Remove old git history
    ```

4.  Open the project in VS Code:

    ```
    code .                                               :: Opens the current project folder in VS Code
    ```

## 🆚 Initialize Git in Project Repository

1. Initialize git and track changes:

   ```cmd
   git init                                             :: Initialize git repo
   git add .                                            :: Stage files
   git commit -m "initial commit"                       :: Commit initial files
   ```

## 🔗 Create a GitHub Repository and Connect Local Repo

1. Create a new GitHub repository:

   ```cmd
   gh repo create ML_Project --public --source=. --remote=origin --push
   ```

   - `ML_Project` → name of your GitHub repository
   - `--public` → make the repo public (use --private if you want it private)
   - `--source=.` → use the current directory as the repo source
   - `--remote=origin` → name the remote connection origin
   - `--push` → push the current commits to GitHub immediately

2. Verify remote connection:

   ```cmd
   git remote -v                                        :: Check remote URLs
   ```
