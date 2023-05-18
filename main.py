import os
import sys
import word_doc_gen as docGen
import file_name as fileName
from docx2pdf import convert


def main():
    print("\033[92m\nThis application will generate as many simple math questions as you want.")
    print("There will be one hundred questions on one page.\033[93m")

    directory = "Generated_Problems"
    change_dir = input("""\033[96m\nDo you want to change the directory to save files to?
    (originally save at 'Generated_Problems') (Y/N)> \033[0m""").lower()
    
    while True:
        if change_dir == "y":
            directory = input("\033[96m\nPlease input your desired directory name.> \033[0m")
            break
        elif change_dir == "n":
            break
        else:
            pdf = input("\033[91m\nInput is Invalid, Please Answer Yes(Y) or No(N).\033[0m").lower
    print(f"\033[92m\nYour result will be save at '{directory}'.\033[0m")
            
    if not os.path.exists(directory):
        print(f"\033[93m\nFolder '{directory}' is Not exists. Creating new folder name '{directory}'.\033[0m")
        try:
            os.makedirs(directory)
        except Exception as e:
            print("\033[91m\nA critical error occurred. Please contact the programmer.")
            print("Error:", str(e), "\033[0m")
            sys.exit(1)
        if os.path.exists(directory):
             print("\033[92m\nDone\033[0m")
    
    while True:
        try:
            times = int(input("\033[96m\nPlease input the desired number of pages> \033[0m"))
            break
        except ValueError:
            print("\033[91m\nInput is Invalid, Please Input an Integer.\033[0m")
    pdf = input("\033[96m\nDo you want a pdf file? (Y/N)> \033[0m").lower()
    while True:
        if pdf == "y":
            docGen.generate_word_document(times)
            name = fileName.get_name(times, directory)
            print("\033[93m\nConveting please wait...\033[0m")
            convert(f"{directory}/{name}", f"{directory}/{name[:-4]}pdf")
            print(f"\033[92m\nDocument '{name[:-4]}pdf' saved successfully at '{directory}/{name[:-4]}pdf'.\033[0m")
            break
        elif pdf == "n":
            docGen.generate_word_document(times)
            break
        else:
            pdf = input("\033[91m\nInput is Invalid, Please Answer Yes(Y) or No(N).\033[0m").lower
    

    input("\033[95m\nPress Enter to exit...\033[0m")


if __name__ == '__main__':
    main()
