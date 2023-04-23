from fastapi import FastAPI
from backend.app.core.config import Settings
from backend.app.api.api import api_router
from backend.app.core.config import Settings


def start_application(config: Settings):
    application = FastAPI(
        debug=True,
        title=config.PROJECT_NAME,
        version=config.PROJECT_VERSION,
        description=""
    )
    return application


settings = Settings()

app = start_application(settings)
app.include_router(api_router)
