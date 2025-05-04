import uvicorn

API_PATH = "api.app:app"  # TODO: to .env
HOST = "0.0.0.0"  # TODO: to .env
PORT = 8000  # TODO: to .env

if __name__ == "__main__":
    uvicorn.run(API_PATH, host=HOST, port=PORT, reload=True)
