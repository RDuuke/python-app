from starlette.applications import Starlette
from starlette.responses import PlainTextResponse

app = Starlette()

@app.route("/")
async def homepage(request):
    return PlainTextResponse("Hola Mundo")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app, host='0.0.0.0', port=8000)