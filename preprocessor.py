import re

def preprocess_text(text):
    """
    Preprocess the input text by:
    - Removing URLs
    - Removing special characters
    - Converting to lowercase
    """
    if not isinstance(text, str):  # Handle non-string values
        return ""  # Replace with an empty string or a default placeholder
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove special characters
    text = text.lower().strip()  # Convert to lowercase
    return text
