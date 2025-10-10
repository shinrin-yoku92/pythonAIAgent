from functions.get_files_info import get_files_info
import os

if __name__ == "__main__":
    print("Result for current directory:")
    res = get_files_info("calculator", ".")
    print(" " + res.replace("\n", "\n "))  # Current directory

    print("Result for 'pkg' directory:")
    res = get_files_info("calculator", "pkg")
    print(" " + res.replace("\n", "\n "))  # Subdirectory (should work)

    print("Result for '/bin' directory:")
    res = get_files_info("calculator", "/bin")
    print(" " + res.replace("\n", "\n "))  # Absolute path (should give error)

    print("Result for '../' directory:")
    res = get_files_info("calculator", "../")
    print(" " + res.replace("\n", "\n "))  # Outside working directory (should give error)