# EXERCISE 1
# "helper function"
def parsed_list_of_salary(read_file_lines: list[str]) -> list[float]:
    salaries_list: list[float] = []
    for line_num, line in enumerate(read_file_lines, start = 1):
        # ignore blank rows in the file
        if not line.strip():
            continue
        
        try:
            # print waring if line contains unexpected quantity of inputs in the row
            line_content = line.split(",")
            if len(line_content) != 2:
                print(f"Warning: Incorrect formation of the row number {line_num}")
                continue
            
            name, salary = line_content
            salary = float(salary.strip())

            # print warning, in case of negative salary
            if salary <= 0:
                print(f"Warning: Not considered salary of the row number {line_num}. Salary value: {salary}")
                continue
            
            salaries_list.append(salary)

        except (TypeError, ValueError) as e:
            print(f"Warning: Failed to parse row number {line_num}: {e}")
        
    return salaries_list


# read txt file. Content: each row "name,salary" -> return tuple(total salary, avg. salary)
def total_salary(path: str) -> tuple[float, float]:
    # read text file
    try: 
        with open(path, mode = "r", encoding = "utf-8") as file:
            read_file_lines: list[str] = file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"File {path} not found!")
    except PermissionError:
        raise PermissionError(f"No access permission to file {path}")

    # list of salary: contains list of each worker
    salary_list: list[float] = []

    # if file has no values -> return tuple(0, 0)
    if not read_file_lines:
        print(f"Warning: File {path} is blank")
        return (0.0, 0.0)
    else:
        salary_list = parsed_list_of_salary(read_file_lines)

    # if file contains only incorrect formats, negative salary, or blank rows
    if not salary_list:
        print(f"Warning: Missing or incorrect salary values in the file {path}")
        return (0.0, 0.0)

    # return a tuple (salaries total and mean)
    total_salary: float = sum(salary_list)
    return total_salary, total_salary / len(salary_list)



# EXERCISE 2
# The oldest varified cat, Creme Puff, leaved 38 years, I consider 50 y.o. as upper limit
CAT_AGE_UPPER_LIMIT: int = 50

# Helper function return
def get_validated_cat_profile_dict(cat_info: list[str]) -> dict[str, str|None]:
    # unpack id, name and age
    cat_id, cat_name, cat_age = cat_info
    cat_profile_dict: dict[str, str|None] = {"id": None, "name": None, "age": None}

    # cat_id shouldn't be empty:
    cat_id = cat_id.strip()
    if not len(cat_id) > 0:
        # return dictionary with empty values
        return cat_profile_dict
    cat_profile_dict["id"] = cat_id

    # cat_name should contains alphabetic characters [A-Z], space, or "-"
    cat_name = cat_name.strip()
    # If cat_name containst [non-alphabetic | " " | "-" | "."] characters return dict with None values
    if len([char for char in cat_name if not any([char.isalpha(), char in " -."])]) > 0:
        return cat_profile_dict
    
    # Capitilized the name of the cat [e.g.: "barsik" >> "Barsik" | "kotyk-myrchyk" >> "Kotyk-Myrchyk"]
    cat_profile_dict["name"] = cat_name.title()

    try:
        trimmed_cat_age: str = cat_age.strip()
        numeric_cat_age = int(trimmed_cat_age)
        # The oldest varified cat, Creme Puff, leaved 38 years, I consider 50
        if 0 < numeric_cat_age <= CAT_AGE_UPPER_LIMIT:
            cat_profile_dict["age"] = trimmed_cat_age
        else:
            print(f"Warning: the age \"{trimmed_cat_age}\" of the cat with id \"{cat_id}\" is not between 1 and {CAT_AGE_UPPER_LIMIT}")

    except ValueError as e:
        print(f"Age conversion error of the cat age \"{trimmed_cat_age}\", cat id \"{cat_id}\". Error: {e}")
    finally:
        return cat_profile_dict


# helper function:
def get_cat_profiles(file_content: list[str]) -> list[dict[str, str]]:
    cat_profiles_list: list[dict[str]] = []
    
    for line_num, line in enumerate(file_content, start = 1):
        try:
            cat_info = line.split(",")

            if len(cat_info) != 3:
                print(f"Warning: Incorrect formating of the row number {line_num}")
                continue
            
            # get dictionary with cat's: id, name, age. If value of a key is None then incorrect format
            cat_profile_dict = get_validated_cat_profile_dict(cat_info)
            
            if not all([cat_profile_dict["id"], cat_profile_dict["name"], cat_profile_dict["age"]]):
                print(f"Warning: Incorrect Cat Information Formation or the row {line_num}")
                continue
            
            cat_profiles_list.append(cat_profile_dict)

        except (ValueError, TypeError) as e:
            print(f"Warning: Incorrect formating of the row number {line_num}. Error: {e}")
    
    return cat_profiles_list


# read txt file. Content: each row "id,name,age" -> return list[dict{"id": id, "name": name, "age": age} of each cat]
def get_cats_info(path: str) -> list[dict[str, str]]:
    # read file:
    try:
        with open(path, mode = "r", encoding = "utf-8") as file:
            cats_info_list = file.readlines()
    except FileNotFoundError as f_e:
        raise FileNotFoundError(f"File \"{path}\" not found! Error: {f_e}")
    except PermissionError as p_e:
        raise PermissionError(f"No access permission to file \"{path}\". Error: {p_e}")
    
    if not cats_info_list:
        print(f"Warning: Missing content in the file \"{path}\"!")
        return []

    cats_info_list: list[dict[str, str, str]] = get_cat_profiles(cats_info_list)

    if not cats_info_list:
        print(f"Warning: No Cat Information recorded to the list from the file \"{path}\"!")

    return cats_info_list