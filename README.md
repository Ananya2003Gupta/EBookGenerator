# EBook Generator

Convert PDFs to interactive eBooks rendered using Material for MkDocs.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/Ananya2003Gupta/EBookGenerator
    ```
    
2. Navigate to the repository directory:
     ```bash
    cd EBookGenerator
    ```

3. Create a Python virtual environment:

    ```bash
    python -m venv env
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        env\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source env/bin/activate
        ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Run the main script to test the example:

    ```bash
    python main.py
    ```

7. Navigate to the ebookgenerator directory:
   ```bash
    cd ebookgenerator
    ```

8. Execute the below command to render ebook
   ```bash
    mkdocs serve
    ```

## PDF to Markdown Generation

The process of converting PDFs to Markdown files was implemented using the guidance provided in this [article](https://soulheartgrit.medium.com/see-how-easily-you-can-transform-pdfs-into-sleek-markdown-without-complex-tools-819aea4940a0).
