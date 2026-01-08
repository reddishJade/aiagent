import sys
import os

# Add the functions directory to the path so we can import get_files_info
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "functions"))

from functions.get_file_content import get_file_content


def run_tests():
    # Test lorem.txt
    result = get_file_content("calculator", "lorem.txt")

    print(f"Content length: {len(result)}")
    if "[...File" in result and "truncated" in result:
        print("File was truncated")
    else:
        print("File was not truncated")

    # Additional tests
    print("\nTesting calculator/main.py:")
    print(get_file_content("calculator", "main.py"))

    print("\nTesting calculator/pkg/calculator.py:")
    print(get_file_content("calculator", "pkg/calculator.py"))

    print("\nTesting calculator//bin/cat (should error):")
    print(get_file_content("calculator", "/bin/cat"))

    print("\nTesting calculator/pkg/does_not_exist.py (should error):")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))


if __name__ == "__main__":
    run_tests()
