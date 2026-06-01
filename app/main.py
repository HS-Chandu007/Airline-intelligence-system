import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.preprocessing import prepare_dataframe
from app.inference import InferencePipeline

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = FastAPI(title="Airline Customer Intelligence System")

pipeline = InferencePipeline()

app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    text: str = Form(...),
    airline: str = Form(...)
):
    df = prepare_dataframe(text=text, airline=airline)
    result = pipeline.predict(df)

    return templates.TemplateResponse(
        request=request,
        name="prediction.html",
        context={
            "result": result,
            "text": text,
            "airline": airline
        }
    )