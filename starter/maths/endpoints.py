import random

from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint
from marshmallow import ValidationError

from .schemas import (
    parse_and_validate_request_data,
    TwoNumberSchema,
    RandomSchema,
    RandomResultSchema,
    ResultSchema,
    ErrorResponseSchema,
)


class Addition(HTTPEndpoint):
    async def post(self, request):
        try:
            json_body = await request.json()
            data = parse_and_validate_request_data(TwoNumberSchema, json_body)
        except ValidationError as err:
            response_data = ErrorResponseSchema().dump(
                {"validation_errors": err.messages}
            )
            return JSONResponse(response_data, 400)

        response_data = ResultSchema().dump({"result": data["x"] + data["y"]})
        return JSONResponse(response_data)


class Subtraction(HTTPEndpoint):
    async def post(self, request):
        try:
            json_body = await request.json()
            data = parse_and_validate_request_data(TwoNumberSchema, json_body)
        except ValidationError as err:
            response_data = ErrorResponseSchema().dump(
                {"validation_errors": err.messages}
            )
            return JSONResponse(response_data, 400)

        response_data = ResultSchema().dump({"result": data["x"] - data["y"]})
        return JSONResponse(response_data)


class Division(HTTPEndpoint):
    async def post(self, request):
        try:
            json_body = await request.json()
            data = parse_and_validate_request_data(TwoNumberSchema, json_body)
        except ValidationError as err:
            response_data = ErrorResponseSchema().dump(
                {"validation_errors": err.messages}
            )
            return JSONResponse(response_data, 400)

        response_data = ResultSchema().dump({"result": data["x"] / data["y"]})
        return JSONResponse(response_data)


class Random(HTTPEndpoint):
    async def post(self, request):
        try:
            json_body = await request.json()
            data = parse_and_validate_request_data(RandomSchema, json_body)
        except ValidationError as err:
            response_data = ErrorResponseSchema().dump(
                {"validation_errors": err.messages}
            )
            return JSONResponse(response_data, 400)

        response_data = RandomResultSchema().dump(
            {"result": random.sample(range(0, 9999999999999), data["count"])}
        )
        return JSONResponse(response_data)
