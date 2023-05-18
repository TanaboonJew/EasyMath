import os
import sys
import word_doc_gen as docGen


def main():
    print("\033[92m\nThis application will generate as many simple math questions as you want.")
    print("There will be one hundred questions on one page.\033[93m")

    directory = "Generated_Problems"
    if os.path.exists(directory):
        print("\033[93m\nFolder 'Generated_Problems' already exists. The result will be inside the folder.\033[0m")
    
    while True:
        try:
            times = int(input("\033[96m\nPlease input the desired number of pages> \033[0m"))
            break
        except ValueError:
            print("\033[91m\nInput is Invalid, Please Input an Integer.\033[0m")
    pdf = input("\033[96m\nDo you want a pdf file? (Y/N)> \033[0m").lower()
    while True:
        if pdf == "y":
            break
        elif pdf == "n":
            break
        else:
            pdf = input("\033[91m\nInput is Invalid, Please Answer Yes(Y) or No(N).\033[0m").lower
    

    docGen.generate_word_document(times)

    input("\033[95m\nPress Enter to exit...\033[0m")


if __name__ == '__main__':
    main()
