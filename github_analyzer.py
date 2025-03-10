import requests
import sys
import json
import mysql.connector
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME  # Import from config.py

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

def store_data_in_mysql(username, user_data, repos):
    """Store GitHub data in MySQL"""
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()

        # Insert user data
        cursor.execute(
            """
            INSERT INTO users (username, name, bio, public_repos, followers, following, github_url)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE name=%s, bio=%s, public_repos=%s, followers=%s, following=%s, github_url=%s
            """,
            (user_data["login"], user_data.get("name", "N/A"), user_data.get("bio", "N/A"),
             user_data["public_repos"], user_data["followers"], user_data["following"], user_data["html_url"],
             user_data.get("name", "N/A"), user_data.get("bio", "N/A"),
             user_data["public_repos"], user_data["followers"], user_data["following"], user_data["html_url"])
        )

        # Insert repository data
        for repo in repos:
            cursor.execute(
                """
                INSERT INTO repositories (username, repo_name, language, repo_url) 
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE language=%s, repo_url=%s
                """,
                (username, repo["name"], repo.get("language", "N/A"), repo["html_url"], repo.get("language", "N/A"), repo["html_url"])
            )

        conn.commit()
        print(f"✅ GitHub data stored in MySQL successfully!")

    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")

    finally:
        cursor.close()
        conn.close()

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
    import matplotlib
    matplotlib.use('Agg')  # Set non-GUI backend before any plotting

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
        plt.savefig("language_analysis.png")  # Save instead of show
        print("📊 Language analysis graph saved as 'language_analysis.png'")

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

    # Analyze repositories and save graph
    analyze_repos(repos)  

    # Ask if user wants to store in MySQL
    choice = input("\nDo you want to store this data in MySQL? (yes/no): ").strip().lower()
    if choice == "yes":
        store_data_in_mysql(username, user_data, repos)
    else:
        print("❌ Data not stored in MySQL.")

    print("\nGitHub Data Extraction Completed Successfully! 🚀")
