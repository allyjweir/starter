from marshmallow import Schema, fields, validates, ValidationError


def parse_and_validate_request_data(schema_class, request_data):
    schema = schema_class()
    try:
        result = schema.load(request_data)
        return result
    except ValidationError as err:
        raise err


class TwoNumberSchema(Schema):
    """
    Common schema for math operations such as add and division
    """

    x = fields.Number(required=True)
    y = fields.Number(required=True)


class RandomSchema(Schema):
    count = fields.Integer(required=False, strict=True, load_default=10)

    @validates("count")
    def validate_count(self, value):
        if value < 0:
            raise ValidationError("count must be a positive integer")


class ErrorResponseSchema(Schema):
    validation_errors = fields.Dict()


class ResultSchema(Schema):
    result = fields.Number(required=True)


class RandomResultSchema(Schema):
    result = fields.List(fields.Number, required=True)
