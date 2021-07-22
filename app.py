from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.middleware import Middleware
from starlette.routing import Route
from starlette_prometheus import metrics, PrometheusMiddleware
from prometheus_client import Counter

greetings_counter = Counter(
    "greetings_given", "the number of times we have said hello on the homepage"
)


async def homepage(request):
    greetings_counter.inc()
    return JSONResponse({"hello": "dan"})


starter = Starlette(
    debug=True,
    middleware=[
        Middleware(PrometheusMiddleware),
    ],
    routes=[
        Route("/", homepage),
        Route("/metrics/", metrics),
    ],
)
