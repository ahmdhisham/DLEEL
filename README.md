# DLEEL
A RAG solution for appliances and gadgets serves as a replacement for traditional user manuals, enhancing the user experience.

- It provides more information about the specific gadget and its maintenance.
- It offers a step-by-step guide for users, reducing the burden of searching for solutions to specific gadget problems.
- It has the potential to reduce the workload on customer service.


### **Install Python**
***NOTE:*** Remove each **"$"** from the commands or copy the commands without it; it's only a declaration for using the terminal
1) Download python 3.10 from the official website of python

2) Install it and add it to the **System PATH**

3) Open the terminal from your project dirctory ***or*** head to your IDE terminal and change the working directory to your project directory 
(e.g. ```ahmed@ahmed-virtual-machine:~/Desktop/Projects/mini-RAG```)

4) Create a new virtual environment using the following command for Linux 
```bash
$ python3 -m venv .venv
```

5) Activate the environment using the following command for Linux
```bash 
$ source .venv/bin/activate
```
***OR*** create a new environment using Conda and activate it (Alternatives to step 4 and 5 if you deal with Anaconda):
```bash
$ conda create --name mini_rag python=3.10  # You can replace 3.10 with your preferred version above 3.10
```

```bash
$ conda activate mini_rag
# Activate the environment
```
**TIP for GUI lovers *(Alternative)*: You can also create the virtual environment with VS Code Built-in GUI if you want a one-click setup**

- Open the command palette: Ctrl + Shift + P

- Then search for:
Python: Create Environment

- Choose:

    - venv

    - Your preferred Python version from the list

    - Project location

    - Also check the requirements.txt file to install dependencies automatically.


### (Optional) Setup your command line interface for better readability - *only valid for Linux* -
```bash
$ export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

## Installation

### **Install the required packages** 
Install the required packages using this command in the same virtual environment 
```bash
$ pip install -r requirements.txt
```

### **Setup the environment variables**

```bash
$ cp src/.env.example src/.env
```
*Set your environment variables in the ".env" file. Like "OPENAI_API_KEY" value*

## Run fastapi server
```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 7000
```