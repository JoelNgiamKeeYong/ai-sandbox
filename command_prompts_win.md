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
