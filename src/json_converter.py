import json
import re
from usable import check_isolated_word

def contains_single_letter(text, letter):
    allowed_surroundings = r'\s\.,;\/\\|\b'
    pattern = rf'(?<=[{allowed_surroundings}]){re.escape(letter)}(?=[{allowed_surroundings}])'
    matches = re.findall(pattern, text)
    return bool(matches)


json_content = open("/Users/stefaniancu/DOcuments/VS Code/JobScraperEngine/jsons/one_search.json").read(200000)

jobs = json.loads(json_content).get('jobs_results', [])

count = 0
strings = []

for job in jobs:
    job_highlights = job.get('job_highlights', [])
    for highlight in job_highlights:
        items = highlight.get('items', [])
        for item in items:
            #print(item, end = "\n\n")
            if check_isolated_word("C++", item) or "C++" in item:
                count += 1
                strings.append(item)

for string in strings:
    print(string)

print(count)
