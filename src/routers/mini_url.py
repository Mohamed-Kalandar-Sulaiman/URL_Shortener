from fastapi import APIRouter
from fastapi import Request,Response

miniurlRouter = APIRouter()


@miniurlRouter.post(path="/create")
def create_short_url(request:Request):
    request.path_params()
    return Response(status_code=200)


@miniurlRouter.get(path="/}")
def get_long_url(miniurl):
    return Response(status_code=200)
    pass









