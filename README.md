
# 📊 GitHub Profile Analyzer

A Python CLI tool to analyze GitHub user profiles, display key metrics, and visualize programming language usage.

## 🚀 Features
✅ Fetch **GitHub user stats** (followers, public repos, etc.)  
✅ Analyze **most used programming languages**  
✅ Display user profile in a **formatted table** using `PrettyTable`  
✅ **Generate visualizations** with `matplotlib`  
✅ **Save data as JSON** for later use  
✅ Support **100+ repositories** per user  

## 📌 Installation
Ensure you have Python installed, then install the required dependencies:

```bash
pip install requests matplotlib prettytable
```

## 🔧 Usage
Run the script and enter a GitHub username when prompted:

```bash
python github_analyzer.py
```

## 📊 Example Output
```
+--------------+--------------------------+
| Profile Info | Details                  |
+--------------+--------------------------+
| Username     | octocat                   |
| Name         | The Octocat               |
| Bio          | GitHub mascot             |
| Public Repos | 8                         |
| Followers    | 5000                      |
| Following    | 10                        |
| GitHub URL   | https://github.com/octocat |
+--------------+--------------------------+
```
A **bar chart** will also be displayed showing the user's **most used programming languages**.

## 💾 Saving Data
After displaying the profile, the script will ask:  

```bash
Do you want to save this data as a JSON file? (yes/no):
```
- Enter **yes** to save the data as `{username}_github_data.json`
- Enter **no** to skip saving  

## 🔍 Limitations
⚠ API rate limits apply (60 requests per hour for unauthenticated users).  
⚠ Large accounts with many repositories may take longer to analyze.  

## 🛠 Future Improvements
🔹 Add GitHub repository statistics (stars, forks, etc.)  
🔹 Support for advanced analytics like contributions and commits  
🔹 Export data in **CSV format**  
🔹 Implement a **web-based version** using Flask/Django  
🔹 Cache results to **reduce API calls**  

---

## 🤝 Contributions & Feedback
Feel free to contribute, open an issue, or suggest improvements! 🚀  


