DAIL_START_NUMBER = 50
INPUT_FILE_PATH = "AdventOfCode_day1_secret_entrance/input.txt"

def dail_password(rotation, dail_start_number):
    if rotation.startswith("L"):
        print(f"Left rotation: {rotation}, Dail Start Number: {dail_start_number}")
        rotation_steps = int(rotation[1:])

        password = dail_start_number
        for _ in range(1, rotation_steps+1):
            if password - 1 in range(0, 100):
                password = password - 1
            elif password - 1 < 0:
                password = 99
        return password
    elif rotation.startswith("R"):
        print(f"Right rotation: {rotation}, Dail Start Number: {dail_start_number}")
        rotation_steps = int(rotation[1:])

        password = dail_start_number
        for _ in range(1, rotation_steps+1):
            if password + 1 in range(0, 100):
                password = password + 1
            elif password + 1 > 99:
                password = 0
        return password
    else:
        return None

def read_input_list(file_path):
    try:
        with open(file_path, 'r') as file:
            data_list = file.readlines()
        
        return data_list

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    real_password = 0
    dail_start_number = DAIL_START_NUMBER
    numbers_range = read_input_list(INPUT_FILE_PATH)

    print(type(numbers_range))
    for rotation in numbers_range:
        current_password = dail_password(rotation, dail_start_number)
        dail_start_number = current_password
        print(current_password)
        if current_password == 0:
            real_password = real_password + 1
    print(f"Real password: {real_password}")


if __name__ == "__main__":
    main()