from starlette.applications import Starlette # type: ignore
from starlette.responses import PlainTextResponse # type: ignore

app = Starlette()

@app.route("/")
async def homepage(request):
    return PlainTextResponse("Hola Mundo")

if __name__ == "__main__":
    import uvicorn # type: ignore
    uvicorn.run(app=app, host='0.0.0.0', port=8000)