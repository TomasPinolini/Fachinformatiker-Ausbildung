import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Scrape words from Wikipedia paragraphs
def scrape_wikipedia(url):
    try:
        print("Scraping the webpage...")
        # Make a request to the webpage
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        
        # Parse the webpage content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all paragraph tags <p>
        paragraphs = soup.find_all('p')
        
        # Extract words from all paragraphs
        words = []
        for p in paragraphs:
            words.extend(p.text.split())  # Split each paragraph into words
        
        print(f"Scraped {len(words)} words from the webpage.")
        return words
    except Exception as e:
        print(f"Error while scraping: {e}")
        return []

# Step 2: Save the words to a CSV file in the same folder as the script
def save_to_file(words, file_name):
    # Get the folder where the script is located
    current_folder = os.path.dirname(os.path.abspath(__file__))
    
    # Create the full path for the CSV file
    file_path = os.path.join(current_folder, file_name)
    
    # Save the words into a CSV file
    df = pd.DataFrame(words, columns=["Word"])  # Create a DataFrame with one column
    df.to_csv(file_path, index=False)  # Save the DataFrame to a CSV file
    print(f"Saved words to {file_path}")

# Step 3: Analyze the words and show most common ones
def analyze_words(file_name):
    try:
        print("Analyzing the words...")
        
        # Get the folder where the script is located
        current_folder = os.path.dirname(os.path.abspath(__file__))
        
        # Create the full path for the CSV file
        file_path = os.path.join(current_folder, file_name)
        
        # Load the CSV into a DataFrame
        df = pd.read_csv(file_path)
        
        # Count how often each word appears
        word_counts = df['Word'].str.lower().value_counts()
        
        print("\nMost common words:")
        print(word_counts.head(10))  # Print the 10 most common words
        
        # Show a bar chart of the most common words
        plot_word_frequencies(word_counts, top_n=10)
    except Exception as e:
        print(f"Error during analysis: {e}")

# Step 4: Plot the most common words
def plot_word_frequencies(word_counts, top_n=10):
    # Get the top N most frequent words
    top_words = word_counts.head(top_n)
    
    # Create a bar chart
    plt.figure(figsize=(10, 6))
    top_words.plot(kind='bar', color='lightblue')
    plt.title("Top Most Common Words", fontsize=16)
    plt.xlabel("Words", fontsize=14)
    plt.ylabel("Frequency", fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Main program
def main():
    print("Welcome to the Wikipedia Word Scraper!")
    url = input("Enter the Wikipedia URL (e.g., https://de.wikipedia.org/wiki/Bayern): ").strip()
    file_name = "scraped_words.csv"
    
    # Step 1: Scrape words from the Wikipedia page
    words = scrape_wikipedia(url)
    if not words:
        print("No words scraped. Exiting...")
        return
    
    # Step 2: Save the words to a CSV file
    save_to_file(words, file_name)
    
    # Step 3: Analyze the words and show the most common ones
    analyze_words(file_name)

# Run the program
if __name__ == "__main__":
    main()
