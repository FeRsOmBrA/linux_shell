import streamlit as st
import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.stderr.decode('utf-8')

def main():
    st.title("Linux Terminal Simulator")
    
    command = st.text_input("Enter a command", "ls -l")
    
    if st.button("Run"):
        output = run_command(command)
        st.text_area("Output", value=output, height=300)
    
if __name__ == "__main__":
    main()
