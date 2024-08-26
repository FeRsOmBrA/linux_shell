import streamlit as st
import subprocess
import time

# Función para ejecutar el comando
def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8'), ""
    except subprocess.CalledProcessError as e:
        return "", e.stderr.decode('utf-8')

# Función principal
def main():
    # Configuración de la página
    st.set_page_config(page_title="Linux Terminal Simulator", layout="wide")

    # Barra lateral
    st.sidebar.title("Linux Terminal Simulator")
    st.sidebar.markdown("### Una herramienta interactiva para ejecutar comandos de Linux")
    st.sidebar.markdown("#### Ejemplos de comandos:")
    st.sidebar.markdown("- `ls -l`\n- `pwd`\n- `echo Hello, World!`\n- `cat /etc/os-release`\n- `cd /path/to/directory`\n- `cp source destination`\n- `mv source destination`\n- `rm filename`\n- `mkdir new_directory`\n- `rmdir empty_directory`\n- `touch newfile.txt`\n- `nano filename`\n- `head -n 10 filename`\n- `tail -n 10 filename`\n- `grep 'search_pattern' filename`\n- `find /path -name filename`\n- `chmod 755 filename`\n- `chown user:group filename`\n- `df -h`\n- `du -sh /path/to/directory`\n- `ps aux`\n- `top`\n- `kill PID`\n- `man command`\n- `uname -a`\n- `whoami`\n- `date`\n- `uptime`\n- `free -h`\n- `ifconfig`\n- `ping -c 4 hostname`\n- `netstat -tuln`\n- `scp source user@remote:/path`\n- `ssh user@hostname`")

    # Título principal
    st.title("Linux Terminal Simulator")

    # Historial de comandos
    if "history" not in st.session_state:
        st.session_state.history = []

    # Campo de entrada de comandos
    command = st.text_input("Enter a command", "ls -l", key="input")

    # Botón para ejecutar el comando
    if st.button("Run"):
        output, error = run_command(command)
        st.session_state.history.append({"command": command, "output": output, "error": error})
        st.rerun()

    # Mostrar el historial de comandos
    st.subheader("Command History")
    for entry in st.session_state.history[::-1]:
        st.markdown(f"**Command:** `{entry['command']}`")
        if entry["output"]:
            st.text_area("Output", value=entry["output"], height=200)
        if entry["error"]:
            st.text_area("Error", value=entry["error"], height=200, key=str(time.time()))

    # Estilo CSS personalizado
    st.markdown("""
    <style>
    .stTextArea textarea {
        font-family: monospace;
        font-size: 14px;
        color: #ffffff;
        background-color: #1e1e1e;
    }
    .stTextInput input {
        font-family: monospace;
        font-size: 14px;
    }
    </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
