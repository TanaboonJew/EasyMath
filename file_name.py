import os


def generate_file_name(times, directory):
    base_filename = f"{times*100}_questions"
    filename = f"{directory}/{base_filename}_1.docx"

    count = 1
    while os.path.exists(filename):
        count += 1
        filename = f"{directory}/{base_filename}_{count}.docx"
    filename = f"{base_filename}_{count}.docx"
    
    if count == 2:
        print(f"\033[93m\nFilename '{base_filename}_1.docx' already exists. Changing the filename to '{filename}'.\033[0m")
    elif count == 3:
        print(f"""\033[93m\nFilename '{base_filename}_1.docx' and '{base_filename}_2.docx' already exist.
    Changing the filename to '{base_filename}_3.docx'.\033[0m""")
    elif count > 3:
        print(f"""\033[93m\nFilename '{base_filename}_1.docx' to '{base_filename}_{count-1}.docx' already exist.
    Changing the filename to '{filename}'.\033[0m""")
    
    filename = f"{directory}/{base_filename}_{count}.docx"

    return filename