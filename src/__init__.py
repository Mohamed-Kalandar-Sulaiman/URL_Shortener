from fastapi import FastAPI, Response
from routers import miniurlRouter

app = FastAPI(debug=True,
              title="Miniurl")

app.include_router(router=miniurlRouter)

@app.get(path="/test")
def test():
    return Response(status_code=200)


    
    