from fastapi import FastAPI, HTTPException
from uuid import UUID, uuid4
from typing import List, Dict, Optional
from models import Job
from usable import roles, skills
from statistics_calculator import calculate_statistics

app = FastAPI()

@app.get('/')
async def root():
    return {
        "Status" : "Ok",
        "Engine" : "Job Scraper"
    }

@app.get('/jobs', response_model= Dict[str, Job])
async def get_all_jobs() -> Dict[str, Job]:
    new = {}
    for skill in skills:
        temp = calculate_statistics(skill=skill)
        new[str(skill)] = Job(title='ALL', statistics=temp)
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
    return Job(
        title=job_name,
        statistics=calculate_statistics(job_name, skill_name)
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host = '0.0.0.0', port = 8000)