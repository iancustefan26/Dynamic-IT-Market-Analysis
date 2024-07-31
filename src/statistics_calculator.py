from store_into_database import extract_count_for_role
from scraper import roles
from usable import roles_id

def calculate_statistics(role = "ALL", skill = "languages"):
    global roles
    percentages = {}
    counts = {}
    total_count = 0
    if role == "ALL":
        for role in roles:
            data = extract_count_for_role(roles_id[role], skill)
            for row in data:
                total_count += row[2]
                if counts.get(row[1], "") != "":
                    counts[row[1]] += row[2]
                else:
                    counts[row[1]] = row[2]
            for row in counts:
                if counts[row] != 0:
                    percentages[row] = round(counts[row] / total_count * 100, 2)
                else:
                    percentages[row] = 0.00
    else:
        data = extract_count_for_role(roles_id[role], skill)
        for row in data:
            total_count += row[2]
            if counts.get(row[1], "") != "":
                counts[row[1]] += row[2]
            else:
                counts[row[1]] = row[2]
        for row in counts:
            if counts[row] != 0:
                percentages[row] = round(counts[row] / total_count * 100, 2)
            else:
                percentages[row] = 0.00
    return percentages

for role in roles:
        print(role, calculate_statistics(role, "languages"), end = "\n")