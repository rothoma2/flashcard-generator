import json
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas

def create_flashcards(json_file, pdf_file):
    # Load data from JSON file
    with open(json_file, 'r') as f:
        flashcard_data = json.load(f)

    # Initialize PDF canvas
    c = canvas.Canvas(pdf_file, pagesize=landscape(letter))
    width, height = letter

    # Calculate dimensions for flashcards
    card_width = width / 2
    card_height = height / 2

    # Loop through flashcard data and create cards
    for i, card_text in enumerate(flashcard_data):
        # Calculate position for current card
        x_offset = (i % 2) * card_width
        y_offset = (i // 2) * card_height

        # Draw rectangle for flashcard
        c.rect(x_offset, y_offset, card_width, card_height)

        # Center text on the flashcard
        text_width = c.stringWidth(card_text, "Helvetica", 12)
        text_height = 12
        x_text = x_offset + (card_width - text_width) / 2
        y_text = y_offset + (card_height - text_height) / 2

        # Add text to flashcard
        c.drawString(x_text, y_text, card_text)

    # Save the PDF
    c.save()

# Example usage
create_flashcards('flashcards.json', 'flashcards.pdf')
