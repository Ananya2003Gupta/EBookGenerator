# EBook Generator

Convert PDFs to interactive eBooks rendered using MkDocs.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/Ananya2003Gupta/EBookGenerator
    ```

2. Create a Python virtual environment:

    ```bash
    python -m venv env
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        env\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source env/bin/activate
        ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the main script to test the example:

    ```bash
    python main.py
    ```

6. Navigate to the generatedmarkdown directory:
   ```bash
    cd example/generatedmarkdown
    ```

7. Execute the below command to render ebook
   ```bash
    mkdocs serve
    ```

## PDF to Markdown Generation

The process of converting PDFs to Markdown files was implemented using the guidance provided in this [article](https://soulheartgrit.medium.com/see-how-easily-you-can-transform-pdfs-into-sleek-markdown-without-complex-tools-819aea4940a0).
