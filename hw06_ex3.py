import sys
from pathlib import Path
from colorama import Fore

# EXERCISE 3
INDENTATION: str = " " * 4

def print_folder_instance(indent_num: int, folder_name: str) -> None:
    print(f"{indent_num * INDENTATION}{Fore.BLUE}{folder_name}/{Fore.RESET}")


def print_file_instance(indent_num: int, file_name: str) -> None:
    print(f"{indent_num * INDENTATION}{Fore.GREEN}{file_name}{Fore.RESET}")


def print_messages(type_of_message: str, message: str) -> None:
    print(f"{Fore.RED}[{type_of_message}]:{Fore.RESET} {message}")


def validation_path(abs_path: Path) -> bool:
    # check if provided path exist
    if not abs_path.exists():
        print_messages("Error", f"\"{abs_path}\" does not exist!")
        return False
    
    # check if provided path is directory
    if not abs_path.is_dir():
        print_messages("Error", f"\"{abs_path}\" is not a path to directory")
        return False
    
    return True


def traversal_path(abs_path: Path, indentation_depth: int = 0) -> None:
    if abs_path.is_dir():
        print_folder_instance(indentation_depth, abs_path.name)
        try:
            for item in sorted(abs_path.iterdir()):
                traversal_path(item, indentation_depth + 1)
        except PermissionError:
            # Information in case of pesmission error
            print(f"{INDENTATION * (indentation_depth + 1)}{Fore.RED}[Permission Denied]{Fore.RESET}")
    else:
        print_file_instance(indentation_depth, abs_path.name)


def main() -> None:
    try:
        # apply resolve() method to accept both relative and absolute paths
        abs_path: Path = Path(sys.argv[1]).resolve()
    except IndexError:
        print_messages("Usage", "python hw03.py <path_to_directory>")
        sys.exit()

    if not validation_path(abs_path):
        sys.exit()
    
    traversal_path(abs_path)


if __name__ == "__main__":
    main()