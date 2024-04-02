import os
import streamlit as st

def list_files(directory):
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def main():
    st.title("Folder Upload")

    # Allow selecting a folder
    folder_path = st.sidebar.text_input("Enter folder path:")

    if folder_path:
        # Validate folder path
        if not os.path.isdir(folder_path):
            st.error("Invalid folder path!")
            return

        st.write("### Files in Folder:")
        files = list_files(folder_path)
        for file in files:
            st.write(file)

            # Display content of the file
            with open(file, "r") as f:
                file_contents = f.read()
                st.write("### File Content")
                st.code(file_contents)

if __name__ == "__main__":
    main()
