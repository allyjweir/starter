from marshmallow import Schema, fields, ValidationError


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


class SubtractionSchema(Schema):
    """
    The spec specified that the values in this needed to be 'real' numbers as
    opposed to just 'numbers' when specified in the other endpoints. Hence, this
    schema is unique to allow for the definition of a 'real number'.

    Examples of real numbers:
    - Rational numbers (examples are 5, -5, 0.42)
    - Irrational numbers (examples are π, √2)
    """

    # TODO: Write the schema
    pass


class RandomSchema(Schema):
    count = fields.Number(required=False)


class ErrorResponseSchema(Schema):
    validation_errors = fields.Dict()


class ResultSchema(Schema):
    result = fields.Number(required=True)


class RandomResultSchema(Schema):
    result = fields.List(fields.Number, required=True)
