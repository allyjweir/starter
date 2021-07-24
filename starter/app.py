from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.middleware import Middleware
from starlette.routing import Route
from starlette_prometheus import metrics, PrometheusMiddleware
from prometheus_client import Counter

from maths.endpoints import (
    Addition,
    Subtraction,
    Division,
    Random,
)


greetings_counter = Counter(
    "greetings_given", "the number of times we have said hello on the homepage"
)


async def homepage(request):
    greetings_counter.inc()
    return JSONResponse({"hello": "world"})


starter = Starlette(
    debug=True,
    middleware=[
        Middleware(PrometheusMiddleware),
    ],
    routes=[
        Route("/", homepage),
        Route("/metrics/", metrics),
        Route("/addition/", Addition),
        Route("/subtraction/", Subtraction),
        Route("/division/", Division),
        Route("/random/", Random),
    ],
)
