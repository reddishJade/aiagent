import sys
import os

# Add the functions directory to the path so we can import get_files_info
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "functions"))

from functions.get_files_info import get_files_info


def run_tests():
    result = get_files_info("calculator", ".")
    print(result)

    result = get_files_info("calculator", "pkg")
    print(result)

    result = get_files_info("calculator", "/bin")
    print(result)

    result = get_files_info("calculator", "../")
    print(result)


if __name__ == "__main__":
    run_tests()
