# 🖐️ Hand Tracking with MediaPipe and OpenCV

This project uses MediaPipe and OpenCV to detect and track hand landmarks in real-time using your webcam. It can serve as a base for building gesture-based interfaces, sign language recognition, or interactive applications.

---

## 🔧 Setup Instructions


### 1️⃣ Clone the Repository

To download this project to your local system, run:

```bash

git clone https://github.com/AAKASH22269796/Hand_Tracking.git

cd Hand_Tracking


### 🔧 Virtual Environment 

### 2️⃣ Create and Activate a Virtual Environment (Recommended)

#### On Windows:
```bash
python -m venv env
env\Scripts\activate



## 🔧 Packages

### 3️⃣ Install Required Packages

Install all necessary Python packages using:

```bash
pip install -r requirements.txt



#####
create env 
enter in it 
pip install mediapipe opencv-python 
pip install tensorflow==2.13.0
if an error comes : pip uninstall jax jaxlib -y
now do : pip install tensorflow==2.13.0
pip freeze > requirements.txt
git init.....



##########

IN .gitignore put:

# Ignore Python virtual environments
env/
.venv/
venv/
ENV/

# Ignore Python cache
__pycache__/
*.py[cod]
*.pyo

# Ignore IDE/project files
.vscode/
.idea/

# Ignore system files
.DS_Store
Thumbs.db
