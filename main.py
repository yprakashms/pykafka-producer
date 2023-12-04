from fastapi import FastAPI
import router
import uvicorn

app = FastAPI()


@app.get('/')
async def home():
    return "welcome home"

app.include_router(router.route)
# asyncio.create_task(router.consume())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
