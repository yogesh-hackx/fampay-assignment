
# Fampay-Assignment (Youtube Latest Videos API)

A backend service that fetches youtube videos on cricket uploaded in last 10 minutes

[![portfolio](https://img.shields.io/badge/live_demo-ff?style=for-the-badge&&logoColor=white)](https://fampay-assignment.yogicodes.com/)

[Live Demo](https://fampay-assignment.yogicodes.com/) 👈️
## API Reference

#### Get videos 👉️  [Live Demo](https://fampay-assignment.yogicodes.com/videos/) 

```http
  GET /videos
```

| Parameter | Type     | Description                |Live Demo|
| :-------- | :------- | :------------------------- | :----|
| `search` | `string` | query to search in the database |[/?search=kohli](https://fampay-assignment.yogicodes.com/videos/?search=kohli) |
| `limit` | `number` | number of records to fetch |[/?limit=2](https://fampay-assignment.yogicodes.com/videos/?limit=2) |
| `offset` | `number` | number of records to skip |[/?offset=2](https://fampay-assignment.yogicodes.com/videos/?limit=2&offset=2) |



## Features

- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- A basic search API to search the stored videos using their title and description.
- Dockerized the project.
- Support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.
- Dashboard (Work in progress in Next.js), till than Django admin could be used with username: `admin`, and, password: `admin`
- It is able to search videos containing partial match for the search query in either video title or description.
    - Ex 1: A video with title *`IND vs PAK Match, High Voltage Inning`* matches for the search query `match inning`
  
## Installation

Clone the repo

```bash
  git clone https://github.com/yogesh-hackx/fampay-assignment
```

Go to project directory and run

```bash
  sudo docker compose up
```

when project completely boots up and is running, open another terminal in the project root and run:

```bash
  sudo docker compose exec web python manage.py createsuperuser
```

Create credentials for django-admin, then login to django-admin, and add API keys