import time
from fastapi.testclient import TestClient
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../master")))
from main import app

client = TestClient(app)

def test_add_task():
    print("Reached here: ")
    response = client.post("/add", json={"x": 4, "y": 6})
    assert response.status_code == 200
    data = response.json()
    assert "task_id" in data
    task_id = data["task_id"]
    print(task_id)
    # Poll for result (in real scenarios use backoff strategy)
    for _ in range(10):
        result_response = client.get(f"/result/{task_id}")
        result_data = result_response.json()
        if result_data.get("result") is not None:
            assert result_data["result"] == 10
            break
        time.sleep(1)
    else:
        assert False, "Task did not complete in expected time"
