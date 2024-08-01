from serpapi import GoogleSearch
from usable import *

serp_api_token = open('/Users/stefaniancu/Documents/VS Code/JobScraperEngine/API_TOKENS/serpapitoken.txt').read(256)

tools = {
    "Tableau" : 0,
    'Excel' : 0,
    'Word' : 0,
    'SAS' : 0,
    'PowerPoint' : 0,
    'SAP' : 0,
    'Looker' : 0,
    'SSIS' : 0,
    'Docker' : 0,
    'Kubernetes' : 0,
    'Linux' : 0
}

databases = {
    'Server' : 0,
    'MySQL' : 0,
    'Postgre' : 0,
    'Cassandra' : 0,
    'Mongo' : 0,
    'Firebase' : 0,
    'Elasticsearch' : 0,
    'Dynamo' : 0
}

cloud = {
    'AWS' : 0,
    'Azure' : 0,
    'Google' : 0,
    'Snowflake' : 0,
    'Databricks' : 0,
    'Redshift' : 0,
    'Oracle' : 0,
    'Redshift' : 0,
    'GCP' : 0
}

libraries = {
    'Spark' : 0,
    'Hadoop' : 0,
    'Kafka' : 0,
    'Airflow' : 0,
    'PySpark' : 0,
    'TensorFlow' : 0,
    'Pandas' : 0,
    'PyTorch' : 0,
    'NumPy' : 0,
    'Spring' : 0,
    'Matplotlib' : 0
}

frameworks = {
    'Express' : 0,
    'Node' : 0,
    'Angular' : 0,
    'Flask' : 0,
    'Django' : 0,
    'Phoenix' : 0,
    'Vue' : 0,
    'FastAPI' : 0,
    '¡Query' : 0,
    'Ruby on Rails' : 0,
    '.NET' : 0
}

languages = {
    'C++' : 0,
    'C' : 0,
    'Fortran' : 0,
    'Java' : 0,
    'Python' : 0,
    'PHP' : 0,
    'Ruby' : 0,
    'Rust' : 0,
    'C#' : 0,
    'Go' : 0,
    'JavaScript' : 0,
    'R' : 0,
    'Bash' : 0,
    'SQL' : 0,
    'NoSQL' : 0
}

all_skills = [
    languages,
    cloud,
    tools,
    databases,
    frameworks,
    libraries
]


def get_skills_for_role(role_name, locations):
    global all_skills, serp_api_token
    for location in locations:
        params = {
            "engine": "google_jobs",
            "location" : location,
            "q": role_name,
            "hl": "en",
            "api_key": serp_api_token
        }
        search = GoogleSearch(params)
        results = search.get_dict().get('jobs_results', [])
        for job in results:
            job_highlights = job.get('job_highlights', [])
            for highlight in job_highlights:
                items = highlight.get('items', [])
                for item in items:
                    for skill in all_skills:
                        for niche in skill:
                            if len(niche) == 1:
                                if check_isolated_letter(item, niche):
                                    skill[niche] += 1
                            elif check_isolated_word(item, niche) or niche in item:
                                skill[niche] += 1
                job_description = job.get('description', [])
                for skill in all_skills:
                    for niche in skill:
                        if len(niche) == 1:
                            if check_isolated_letter(job_description, niche):
                                skill[niche] += 1
                        elif check_isolated_word(job_description, niche) or niche in item:
                            skill[niche] += 1
    return all_skills
