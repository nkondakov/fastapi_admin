from fastapi import Request, APIRouter
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("account/index.html", {"request": request, "user": "Nick"})
