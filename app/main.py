from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.api.sensor.routes import sensor

from app.utils.exceptions import CustomBaseException, custom_exception_handler
app = FastAPI()

# Attaching routers to app
app.include_router(sensor)

# Attaching error handlers to app
app.add_exception_handler(CustomBaseException, custom_exception_handler)

@app.get("/")
def index():
    return RedirectResponse(url="/docs")
