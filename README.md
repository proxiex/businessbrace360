# businessbrace360

With the current situation with Covid-19 epidemic, this is a web platform that allows testing candidates for recruitment remotely.

## Features
- Create new job posting or offers (admin)
- View job posting
- Apply for job posting
- View and review all candidates
- Move candidate from `job applicant` to `Test candidate` to `Succesful candidate` (admin)
- Candidate get's email with datails of test 
- Recored candidate score (admin)
- Sign in
- Record signed company documents uploads
- Recored personal information
- Record certificat upload
- Monitor and update candidate onboarding process progress (admin)



## Installation Guide

### Development Environment
- Ensure you have Postgresql installed and running on your computer
- Clone this repository with `git clone https://github.com/proxiex/businessbrace360.git`
- `cd businessbrace360`
- Install virtualenv `pip install virtualenv`
- Create virtual env `python3 -m virtualenv venv`
- Activate virtual env `source venv/bin/activate`
- make a copy of `.env.example` and edit as approriate to `.env` file
- Install dependencies `pip install -r requirements.txt`
- Start app `python manage.py runserver`
- Navigate to `localhost:8000/api/v1`

## Technologies
- Python3/Django: A Python web framework
- Postgresql: Relational Database Management System 
