import os
import re
import datetime
import random # For random selection

def update_readme():
    """
    Scans the current directory for problem solutions, extracts details,
    and generates a comprehensive README.md file.
    Features: Problem Links, Counts, Language, Random Spotlight,
    Difficulty Analysis (Tags), Search/Filter, Learning Path, Contribution.
    """
    
    # --- Configuration ---
    # Languages recognized by file extension
    language_map = {
        '.cpp': 'C++',
        '.py': 'Python',
        '.java': 'Java',
        '.c': 'C',
        '.go': 'Go',
        '.js': 'JavaScript', # For Node.js solutions
        # Add more extensions as needed
    }

    # --- Data Collection ---
    all_problems_data = {} # {rating: [(problem_name, url, language, filename, tags), ...]}
    problems_by_tag = {}   # {tag: [(problem_name, url, language, filename), ...]}
    total_problems_count = 0
    all_problem_items = [] # To store all problem data for random selection

    # Iterate through all items in the current directory
    for item in os.listdir('.'):
        # Check if it's a directory and its name is a digit (representing a rating)
        if os.path.isdir(item) and item.isdigit():
            rating = int(item)
            
            # Ensure the rating exists in our primary data structure
            if rating not in all_problems_data:
                all_problems_data[rating] = []

            # Iterate through files within the rating folder
            for file_name in os.listdir(item):
                file_path = os.path.join(item, file_name)
                
                # Check if it's a file and has a recognized extension
                ext = os.path.splitext(file_name)[1].lower()
                if os.path.isfile(file_path) and ext in language_map:
                    
                    problem_name = os.path.splitext(file_name)[0] # Default to filename without extension
                    problem_url = "#"      # Default to a local anchor if URL not found
                    language = language_map.get(ext, "Unknown")
                    tags_found = []
                    
                    # Try to extract Problem Name, URL, and Tags from file content
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            # Read first few lines for efficiency (up to 20 lines should be enough for headers)
                            lines = [f.readline() for _ in range(20)]
                            content = "".join(lines)

                            # Regex to find Problem Name
                            name_match = re.search(r'(?:Problem:|# Problem:)\s*(.+)', content, re.IGNORECASE)
                            if name_match:
                                problem_name = name_match.group(1).strip()
                            
                            # Regex to find URL
                            url_match = re.search(r'(?:URL:|# URL:)\s*(https?://[^\s]+)', content, re.IGNORECASE)
                            if url_match:
                                problem_url = url_match.group(1).strip()
                            
                            # Regex to find Tags
                            tag_match = re.search(r'(?:Tag:|# Tag:)\s*(.+)', content, re.IGNORECASE)
                            if tag_match:
                                raw_tags = tag_match.group(1).split(',')
                                tags_found = sorted([tag.strip() for tag in raw_tags if tag.strip()])

                    except Exception as e:
                        print(f"Warning: Could not read or parse '{file_path}': {e}")
                    
                    # Store problem data
                    problem_data = (problem_name, problem_url, language, file_name, tags_found, rating)
                    all_problems_data[rating].append(problem_data)
                    all_problem_items.append(problem_data) # Add to list for random selection
                    total_problems_count += 1

                    # Populate problems_by_tag
                    for tag in tags_found:
                        if tag not in problems_by_tag:
                            problems_by_tag[tag] = []
                        problems_by_tag[tag].append(problem_data)

    # Sort problems within each rating (alphabetically by problem name)
    for rating in all_problems_data:
        all_problems_data[rating] = sorted(all_problems_data[rating], key=lambda x: x[0].lower())

    # Sort problems within each tag (alphabetically by problem name)
    for tag in problems_by_tag:
        problems_by_tag[tag] = sorted(problems_by_tag[tag], key=lambda x: x[0].lower())

    # --- README Content Generation ---
    readme_content = []

    # 1. Main Header
    readme_content.append("# My Codeforces Journey 🚀\n")
    readme_content.append("Welcome to my competitive programming journey on Codeforces! This repository "
                          "showcases my solved problems, organized by rating and algorithmic concept.\n\n")

    # 2. Overall Statistics & Badges (Feature: Problems per Rating Category / Statistics)
    readme_content.append("## 📊 Journey Statistics\n")
    readme_content.append(f"![Total Problems Solved](https://img.shields.io/badge/Total_Problems-{total_problems_count}-blue)\n\n")

    if all_problems_data:
        readme_content.append("### Problem Distribution by Rating:\n")
        # Simple text-based bar chart or just counts
        for rating in sorted(all_problems_data.keys()):
            num_problems = len(all_problems_data[rating])
            readme_content.append(f"- **Rating {rating}:** {num_problems} problems\n")
        readme_content.append("\n")

    # 3. Problem of the Day/Week Spotlight (Feature: Random Spotlight)
    if all_problem_items:
        random_problem = random.choice(all_problem_items)
        rp_name, rp_url, rp_lang, _, _, rp_rating = random_problem
        readme_content.append("## ✨ Spotlight Problem\n")
        readme_content.append(f"Feeling lucky? Here's a random problem from my collection:\n")
        readme_content.append(f"* **[{rp_name}]({rp_url})** (Rating: {rp_rating}, Language: {rp_lang})\n\n")


    # 4. Search/Filter Instructions (Feature)
    readme_content.append("## 🔍 How to Explore\n")
    readme_content.append("You can easily navigate through the problems:\n")
    readme_content.append("- **By Rating:** Browse the sections below for problems grouped by Codeforces rating.\n")
    readme_content.append("- **By Concept/Tag:** Find problems categorized by the algorithms or data structures they use.\n")
    readme_content.append("- **GitHub Search:** Use GitHub's search bar (at the top of the repository page) to quickly find specific problem names or keywords within my solutions.\n\n")

    # 5. Problems by Rating (Feature: Rating Wise)
    readme_content.append("## 🏆 Problems by Rating\n")
    if not all_problems_data:
        readme_content.append("No problems found categorized by rating yet.\n\n")
    else:
        for rating in sorted(all_problems_data.keys()):
            problems = all_problems_data[rating]
            readme_content.append(f"### Rating: {rating} ({len(problems)} Problems)\n\n")
            for problem_name, problem_url, language, original_filename, _, _ in problems:
                readme_content.append(f"* [{problem_name}]({problem_url}) ({language})\n")
            readme_content.append("\n")

    # 6. Problems by Concept/Tag (Feature: Difficulty Analysis)
    readme_content.append("## 🧩 Problems by Concept/Tag\n")
    if not problems_by_tag:
        readme_content.append("No problems found with specific tags yet. Add `// Tag: YourTag1, YourTag2` to your solution files!\n\n")
    else:
        # Sort tags alphabetically
        for tag in sorted(problems_by_tag.keys()):
            problems = problems_by_tag[tag]
            readme_content.append(f"### {tag} ({len(problems)} problems)\n\n")
            for problem_name, problem_url, language, original_filename, _, _ in problems:
                readme_content.append(f"* [{problem_name}]({problem_url}) ({language})\n")
            readme_content.append("\n")

    # 7. A "Learning Path" Section (Feature)
    readme_content.append("## 🗺️ My Learning Path & Advice\n")
    readme_content.append("This section reflects my journey and how I approach learning competitive programming. "
                          "It might serve as a guide for others!\n\n")
    readme_content.append("### Suggested Learning Progression:\n")
    readme_content.append("- **Start with Basics (Rating 800-1000):** Focus on implementation, basic math, and simple data structures. Get comfortable with problem reading and input/output.\n")
    readme_content.append("- **Dive into Core Algorithms (Rating 1000-1400):** Explore Dynamic Programming (DP), Graph Traversal (BFS/DFS), Binary Search, Two Pointers, and Greedy algorithms. Practice problems specifically tagged with these concepts.\n")
    readme_content.append("- **Advanced Topics (Rating 1400+):** Branch out into more complex data structures (Segment Trees, Fenwick Trees), advanced graph algorithms (Dijkstra, Floyd-Warshall), number theory, combinatorics, and flow algorithms. Pay attention to time and space complexity.\n")
    readme_content.append("- **Consistency is Key:** Solve problems regularly, participate in contests, and always review solutions (even if you solve them) to learn new tricks.\n\n")


    # 8. Contribution Guidelines (Feature)
    readme_content.append("## 🤝 Contributions & Feedback\n")
    readme_content.append("While this is primarily a personal repository, I welcome feedback and suggestions!\n")
    readme_content.append("- **Spot an optimization or a bug?** Feel free to open an [issue](https://github.com/Angkon-Kar/Codeforces-Journey/issues) or a [pull request](https://github.com/Angkon-Kar/Codeforces-Journey/pulls).\n")
    readme_content.append("- **Have questions about a solution?** Don't hesitate to ask by opening an issue.\n")
    readme_content.append("- **Want to use my solutions?** You're welcome to learn from them! Please attribute if you share them publicly.\n\n")

    # Footer with Timestamp
    readme_content.append("---\n")
    readme_content.append(f"*README generated on {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC*\n")

    # Write the combined content to README.md
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write("".join(readme_content))

if __name__ == "__main__":
    update_readme()
