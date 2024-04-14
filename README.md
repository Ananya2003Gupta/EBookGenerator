# EBook Generator

Convert PDFs to interactive eBooks rendered using MkDocs.

**Work in Progress**

- **Completed:** Basic PDF to Markdown conversion.
- **To Do:** Automate the rendering of generated Markdown files using MkDocs.

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

## PDF to Markdown Generation

The process of converting PDFs to Markdown files was implemented using the guidance provided in this [article](https://soulheartgrit.medium.com/see-how-easily-you-can-transform-pdfs-into-sleek-markdown-without-complex-tools-819aea4940a0).

## Rendering of Generated Markdown Files using MkDocs

The approach for rendering the generated Markdown files using MkDocs will be based on the [MkDocs recipe guide](https://mkdocstrings.github.io/recipes/).
