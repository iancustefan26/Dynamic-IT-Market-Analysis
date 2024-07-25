from scraper import get_skills_for_all_roles
from scraper import get_skills_for_role
from json_convertor import extract_countries

roles = [
    "Software Engineer",
    "Data Scientist",
    "Machine Learning Engineer",
    "Cloud Engineer",
    "Cybersecurity Specialist"
]

locations = extract_countries(90)

print(locations)