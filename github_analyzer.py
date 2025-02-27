import requests
import sys
import json
import matplotlib.pyplot as plt
from prettytable import PrettyTable

def fetch_github_data(username):
    """Fetch GitHub user details"""
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("❌ User not found or API limit exceeded!")
        sys.exit()

    return response.json()

def fetch_repos(username):
    """Fetch user repositories"""
    url = f"https://api.github.com/users/{username}/repos?per_page=100"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else []

def display_basic_info(user_data):
    """Display GitHub user profile summary"""
    table = PrettyTable()
    table.field_names = ["Profile Info", "Details"]
    table.add_row(["Username", user_data["login"]])
    table.add_row(["Name", user_data.get("name", "N/A")])
    table.add_row(["Bio", user_data.get("bio", "N/A")])
    table.add_row(["Public Repos", user_data["public_repos"]])
    table.add_row(["Followers", user_data["followers"]])
    table.add_row(["Following", user_data["following"]])
    table.add_row(["GitHub URL", user_data["html_url"]])
    print(table)

def analyze_repos(repos):
    """Analyze top languages used"""
    language_count = {}
    for repo in repos:
        lang = repo.get("language")
        if lang:
            language_count[lang] = language_count.get(lang, 0) + 1

    if language_count:
        plt.figure(figsize=(6, 4))
        plt.bar(language_count.keys(), language_count.values(), color="skyblue")
        plt.xlabel("Languages")
        plt.ylabel("Number of Repos")
        plt.title("Most Used Programming Languages")
        plt.xticks(rotation=45)
        plt.show(block=False)  # ✅ Make it non-blocking

def save_data_as_json(username, user_data, repos):
    """Save GitHub data to a JSON file"""
    data = {
        "user_info": user_data,
        "repositories": repos
    }
    
    filename = f"{username}_github_data.json"
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)
    
    print(f"✅ GitHub data saved as '{filename}'")

if __name__ == "__main__":
    username = input("Enter GitHub username: ").strip()
    
    user_data = fetch_github_data(username)
    repos = fetch_repos(username)

    # Display data
    display_basic_info(user_data)
    
    # Analyze repositories and display graph (non-blocking)
    analyze_repos(repos)  

    # Ask if user wants to save data while the graph is open
    choice = input("\nDo you want to save this data as a JSON file? (yes/no): ").strip().lower()
    
    if choice == "yes":
        save_data_as_json(username, user_data, repos)
    else:
        print("❌ Data not saved. Exiting...")
    
    print("\nGitHub Data Extraction Completed Successfully! 🚀")
