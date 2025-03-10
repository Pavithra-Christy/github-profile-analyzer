# 📊 GitHub Profile Analyzer

<<<<<<< HEAD
A **Python CLI tool** that fetches and analyzes GitHub user profiles, displaying key metrics and visualizing programming language usage. Now with **MySQL integration** for storing user data and JSON export for saving profiles locally!

## 🚀 Features
✅ Fetch **GitHub user statistics** (followers, public repos, etc.)  
✅ Analyze **most used programming languages**  
✅ Display user profile in a **formatted table** using `PrettyTable`  
✅ **Generate visualizations** with `matplotlib`  
✅ **Save data as JSON & MySQL** for later use  
✅ Support **100+ repositories** per user  
✅ **MySQL database integration** for storing user profiles and repo data  
✅ **JSON export** to save user details locally  

---
=======
# 📊 GitHub Profile Analyzer

A Python CLI tool to analyze GitHub user profiles, display key metrics, and visualize programming language usage.

## 🚀 Features
✅ Fetch **GitHub user stats** (followers, public repos, etc.)  
✅ Analyze **most used programming languages**  
✅ Display user profile in a **formatted table** using `PrettyTable`  
✅ **Generate visualizations** with `matplotlib`  
✅ **Save data as JSON** for later use  
✅ Support **100+ repositories** per user  
>>>>>>> d6ee26680834d84e0757a2efb8d30806729f11a2

## 📌 Installation
Ensure you have Python installed, then install the required dependencies:

```bash
<<<<<<< HEAD
pip install -r requirements.txt
```

### 📂 Database Setup (MySQL)
Before running the script, **set up your MySQL database**:
1. Install MySQL and ensure it’s running.
2. Create a database:
   ```sql
   CREATE DATABASE github_analysis;
   ```
3. Update your MySQL credentials in `github_analyzer.py`:
   ```python
   conn = mysql.connector.connect(
       host="localhost",
       user="your_username",
       password="your_password",
       database="github_analysis"
   )
   ```
4. Run the script to initialize tables automatically.

---

=======
pip install requests matplotlib prettytable
```

>>>>>>> d6ee26680834d84e0757a2efb8d30806729f11a2
## 🔧 Usage
Run the script and enter a GitHub username when prompted:

```bash
python github_analyzer.py
```

### 📊 Example Output
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
<<<<<<< HEAD
A **bar chart** will also be saved showing the user's **most used programming languages**.

---

## 💾 Saving Data
### ✅ JSON File
After displaying the profile, the script will save data as `{username}_github_data.json`.

### 📂 MySQL Database
The script stores user profile and repository data in **MySQL** if enabled.

---

## 👁️ Limitations
⚠ API rate limits apply (60 requests per hour for unauthenticated users).  
⚠ Large accounts with many repositories may take longer to analyze.  
⚠ Requires **MySQL setup** for database functionality.

---
=======
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
>>>>>>> d6ee26680834d84e0757a2efb8d30806729f11a2

## 🛠 Future Improvements
🔹 Add GitHub repository statistics (stars, forks, etc.)  
🔹 Support for advanced analytics like contributions and commits  
🔹 Export data in **CSV format**  
🔹 Implement a **web-based version** using Flask/Django  
🔹 Cache results to **reduce API calls**  

---

## 🤝 Contributions & Feedback
<<<<<<< HEAD
Feel free to **contribute, open an issue, or suggest improvements!** 🚀
=======
Feel free to contribute, open an issue, or suggest improvements! 🚀  

>>>>>>> d6ee26680834d84e0757a2efb8d30806729f11a2

