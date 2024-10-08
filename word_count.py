import os
from collections import Counter
import pandas as pd
import re
from datetime import datetime
import argparse
from PyPDF2 import PdfReader
from docx import Document

# Extract text from a PDF file
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

# Extract text from a Word file
def extract_text_from_word(file_path):
    doc = Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

# Get word counts from text
def get_word_counts(text):
    # Split the text into words, excluding punctuation except for apostrophes and excluding numbers
    words = re.findall(r"\b[a-zA-Z]+(?:['-_][a-zA-Z]+)*\b", text)
    word_counts = Counter(words)

    # Convert the Counter object to a pandas DataFrame
    word_counts_df = pd.DataFrame(word_counts.items(), columns=['Word', 'Count'])

    # Sort the DataFrame by word counts in descending order
    word_counts_df = word_counts_df.sort_values(by='Word', ascending=True, key=lambda col: col.str.lower()).reset_index(
        drop=True)

    return word_counts_df

# Get phrase counts from text
def get_phrase_counts(text, phrases):
    # Skip if the list of phrases is empty
    if len(phrases) == 0:
        phrases_df = pd.DataFrame(columns=['Phrase', 'Count'])
        print('No phrase count: Empty list of phrases')
        return phrases_df

    # Convert the list of phrases to a DataFrame
    phrases_df = pd.DataFrame({'Phrase': phrases})

    # Count the occurrences of each phrase
    phrase_counts = [text.count(phrase) for phrase in phrases_df['Phrase']]
    phrases_df['Count'] = phrase_counts

    # Replace NaN values with 0
    phrases_df['Count'] = phrases_df['Count'].fillna(0).astype(int)

    phrases_df = phrases_df.sort_values(by='Phrase', ascending=True, key=lambda col: col.str.lower()).reset_index(
        drop=True)

    return phrases_df

# Save word and phrase counts to CSV files
def save_dataframes_to_csv(file_path, f_type, word_counts_df, phrases_df, want_words):
    # Generate timestamp for unique file names
    now = datetime.now()
    timestamp = now.strftime('%Y%m%d%H%M%S')

    # Generate file names based on the file path
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    dir_name = os.path.dirname(file_path)
    word_counts_file = os.path.join(dir_name, f'{base_name}_{f_type}_words_{timestamp}.csv')
    phrases_file = os.path.join(dir_name, f'{base_name}_{f_type}_phrases_{timestamp}.csv')

    # Save the DataFrames as CSV files
    if want_words:
        # Insert the file name as the first column
        word_counts_df.insert(0, 'Source file name', base_name)
        # Save the word counts to a CSV file
        word_counts_df.to_csv(word_counts_file, index=False)
        # Print the file path where the word counts are saved
        print(f'{file_path} word counts saved to: {word_counts_file}')

    if phrases_df.shape[0] != 0:
        # Insert the file name as the first column
        phrases_df.insert(0, 'Source file name', base_name)
        # Save the phrase counts to a CSV file
        phrases_df.to_csv(phrases_file, index=False)
        # Print the file path where the phrase counts are saved
        print(f'{file_path} phrase counts saved to: {phrases_file}')

# Process a file
def process_file(file_path, phrases_list=[], want_words=True):
    # Check the file type and extract text
    if file_path.endswith('.pdf'):
        f_type = 'pdf'
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        f_type = 'docx'
        text = extract_text_from_word(file_path)
    else:
        print(f'Unsupported file type: {file_path}')
        return

    # Get word and phrase counts
    word_counts_df = get_word_counts(text)
    phrases_df = get_phrase_counts(text, phrases_list)

    # Save the word and phrase counts to CSV files
    save_dataframes_to_csv(file_path, f_type, word_counts_df, phrases_df, want_words)

# Process a folder
def process_folder(folder_path, file_type, phrases_list=[], want_words=True):
    # Traverse the folder and process each file
    for root, _, files in os.walk(folder_path):

        # Process each file based on the file type
        for file in files:
            if file_type == '1' and file.endswith('.pdf'):
                process_file(os.path.join(root, file), phrases_list, want_words)
            elif file_type == '2' and file.endswith('.docx'):
                process_file(os.path.join(root, file), phrases_list, want_words)
            elif file_type == '3' and (file.endswith('.pdf') or file.endswith('.docx')):
                process_file(os.path.join(root, file), phrases_list, want_words)

# Main function
def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Process PDF and Word documents.')

    # Add arguments for phrases, want_words, and want_phrases
    parser.add_argument('--p', nargs='*', default=[], help='List of phrases to count')
    parser.add_argument('--w', action='store_true', help='Flag to save word counts')
    args = parser.parse_args()

    # Get the path of a file or folder
    path = input("Enter the path of a file or folder: ")

    # Process the file or folder based on the input
    if os.path.isfile(path):
        process_file(path, args.p, args.w)
    elif os.path.isdir(path):
        file_type = input("Specify file type to analyze (1 for pdf, 2 for word, 3 for both): ")
        process_folder(path, file_type, args.p, args.w)
    else:
        print("Invalid path")

# Run the main function
if __name__ == "__main__":
    main()