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


async def liveness(request):
    """This endpoint purely serves as a check to see if the application itself
    is up and is alive. It returning a 200 does not indicate that it is ready
    to accept traffic.
    """
    return JSONResponse({"status": "still alive"})


async def readiness(request):
    """Typically this is where we would validate all external dependencies such
    as caches, and databases are healthy and ready to go.

    Since this application is an example, we are not going to do any real work
    here. Instead, the readiness check will fail the first two times Kubernetes
    tries to hit it. This simulates the application waiting for readiness.
    """
    if request.app.state.READINESS_FAIL_COUNT < 2:
        request.app.state.READINESS_FAIL_COUNT += 1
        return JSONResponse({"status": "not ready"}, 500)
    return JSONResponse({"status": "ready"})


starter = Starlette(
    debug=True,
    middleware=[
        Middleware(PrometheusMiddleware),
    ],
    routes=[
        Route("/", homepage),
        Route("/healthz/liveness", liveness),
        Route("/healthz/readiness", readiness),
        Route("/metrics/", metrics),
        Route("/addition/", Addition),
        Route("/subtraction/", Subtraction),
        Route("/division/", Division),
        Route("/random/", Random),
    ],
)
starter.state.READINESS_FAIL_COUNT = 0
