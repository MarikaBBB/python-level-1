import requests
import json 

def get_wikipedia_summary(topic):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        summary = data.get("extract", "No summary available.")
        return summary
    else:
        return "Failed to fetch information. Please try again later."

def save_summary_to_file(topic, summary):
    filename = f"{topic.replace(' ', '_')}.txt"
    with open(filename, "w") as file:
        file.write(summary)
    print(f"Summary saved to {filename}")

def main():
    print("Welcome to the Wikipedia Summary App!")
    topic = input("Enter the topic you want to learn about: ")
    summary = get_wikipedia_summary(topic)
    print("\nSummary:")
    print(summary)
    save_summary_to_file(topic, summary)

if __name__ == "__main__":
    main()
