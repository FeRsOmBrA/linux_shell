# Linux Terminal Simulator

This Streamlit application provides a web-based interface for executing Linux commands. It's a convenient tool for learning Linux commands, experimenting with different commands, or quickly accessing a terminal without needing a full-fledged Linux environment.

## Features

* **Interactive Command Execution:** Execute Linux commands directly in your web browser.
* **Real-Time Output:** View the output of your commands in real-time.
* **Command History:** Access a history of previously executed commands.
* **Error Handling:** Displays error messages if a command fails to execute.
* **User-Friendly Interface:** Simple and intuitive design for ease of use.
* **Extensive Sidebar Help:** Provides examples of common Linux commands for reference.

## How to Use

1. **Enter a Command:** Type a Linux command into the text input field.
2. **Run the Command:** Click the "Run" button to execute the command.
3. **View Output/Error:** The output or error message will be displayed below the command.
4. **Command History:** Scroll down to see a history of previously executed commands.

## Examples

The sidebar provides a comprehensive list of example commands, including:

* `ls -l` (List files in long format)
* `pwd` (Print working directory)
* `echo Hello, World!` (Print a message)
* `cat /etc/os-release` (Display operating system information)
* `cd /path/to/directory` (Change directory)
* `cp source destination` (Copy files)
* `mv source destination` (Move or rename files)
* `rm filename` (Remove files)
* `mkdir new_directory` (Create a new directory)
* and many more...

## Technical Details

* **Framework:** Streamlit
* **Language:** Python
* **Library:** `subprocess` (for command execution)

## Installation

1. Make sure you have Python and pip installed.
2. Install the required library:
   ```bash
   pip install streamlit
   ```

## Running the Application

1. Save the code as a Python file (e.g., `terminal_app.py`).
2. Run the application using Streamlit:
   ```bash
   streamlit run terminal_app.py
   ```



<hr>  
By:
<div align="center">
    <img src="https://i.ibb.co/DVCbGKp/1694197931620-e-1700697600-v-beta-t-V9i-TOhf-Pk-Vf-Bh4-QQxt-QPBVvs-Uyi-c-Emms-Qlh9d-C8p-UA.jpg" alt="hero" style="width: 200px; height: auto; border-radius: 50%;">
    <h3>Andres Castaño</h3>
    <p>Data Scientist | Geological Engineer</p>
    <a href="https://github.com/FeRsOmBrA" target="_blank">
        <img alt="GitHub" src="https://img.shields.io/badge/-GitHub-181717?style=for-the-badge&logo=github" />
    </a>
    <a href="https://www.linkedin.com/in/ferney-castano/" target="_blank">
        <img alt="LinkedIn" src="https://img.shields.io/badge/-LinkedIn-0077B5?style=for-the-badge&logo=linkedin" />
    </a>
</div>
