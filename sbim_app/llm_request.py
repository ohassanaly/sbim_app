from openai import OpenAI
import PyPDF2
import json
import os

client = OpenAI()

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.

    Parameters:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted text from the PDF.
    """
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
    return text

def load_json_grid(json_path):
    """Loads the JSON extraction grid."""
    with open(json_path, "r", encoding="utf-8") as file:
        return json.load(file)

def fill_json_with_ai(extraction_grid, pdf_text, model="gpt-4o-mini"):
    """
    Uses OpenAI API to fill an extraction grid with information extracted from a PDF.

    Parameters:
        extraction_grid (dict): The JSON grid specifying the structure of extracted data.
        pdf_text (str): The raw text extracted from the PDF.
        model (str): The OpenAI model to use (default: "gpt-4o-mini").

    Returns:
        dict: The extraction grid filled with AI-generated data.
    """
    
    prompt = f"""
    You are an AI assistant that extracts structured information from text.
    Given the following PDF content, fill in the JSON extraction grid with the relevant information.

    PDF Text:
    {pdf_text}

    Extraction Grid Schema:
    {extraction_grid}

    Provide a filled JSON object that adheres to the extraction grid schema.
    """

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an intelligent data extraction assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract the AI's response and parse it as JSON
    filled_grid = response.choices[0].message.content
    return filled_grid

if __name__ == "__main__":
    # Set file paths
    pdf_path = "../data/CT-20974_NOMANESIT_PIC_INS_AvisDef_CT20974.pdf"
    json_path = "../data/extract_grid.json"
    output_path = "../data/filled_grid.json"

    # Extract text from PDF
    extracted_text = extract_text_from_pdf(pdf_path)

    # Load the JSON extraction grid
    extraction_grid = load_json_grid(json_path)

    # Fill the JSON grid with AI
    filled_data = fill_json_with_ai(extraction_grid, extracted_text)

    # Save the filled JSON
    with open(output_path, "w", encoding="utf-8") as outfile:
        json.dump(filled_data, outfile, indent=2, ensure_ascii=False)

    print(f"Filled JSON saved to {output_path}")