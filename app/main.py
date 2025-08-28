from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
 

app = FastAPI()
from app.app_routes import router
from fastapi.middleware.cors import CORSMiddleware


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """
    Middleware that checks for the 'X-Forwarded-For' header in each incoming request.
    If the header is missing, it returns a 400 response.
    Otherwise, the request is passed along to the next handler.
    """


    current_client_ip = request.headers.get("X-Forwarded-For")
    if not current_client_ip:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"error": "No client ip provided"},
        )
    response = await call_next(request)
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)
