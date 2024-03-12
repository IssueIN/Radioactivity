def subtract_and_save(input_file, output_file, value_to_subtract):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
        
        new_content = ""
        for line in lines:
            if line.strip(): 
                new_number = float(line.strip()) - value_to_subtract
                new_content += f"{new_number}\n"
        
        with open(output_file, 'w') as file:
            file.write(new_content)
        
        print("Operation completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

subtract_and_save('data/task16/55', 'data/ndsquare_data/55', -3.6363636)
