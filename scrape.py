import requests
from bs4 import BeautifulSoup
import json
import re

# Function to extract all href links from an HTML file
def extract_hrefs(file_path):
    """
    Extract all href links ending with .html from an HTML file.

    Args:
        file_path (str): Path to the HTML file.
    
    Returns:
        list: A list of href links.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
    
    soup = BeautifulSoup(html_content, "html.parser")
    # Extract all href links ending with ".html"
    hrefs = [a["href"] for a in soup.find_all("a", href=True) if a["href"].endswith(".html")]
    
    return hrefs


# Function to fetch and parse text from a given URL
def fetch_url_content(url):
    """
    Send a GET request to fetch the webpage content.

    Args:
        url (str): The URL to fetch content from.
    
    Returns:
        str: The raw HTML content from the page, or None if failed.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch URL {url}: {e}")
        return None


# Function to extract the clean text from the body of an HTML page
def extract_text_from_html(html_content):
    """
    Extract all visible text content from the HTML, excluding scripts and styles.

    Args:
        html_content (str): The raw HTML content to extract text from.

    Returns:
        str: The extracted clean text from the body of the HTML.
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove script and style elements
    for element in soup(["script", "style"]):
        element.decompose()

    # Extract the text from the body of the page
    text = soup.body.get_text(separator=" ", strip=True)

    # Clean the text by removing unwanted characters and extra spaces
    text = re.sub(r'\\u[0-9a-fA-F]{4}', '', text)  # Remove escape sequences
    text = text.replace("\u00d7", "")  # Remove multiplication sign (×)
    text = re.sub(r'\s+', ' ', text).strip()  # Normalize spaces
    
    return text


# Function to extract all text for each href and store it in a dictionary
def extract_text_for_hrefs(hrefs):
    """
    Extract text from each URL and store it in a dictionary.

    Args:
        hrefs (list): List of URLs to extract text from.

    Returns:
        dict: A dictionary where keys are hrefs and values are extracted text.
    """
    all_text = {}
    for href in hrefs:
        print(f"Processing: {href}")
        html_content = fetch_url_content(href)
        
        if html_content:
            text = extract_text_from_html(html_content)
            all_text[href] = text
        else:
            all_text[href] = "Failed to retrieve content"
    
    return all_text


# Function to save data to a JSON file
def save_to_json(data, file_path):
    """
    Save a Python dictionary to a JSON file.

    Args:
        data (dict): The dictionary to save as JSON.
        file_path (str): The path to the output JSON file.
    """
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)


def scrape():
    # Path to your HTML file
    file_path = "assignment.html"

    # Extract all href links from the HTML file
    hrefs = extract_hrefs(file_path)
    
    # Extract the text for each href link
    all_text = extract_text_for_hrefs(hrefs)

    # Save the extracted text to a JSON file
    output_file = "assignment_test.json"
    save_to_json(all_text, output_file)
    print(f"Data saved to {output_file}")

scrape()