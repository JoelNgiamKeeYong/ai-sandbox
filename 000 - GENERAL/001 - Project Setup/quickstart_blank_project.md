# **Blank Project Quickstart (Windows)**

## 🚀 Open the Command Prompt

1.  Open Command Prompt quickly:

    ```
    Press Win
    Type "cp" and press Enter                            :: Opens the Windows Command Prompt
    ```

2.  Clear the screen by typing:

    ```cmd
    cls                                                  :: Clears the screen
    ```

## 📂 Create a Sample ML Project Folder

1. Navigate to Desktop inside OneDrive (common storage location):

   ```cmd
   cd OneDrive                                          :: Navigate to the OneDrive folder (Desktop is located here)
   cd Desktop                                           :: Change directory to the Desktop
   ```

2. Create common project folders and files:

   ```cmd
   mkdir ML_Project                                     :: Create main project folder
   cd ML_Project                                        :: Enter the project folder

   mkdir src                                            :: Create source folder
   mkdir data                                           :: Create data folder
   mkdir models                                         :: Create data folder

   type NUL > README.md                                 :: Create an empty README.md file
   type NUL > eda.ipynb                                 :: Create an empty Jupyter notebook for EDA
   type NUL > main.py                                   :: Create an empty main Python script
   type NUL > requirements.txt                          :: Create an empty requirements file
   ```

   This will create the folder structure as per below:

   ```
   ML_Project
   ├── data/
   ├── src/
   ├── models/
   ├── eda.ipynb
   ├── main.py
   ├── requirements.txt
   └── README.md
   ```

3. Review project structure in code editor / CLI:

   ```cmd
   code .                                               :: Open the project folder in VS Code

   tree                                                 :: See the folders only in the directory
   tree /f                                              :: Show directory tree with all files (requires 'tree' command)
   dir                                                  :: List files and folders in the current directory
   ```

4. (Alternatively) Create the project structure in **one (1)** command:

   ```cmd
   cd %UserProfile%\OneDrive\Desktop & mkdir sample_ml_project & cd sample_ml_project & mkdir src data models & type NUL > README.md & type NUL > eda.ipynb & type NUL > main.py & type NUL > requirements.txt & code .
   ```

## 🐍 (Optional) Setup Python Virtual Environment

1. Create a new Python virtual environment:

   ```cmd
   python -m venv venv                                  :: Create venv inside project
   py -3.11 -m venv venv                                :: Create a Python 3.11 venv inside project; ensure the specific Python version is installed
   ```

2. Activate the environment:

   ```cmd
   venv\Scripts\activate                                :: Activate (Windows)
   . venv\Scripts\activate                              :: Activate (Git Bash)
   python --version                                     :: Check Python version
   ```

3. Deactivate when done:

   ```cmd
   deactivate                                           :: Exit venv
   ```

4. [Optional] Remove current virutal environment folder:

   ```cmd
   Remove-Item -Recurse -Force .\venv                   :: Ensure that all instances are closed
   ```

## 📦 Manage Packages and Dependencies

1. Check what packages are currently installed in your environment:

   ```cmd
   pip list                                             :: List installed packages
   ```

2. Populate `requirements.txt` file with packages required for the blank project template:

   ```cmd
   # List of essential supervised ML libraries, grouped logically
   $packages = @(
      # Core data libraries
      "numpy", "pandas", "PyYAML", "setuptools",
      # ML frameworks
      "scikit-learn", "xgboost", "lightgbm", "catboost", "imbalanced-learn", "statsmodels",
      # Visualization
      "matplotlib", "seaborn", "missingno", "ydata_profiling",
      # Jupyter & notebook tools
      "iPython", "ipykernel", "ipywidgets", "jinja2",
      # Utilities
      "joblib", "requests"
   )

   # Clear previous requirements.txt if it exists
   Remove-Item requirements.txt -ErrorAction Ignore

   # Sort packages alphabetically
   $packages = $packages | Sort-Object

   # Loop through each package to get its installed version
   foreach ($pkgName in $packages) {
      $pkg = pip show $pkgName
      if ($pkg) {
         $versionLine = $pkg | Where-Object { $_ -like 'Version:*' }
         $version = $versionLine -replace 'Version:\s+', ''
         "$pkgName==$version" | Out-File -Append -Encoding UTF8 requirements.txt
      }
   }
   ```

3. Install packages from `requirements.txt`:

   ```cmd
   pip install -r requirements.txt                      :: Install all packages from requirements.txt
   pip list                                             :: Confirm that all packages are successfully installed
   ```

4. Manually install or remove packages:

   ```cmd
   pip install package_name                             :: Install a specific package
   pip uninstall package_name                           :: Uninstall a specific package
   ```

5. [Optional] Freeze Current Environment

   ```cmd
   pip freeze > requirements.txt
   ```

## 🆚 Initialize Git in Project Repository

1. Create a `.gitignore` file to avoid committing unnecessary files:

   ```cmd
   type NUL > .gitignore
   ```

   Common files for git to ignore are as follows:

   ```
   venv/
   __pycache__/
   *.pyc
   .DS_Store
   *.ipynb_checkpoints
   data/raw/
   ```

2. Initialize git and track changes:

   ```cmd
   git init                                             :: Initialize git repo with main branch as "master"
   git add -A                                           :: Stage all changes
   git commit -m "initial commit"                       :: Commit initial files
   ```

3. [Optional] Rename git branch:

   ```cmd
   git branch -m new-branch-name                        :: If currently on the branch you want to rename
   git branch -m old-branch-name new-branch-name        :: If not
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
