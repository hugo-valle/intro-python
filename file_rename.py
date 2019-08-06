"""
Rename files from a folder
Get: http://icarus.cs.weber.edu/~hvalle/hafb/prank.zip
"""
import os


def rename_files():
    """
    Rename files in a folder
    :return: nothing
    """
    folder_dir = r"C:\Users\CCETeach03.AD\Desktop\hafb\prankOrig"
    files = os.listdir(folder_dir)
    saved_path = os.getcwd()  # save current directory
    # Go the the files' directory
    os.chdir(folder_dir)
    for file in files:
        # Remove digits from name
        new_file = file.lstrip('0123456789')
        print("old name", file, "new name", new_file)
        # Rename file to new name
        os.rename(file, new_file)
    # Get back home
    os.chdir(saved_path)


def main():
    """
    test function
    :return: nothing
    """
    rename_files()


if __name__ == '__main__':
    main()
    exit(0)