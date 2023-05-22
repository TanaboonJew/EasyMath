# EasyMath

This repository contains a Python application that generates simple math questions and saves them as Word documents. The application allows you to specify the number of pages and whether you want the output in PDF format. Each page contains one hundred questions.

## Features

- Generates addition, subtraction, multiplication, and division questions.
- Randomly generates operands and operators for each question.
- Supports generating multiple pages of questions.
- Saves the generated questions as Word documents.
- Optionally converts the Word documents to PDF format.

## Requirements

- Python 3.10 or later
- Python packages: `python-docx`, `docx2pdf`, `tqdm`

## Usage

1. Clone the repository:

   ```bash
    git clone https://github.com/TanaboonJew/EasyMath

2. Install the required Python packages:

    ```bash
    pip install requirements.txt
    
3. Navigate to the repository directory:
    cd EasyMath

4. Run the application:
    python main.py

5. Follow the on-screen prompts to specify the number of pages, output format (PDF or Word), and the directory to save the generated files.

6. The application will generate the math questions and save them as Word documents in the specified directory. If you choose the PDF format, the Word documents will be converted to PDF.

## Directory Structure

- main.py: The main entry point of the application.
- file_name.py: Module for generating unique file names for the generated documents.
- questions_gen.py: Module for generating the math questions.
- word_doc_gen.py: Module for generating the Word documents.
- Generated_Problems/: Default directory for saving the generated files.

## Contributing
Contributions to this repository are welcome. If you encounter any issues or have suggestions for improvements, please feel free to submit a pull request.
