import os
import re
import datetime
import random
from collections import defaultdict

# --- User Configuration ---
GITHUB_USERNAME = "Angkon-Kar"
GITHUB_REPO_NAME = "Competitive-Programming-Journey"

def update_unified_readme():
    """
    Scans the entire repository for problem solutions, organizing them
    by platform (Codeforces, LeetCode, etc.), rating/difficulty, and tags.
    Generates a comprehensive, auto-updating README.md.
    Includes: Problem Name, URL, Language, GitHub Source Link,
    Platform, Category (Rating/Difficulty), Tags, Language Usage Stats, Solving Trend.
    """

    # --- Configuration ---
    language_map = {
        '.cpp': 'C++', '.py': 'Python', '.java': 'Java', '.c': 'C',
        '.go': 'Go', '.js': 'JavaScript', # Add more as needed
    }

    # --- Data Collection ---
    all_problems_by_platform = {} # {platform: {category: [(problem_name, url, language, tags, original_filename, last_modified_date), ...]}}
    problems_by_tag = {}          # {tag: [(problem_name, url, language, platform_display, category_display, last_modified_date), ...]}
    total_problems_count = 0
    all_problem_items = []        # For random selection

    language_counts = defaultdict(int) # For Language Usage Feature
    solving_trend_by_month = defaultdict(int) # For Solving Trend Feature (YYYY-MM format)

    # Main loop to iterate through top-level platform folders (e.g., 'Codeforces', 'LeetCode')
    for platform_folder in os.listdir('.'):
        platform_path = os.path.join('.', platform_folder)

        # Exclude hidden folders, script file, and README itself
        if os.path.isdir(platform_path) and \
           not platform_folder.startswith('.') and \
           platform_folder not in ['update_readme.py', 'README.md', '__pycache__']:
            
            # Initialize platform entry
            if platform_folder not in all_problems_by_platform:
                all_problems_by_platform[platform_folder] = {}

            # Determine how to iterate based on platform type
            if platform_folder == 'Codeforces':
                # Codeforces uses numeric rating folders (e.g., 800, 900)
                category_folders = [f for f in os.listdir(platform_path) if os.path.isdir(os.path.join(platform_path, f)) and f.isdigit()]
                category_type = "Rating"
            else:
                # Other platforms use difficulty folders (e.g., Easy, Medium)
                category_folders = [f for f in os.listdir(platform_path) if os.path.isdir(os.path.join(platform_path, f))]
                category_type = "Difficulty"
            
            for category_folder_name in category_folders:
                category_path = os.path.join(platform_path, category_folder_name)

                # Initialize category entry for this platform
                if category_folder_name not in all_problems_by_platform[platform_folder]:
                    all_problems_by_platform[platform_folder][category_folder_name] = []

                # Iterate through solution files inside the category folder
                for file_name in os.listdir(category_path):
                    file_path = os.path.join(category_path, file_name)

                    ext = os.path.splitext(file_name)[1].lower()
                    if os.path.isfile(file_path) and ext in language_map:
                        
                        # Default values (infer from path if not found in file)
                        problem_name = os.path.splitext(file_name)[0]
                        problem_url = "#"
                        language = language_map.get(ext, "Unknown")
                        platform_in_file = platform_folder # Default to folder name
                        category_in_file = category_folder_name # Default to folder name
                        tags_found = []
                        last_modified_date = None # Initialize last modified date
                        last_modified_month_year = None # For solving trend

                        # Try to extract details from file content (Problem, URL, Platform, Difficulty, Tags)
                        try:
                            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                                lines = [f.readline() for _ in range(20)]
                                content = "".join(lines)

                                name_match = re.search(r'(?:Problem:|# Problem:)\s*(.+)', content, re.IGNORECASE)
                                if name_match: problem_name = name_match.group(1).strip()
                                
                                url_match = re.search(r'(?:URL:|# URL:)\s*(https?://[^\s]+)', content, re.IGNORECASE)
                                if url_match: problem_url = url_match.group(1).strip()
                                
                                platform_match = re.search(r'(?:Platform:|# Platform:)\s*(.+)', content, re.IGNORECASE)
                                if platform_match: platform_in_file = platform_match.group(1).strip()
                                # No else for category_in_file from file content, relies on folder name if tag not found
                                category_tag_name = "Difficulty" if platform_folder != 'Codeforces' else "Rating"
                                category_match = re.search(r'(?:' + category_tag_name + r':|# ' + category_tag_name + r':)\s*(.+)', content, re.IGNORECASE)
                                if category_match: category_in_file = category_match.group(1).strip() # Overrides folder name if tag exists
                                
                                tag_match = re.search(r'(?:Tag:|# Tag:)\s*(.+)', content, re.IGNORECASE)
                                if tag_match:
                                    raw_tags = tag_match.group(1).split(',')
                                    tags_found = sorted([tag.strip() for tag in raw_tags if tag.strip()])

                            # Get last modified date from file system (still needed for Solving Trend)
                            mtime = os.path.getmtime(file_path)
                            dt_object = datetime.datetime.fromtimestamp(mtime, datetime.timezone.utc)
                            last_modified_date = dt_object.strftime('%Y-%m-%d') # Keep for internal use if needed
                            last_modified_month_year = dt_object.strftime('%Y-%m')

                        except Exception as e:
                            print(f"Warning: Could not read or parse '{file_path}' or get modification date for '{file_path}': {e}")
                        
                        # Store problem data
                        # Tuple: (name, url, language, tags, original_filename, platform_for_display, category_for_display, last_modified_date)
                        problem_data = (problem_name, problem_url, language, tags_found, file_name, platform_in_file, category_in_file, last_modified_date)
                        
                        all_problems_by_platform[platform_folder][category_folder_name].append(problem_data)
                        all_problem_items.append(problem_data)
                        total_problems_count += 1

                        # Update language counts
                        language_counts[language] += 1

                        # Update solving trend
                        if last_modified_month_year:
                            solving_trend_by_month[last_modified_month_year] += 1

                        # Populate problems_by_tag
                        for tag in tags_found:
                            if tag not in problems_by_tag:
                                problems_by_tag[tag] = []
                            # problem_data_for_tag: (name, url, language, platform_display, category_display, last_modified_date)
                            problems_by_tag[tag].append((problem_name, problem_url, language, platform_in_file, category_in_file, last_modified_date))

    # Sort problems within each category (alphabetically by problem name)
    for platform in all_problems_by_platform:
        for category in all_problems_by_platform[platform]:
            all_problems_by_platform[platform][category] = sorted(all_problems_by_platform[platform][category], key=lambda x: x[0].lower())

    # Sort problems within each tag (alphabetically by problem name)
    for tag in problems_by_tag:
        problems_by_tag[tag] = sorted(problems_by_tag[tag], key=lambda x: x[0].lower())

    # --- README Content Generation ---
    readme_content = []

    # 1. Main Header
    readme_content.append("# My Competitive Programming Journey 🚀\n")
    readme_content.append("Welcome to my comprehensive collection of solutions from various online judges! "
                          "This repository showcases problems solved on platforms like Codeforces, LeetCode, Beecrowd, HackerRank, and HackerEarth, "
                          "organized by platform, rating/difficulty, and algorithmic concept.\n\n")

    # --- Add Table of Contents Here ---
    readme_content.append("## Table of Contents\n")
    readme_content.append("- [📊 Journey Statistics](#-journey-statistics)\n")
    readme_content.append("- [✨ Spotlight Problem](#-spotlight-problem)\n")
    readme_content.append("- [🌐 Problems by Platform & Category](#-problems-by-platform--category)\n")
    readme_content.append("- [🧩 Problems by Concept/Tag](#-problems-by-concepttag)\n")
    readme_content.append("- [🗺️ My Learning Path & Advice](#️-my-learning-path--advice)\n")
    readme_content.append("- [🤝 Contributions & Feedback](#-contributions--feedback)\n")
    readme_content.append("\n") # Add a blank line for better spacing after TOC

    # 2. Overall Statistics & Badges
    readme_content.append("## 📊 Journey Statistics\n")
    readme_content.append(f"![Total Problems Solved](https://img.shields.io/badge/Total_Problems-{total_problems_count}-blue)\n\n")

    if all_problems_by_platform:
        readme_content.append("### Problem Distribution:\n")
        for platform in sorted(all_problems_by_platform.keys()):
            platform_problem_count = sum(len(all_problems_by_platform[platform][cat]) for cat in all_problems_by_platform[platform])
            readme_content.append(f"- **{platform}:** {platform_problem_count} problems\n")
            for category in sorted(all_problems_by_platform[platform].keys()):
                num_problems = len(all_problems_by_platform[platform][category])
                readme_content.append(f"  - *{category}:* {num_problems} problems\n")
        readme_content.append("\n")

    # Feature: Language Usage
    if language_counts:
        readme_content.append("### Language Usage\n")
        sorted_languages = sorted(language_counts.items(), key=lambda item: item[1], reverse=True)
        for lang, count in sorted_languages:
            percentage = (count / total_problems_count) * 100 if total_problems_count > 0 else 0
            readme_content.append(f"- **{lang}:** {percentage:.1f}% ({count} problems)\n")
        readme_content.append("\n")
    
    # Feature: Solving Trend
    if solving_trend_by_month:
        readme_content.append("### Solving Trend (Problems Solved by Month)\n")
        # Ensure months are sorted chronologically
        sorted_months = sorted(solving_trend_by_month.keys())
        for month_year in sorted_months:
            count = solving_trend_by_month[month_year]
            readme_content.append(f"- **{month_year}:** {count} problems\n")
        readme_content.append("\n")


    # 3. Problem of the Day/Week Spotlight
    if all_problem_items:
        random_problem = random.choice(all_problem_items)
        rp_name, rp_url, rp_lang, _, rp_original_filename, rp_platform_display, rp_category_display, _ = random_problem
        
        # Construct GitHub source link for the random problem
        rp_source_link_path = os.path.join(rp_platform_display, rp_category_display, rp_original_filename)
        rp_source_link = f"https://github.com/{GITHUB_USERNAME}/{GITHUB_REPO_NAME}/blob/main/{rp_source_link_path}"
        
        readme_content.append("## ✨ Spotlight Problem\n")
        readme_content.append(f"Feeling lucky? Here's a random problem from my collection:\n")
        readme_content.append(f"* **[{rp_name}]({rp_url})** "
                              f"([View Code]({rp_source_link})) "
                              f"(Platform: {rp_platform_display}, Category: {rp_category_display}, Language: {rp_lang})\n\n")

    # 4. Search/Filter Instructions
    readme_content.append("## 🔍 How to Explore\n")
    readme_content.append("You can easily navigate through the problems:\n")
    readme_content.append("- **By Platform & Category:** Browse the sections below for problems grouped by their original platform and then by their rating (for Codeforces) or difficulty (for others).\n")
    readme_content.append("- **By Concept/Tag:** Find problems categorized by the algorithms or data structures they use.\n")
    readme_content.append("- **GitHub Search:** Use GitHub's search bar (at the top of the repository page) to quickly find specific problem names or keywords within my solutions.\n\n")

    # 5. Problems by Platform & Category
    readme_content.append("## 🌐 Problems by Platform & Category\n")
    if not all_problems_by_platform:
        readme_content.append("No problems found categorized by platform yet. Please add your solution files into platform/category folders.\n\n")
    else:
        for platform_folder_name in sorted(all_problems_by_platform.keys()):
            readme_content.append(f"### {platform_folder_name}\n")
            
            category_display_name = "Rating" if platform_folder_name == 'Codeforces' else "Difficulty"

            for category_name in sorted(all_problems_by_platform[platform_folder_name].keys()):
                problems = all_problems_by_platform[platform_folder_name][category_name]
                readme_content.append(f"#### {category_display_name}: {category_name} ({len(problems)} Problems)\n\n")
                for problem_name, problem_url, language, _, original_filename, platform_display, category_display, _ in problems:
                    source_link_path = os.path.join(platform_folder_name, category_name, original_filename)
                    source_link = f"https://github.com/{GITHUB_USERNAME}/{GITHUB_REPO_NAME}/blob/main/{source_link_path}"

                    readme_content.append(f"* [{problem_name}]({problem_url}) "
                                          f"([View Code]({source_link})) "
                                          f"({language})\n")
                readme_content.append("\n")

    # 6. Problems by Concept/Tag
    readme_content.append("## 🧩 Problems by Concept/Tag\n")
    if not problems_by_tag:
        readme_content.append("No problems found with specific tags yet. Add `// Tag: YourTag1, YourTag2` to your solution files!\n\n")
    else:
        for tag in sorted(problems_by_tag.keys()):
            problems = problems_by_tag[tag]
            readme_content.append(f"### {tag} ({len(problems)} problems)\n\n")
            for problem_name, problem_url, language, platform_display, category_display, _ in problems:
                readme_content.append(f"* [{problem_name}]({problem_url}) "
                                      f"(Platform: {platform_display}, Category: {category_display}, Lang: {language})\n")
            readme_content.append("\n")

    # 7. A "Learning Path" Section
    readme_content.append("## 🗺️ My Learning Path & Advice\n")
    readme_content.append("This section reflects my approach to learning competitive programming across various platforms. "
                          "It might serve as a guide for others!\n\n")
    readme_content.append("### General Progression Tips:\n")
    readme_content.append("- **Build Foundations:** Start with 'Easy' problems on LeetCode or 'Rating 800-1000' on Codeforces. Focus on basic data structures, implementation, and I/O.\n")
    readme_content.append("- **Master Core Algorithms:** Once comfortable, move to 'Medium' problems and higher ratings. Deep dive into Dynamic Programming, Graph Traversal (BFS/DFS), Binary Search, Two Pointers, Greedy algorithms. Use the 'Problems by Concept/Tag' section to practice specific topics.\n")
    readme_content.append("- **Platform Nuances:** Be aware that each platform might have slightly different problem styles. LeetCode is great for interview prep, Codeforces for contest problem-solving, Beecrowd for pure logic/math.\n")
    readme_content.append("- **Consistent Practice:** Solve problems daily or weekly. Participate in contests to test your skills under pressure.\n")
    readme_content.append("- **Learn from Others:** Don't hesitate to look at solutions (after trying extensively!) to understand different approaches and optimizations.\n\n")

    # --- Add My Other Resources Here ---
    readme_content.append("### My Other Resources:\n")
    readme_content.append(f"- **C++ DSA Journey:** For detailed topic-wise discussions and implementations of Data Structures and Algorithms, check out my dedicated [Cpp-DSA-Journey repository](https://github.com/Angkon-Kar/Cpp-DSA-Journey).\n\n")


    # 8. Contribution Guidelines
    readme_content.append("## 🤝 Contributions & Feedback\n")
    readme_content.append("While this is primarily a personal repository, I welcome feedback and suggestions!\n")
    readme_content.append(f"- **Spot an optimization or a bug?** Feel free to open an [issue](https://github.com/{GITHUB_USERNAME}/{GITHUB_REPO_NAME}/issues) or a [pull request](https://github.com/{GITHUB_USERNAME}/{GITHUB_REPO_NAME}/pulls).\n")
    readme_content.append("- **Have questions about a solution?** Don't hesitate to ask by opening an issue.\n")
    readme_content.append("- **Want to use my solutions?** You're welcome to learn from them! Please attribute if you share them publicly.\n\n")

    # Footer with Timestamp
    readme_content.append("---\n")
    readme_content.append(f"*README generated on {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC*\n")

    # Write the combined content to README.md
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write("".join(readme_content))

if __name__ == "__main__":
    update_unified_readme()