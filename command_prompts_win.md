# **Command Prompts (Windows)**

## 🚀 Opening the Command Prompt

```
Press Win
Type "cp" and press Enter         :: Opens the Windows Command Prompt
```

- Clear the screen by typing:

```cmd
cls                               :: Clears the screen
```

## 🧑‍💻 General Scripts

```
Press Win
Type "cp" and press Enter         :: Opens the Windows Command Prompt
```

- Clear the screen by typing:

```cmd
cls                               :: Clears the screen
```

## ⚡Create a Sample ML Project Folder

- Scaffold a new ML project with organized folder structure.
- Desktop inside OneDrive for easy access and backup.

```cmd
cd OneDrive                       :: Navigate to the OneDrive folder (Desktop is located here)
cd Desktop                        :: Change directory to the Desktop

mkdir ML_Project                  :: Create main project folder
cd ML_Project                     :: Enter the project folder

mkdir src                         :: Create source folder
mkdir data                        :: Create data folder

type NUL > README.md              :: Create an empty README.md file
type NUL > eda.ipynb              :: Create an empty Jupyter notebook for EDA
type NUL > main.py                :: Create an empty main Python script
type NUL > requirements.txt       :: Create an empty requirements file
```

- Alternatively, you can also create files using:

```cmd
echo.> README.md                  :: Create an empty requirements file
```

- This will create a folder structure like this:

```
ML_Project
└── data/
└── src/
├── eda.ipynb
├── main.py
├── requirements.txt
└── README.md
```

## 🆚 Git Initialization

- Track changes and prepare for version control and GitHub.

```cmd
git init                          :: Initialize git repo
git add .                         :: Stage files
git commit -m "initial commit"    :: Commit initial files
```

- Optionally, create a .gitignore file to avoid committing unnecessary files

```cmd
type NUL > .gitignore
```

- Common entries for ML projects:

```
venv/
__pycache__/
*.pyc
.DS_Store
*.ipynb_checkpoints
data/raw/
```

## 🔗 Create a GitHub Repository & Connect Local Repo

1. Ensure that the `GitHub CLI` / `gh` installed and are logged in via `gh auth login` before running the commands.

2. Create a new GitHub repo from the command line using `gh`:

   ```cmd
   gh repo create ML_Project --public --source=. --remote=origin --push
   ```

   Explanation of flags:

   - `ML_Project` → name of your GitHub repository
   - `--public` → make the repo public (use --private if you want it private)
   - `--source=.` → use the current directory as the repo source
   - `--remote=origin` → name the remote connection origin
   - `--push` → push the current commits to GitHub immediately

3. Verify remote connection:

   ```cmd
   git remote -v                                           :: Check remote URLs
   ```

4. Push future changes:

   ```cmd
   git add .
   git commit -m "Add new feature or update"
   git push origin main                                    :: Push to the main branch
   ```

## 🐍 Creating Virtual Environments

- Isolate dependencies for reproducible environments.

```cmd
python -m venv venv           :: Create a virtual environment named 'venv'
venv\Scripts\activate         :: Activate the virtual environment
```

- Update requirements.txt after installing packages:

```cmd
pip freeze > requirements.txt
```
