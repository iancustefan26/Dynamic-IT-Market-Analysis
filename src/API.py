from fastapi import FastAPI, HTTPException
from uuid import UUID, uuid4
from typing import List, Dict, Optional
from models import Job
from usable import roles, skills
from statistics_calculator import calculate_statistics

app = FastAPI()

@app.get('/')
async def home():
    return {
        "Status" : "Ok",
        "Engine" : "Job Scraper",
        "Page" : "This is the home page"
    }
@app.get('/about')
async def about():
    return {
        "Status" : "Ok",
        "Page" : "About Page",
    }

@app.get('/jobs/all', response_model= Dict[str, Job])
async def get_all_jobs() -> Dict[str, Job]:
    new = {}
    for skill in skills:
        temp = calculate_statistics(skill=skill)
        new[str(skill)] = Job(title='ALL', statistics=temp)
    if len(new) == 0:
        raise HTTPException(
            status_code=204,
            detail={
                "Internal error" : "No content, database empty"
            }
        )
    return new

@app.get('/jobs/{job_name}', response_model = Job)
async def get_job(job_name : str) -> Job:
    if job_name not in roles:
        raise HTTPException(
            status_code=404,
            detail={
                "Error" : "Job not found"
            }
        )
    temp = {}
    for skill in skills:
        temp[skill] = calculate_statistics(job_name, skill)

    if len(temp) == 0:
        raise HTTPException(
            status_code=204,
            detail={
                "Internal error" : "No content, database empty"
            }
        )

    return Job(
        title = job_name,
        statistics=temp
    )

@app.get('/jobs/{job_name}/{skill_name}', response_model=Job)
async def get_job_skill(job_name:str, skill_name: str) -> Job:
    if job_name not in roles:
        raise HTTPException(
            status_code=404,
            detail={
                "Error" : "Job not found"
            }
        )
    if skill_name not in skills:
        raise HTTPException(
            status_code=404,
            detail={
                "Error" : "Skill not found"
            }
        )
    temp = calculate_statistics(job_name, skill_name)
    if len(temp) == 0:
        raise HTTPException(
            status_code=204,
            detail={
                "Internal error" : "No content, database empty"
            }
        )
    return Job(
        title=job_name,
        statistics=temp
    )

@app.get('/jobs', response_model=Job)
async def get_skill_for_all_jobs(skill : str) -> Job:
    if skill not in skills:
        raise HTTPException(
            status_code=404,
            detail={
                "Error" : "Skill not found"
            }
        )
    for role in roles:
        temp = calculate_statistics(skill=skill)
    if len(role) == 0:
        raise HTTPException(
            status_code=204,
            detail={
                "Internal Error" : "No content, database empty"
            }
        )
    return Job(
        title='ALL',
        statistics=temp
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host = '0.0.0.0', port = 8000)