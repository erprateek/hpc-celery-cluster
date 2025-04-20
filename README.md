# 🚀 FastAPI + Celery + Redis with Docker (WSL2 HPC Mock Cluster)

This repo demonstrates a distributed task queue architecture using **FastAPI** (as master), **Celery workers**, and **Redis** as the message broker. Ideal for learning task orchestration, background job handling, and basic HPC-style task delegation — all within Docker on WSL2.

## 📦 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [Celery](https://docs.celeryq.dev/)
- [Redis](https://redis.io/)
- [Docker](https://www.docker.com/)
- WSL2 (for Linux container compatibility on Windows)

## ⚙️ Project Structure

```
.
├── celery_worker.py     # Defines the Celery app and task(s)
├── main.py              # FastAPI app with task submission & status routes
├── Dockerfile           # Builds app container
├── docker-compose.yml   # Orchestrates FastAPI, Redis, and workers
└── requirements.txt     # Python dependencies
```

## 🚀 How to Run

### 1. Prerequisites

- [Docker Desktop (with WSL2 backend)](https://docs.docker.com/desktop/windows/wsl/)
- Git
- VSCode (recommended)

### 2. Clone the Repo

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 3. Start the Cluster

```bash
docker-compose up --build
```

This will spin up:
- `master` → FastAPI app on `localhost:8000`
- `redis`  → Redis broker
- `worker1` & `worker2` → Celery workers waiting for tasks

### 4. Submit a Task

```bash
curl -X POST http://localhost:8000/add      -H "Content-Type: application/json"      -d '{"x": 5, "y": 7}'
```

📥 Response:
```json
{ "task_id": "some-task-uuid" }
```

### 5. Check Task Status

```bash
curl http://localhost:8000/status/<task_id>
```

📤 Sample response:
```json
{
  "task_id": "<task_id>",
  "status": "SUCCESS",
  "result": 12
}
```

## 📁 Example Task (`celery_worker.py`)

```python
from celery import Celery
import os

broker = os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0")
celery = Celery("tasks", broker=broker, backend=broker)

@celery.task
def add(x, y):
    return x + y
```

## 📑 API Routes

| Route               | Method | Description                    |
|--------------------|--------|--------------------------------|
| `/add`             | POST   | Submit a task (add x + y)      |
| `/status/{task_id}`| GET    | Get task status and result     |
| `/result/{task_id}`| GET    | Get final result (optional)    |

## 🧪 Dev Tips

- Use the Swagger UI at [http://localhost:8000/docs](http://localhost:8000/docs)
- To rebuild after code changes:
  ```bash
  docker-compose down
  docker-compose up --build
  ```

## 🧼 TODO Ideas

- Add more task types (e.g., simulate long-running tasks)
- Connect PostgreSQL to persist results
- Add unit/integration tests
- Deploy with Docker Swarm / Kubernetes

## 🧠 Credits

Built for educational and testing purposes. Inspired by distributed computing and task orchestration in HPC environments.

## 🔐 License

MIT
