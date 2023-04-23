from fastapi import FastAPI
import uvicorn
import numpy as np
import time

app = FastAPI()

@app.get("/compute")
def compute(n: int):
    # Timeit to benchmark the performance of numpy 
    t = time.time()
    for _ in range(n):
        a = np.random.rand(1000, 1000)
        b = np.random.rand(1000, 1000)
        c = np.dot(a, b)
    return {"process-time": "%.3f" % ((time.time() - t)/n)}


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(
        "myapp.main:app",
        host="0.0.0.0",
        port=8000,
        workers=4,
        log_level="info",
        limit_max_requests=10_000,
    )