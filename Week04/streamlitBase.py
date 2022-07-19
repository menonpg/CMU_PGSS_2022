import sys
from streamlit import cli as stcli
import streamlit as st
    
def main():
    # Your streamlit code
    st.title("Test")
    st.title("My first app using Streamlit!")


if __name__ == '__main__':
    if st._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0], "--server.port=8501", "--server.address=0.0.0.0"]
        sys.exit(stcli.main())