import os
import re
import datetime

def update_readme():
    """
    Scans the current directory for subfolders named after problem ratings (e.g., '800', '900').
    It then lists all .cpp, .py, or .java files within these folders, extracts problem details
    (name, URL, language), and generates a README.md file, categorizing problems by their rating.
    It also includes problem counts.
    """
    readme_header = "# Codeforces Problems\n\n" \
                    "This repository contains my solutions to Codeforces problems, organized by rating.\n\n"

    all_problems_data = {} # To store problems: {rating: [(problem_name, url, language, filename), ...]}
    total_problems_count = 0

    # Define a mapping for file extensions to language names
    language_map = {
        '.cpp': 'C++',
        '.py': 'Python',
        '.java': 'Java',
        # Add more extensions and languages if needed
    }

    # Iterate through all items in the current directory
    for item in os.listdir('.'):
        # Check if it's a directory and its name is a digit (representing a rating)
        if os.path.isdir(item) and item.isdigit():
            rating = int(item)
            problems_in_rating = []

            # Iterate through files within the rating folder
            for file_name in os.listdir(item):
                file_path = os.path.join(item, file_name)
                
                # Check if it's a file and has a recognized extension
                ext = os.path.splitext(file_name)[1].lower()
                if os.path.isfile(file_path) and ext in language_map:
                    
                    problem_name = file_name # Default to filename if name not found
                    problem_url = "#"      # Default to a local anchor if URL not found
                    language = language_map.get(ext, "Unknown") # Get language from map
                    
                    # Try to extract Problem Name and URL from file content
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            # Read first few lines for efficiency
                            lines = [f.readline() for _ in range(10)] # Read up to 10 lines
                            content = "".join(lines)

                            # Regex to find Problem Name
                            name_match = re.search(r'(?:Problem:|# Problem:)\s*(.+)', content, re.IGNORECASE)
                            if name_match:
                                problem_name = name_match.group(1).strip()
                            
                            # Regex to find URL
                            url_match = re.search(r'(?:URL:|# URL:)\s*(https?://[^\s]+)', content, re.IGNORECASE)
                            if url_match:
                                problem_url = url_match.group(1).strip()
                            elif problem_name and not url_match: # Fallback to Codeforces standard if name is found but URL isn't
                                # Attempts to construct a URL if problem name has contest/problem ID pattern
                                # This is a heuristic and might not always work perfectly without full context.
                                contest_problem_match = re.search(r'([A-Za-z]?\d+)[A-Za-z]?$', problem_name)
                                if contest_problem_match:
                                    # This part is highly heuristic. Codeforces URLs are structured
                                    # like contestID/problemID. If you always name your files consistently,
                                    # for example, using "contestID_problemLetter.cpp" (e.g., 123A.cpp),
                                    # you might try to parse contest ID from filename.
                                    # For more robust linking, manual URL in file is best.
                                    pass # Stick to default '#' or rely on explicitly written URL in file
                                
                    except Exception as e:
                        print(f"Warning: Could not read or parse '{file_path}': {e}")
                    
                    problems_in_rating.append((problem_name, problem_url, language, file_name))
                    total_problems_count += 1
            
            if problems_in_rating: # Only add if there are problems in this rating
                all_problems_data[rating] = sorted(problems_in_rating, key=lambda x: x[0].lower()) # Sort problems alphabetically

    # --- Construct README Content ---
    readme_content = readme_header
    
    # Add Total Problems Badge (Feature 5 - text-based)
    readme_content += f"![Total Problems](https://img.shields.io/badge/Total_Problems-{total_problems_count}-blue)\n\n"
    
    readme_content += "## Problems by Rating\n\n"

    # Sort ratings in ascending order to display them nicely
    for rating in sorted(all_problems_data.keys()):
        problems = all_problems_data[rating]
        readme_content += f"### Rating: {rating} ({len(problems)} Problems)\n\n" # Feature 2: Problem Count

        for problem_name, problem_url, language, original_filename in problems:
            # Feature 1 (Problem Link) & Feature 4 (Language)
            readme_content += f"* [{problem_name}]({problem_url}) ({language})\n"
        readme_content += "\n"
    
    # Add a footer with last updated timestamp
    readme_content += f"\n---\n*README generated on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC*"


    # Write the generated content to README.md
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

if __name__ == "__main__":
    update_readme()