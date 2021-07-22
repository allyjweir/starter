import pytest 
from starlette.testclient import TestClient
from starter.app import starter

client = TestClient(starter)

common_validation_test_cases = [
    ({'x': "string", 'y': 2}, 'x', "Not a valid number."),
    ({'x': True, 'y': 2}, 'x', "Not a valid number."),
    ({'x': None, 'y': 2}, 'x', "Field may not be null."),
    ({'x': 1, 'y': "string"}, 'y', "Not a valid number."),
    ({'x': 1, 'y': True}, 'y', "Not a valid number."),
    ({'x': 1, 'y': None}, 'y', "Field may not be null."),
    ({'x': 1, 'y': {}}, 'y', "Not a valid number."),
]


'''
Addition endpoint tests
'''
@pytest.mark.parametrize("test_input,expected", [
    ({'x': 1, 'y': 2}, 3.0),
    ({'x': -99999.124032984e12, 'y': 999999.123124e16}, 9.999891232115967e+21),
])
def test_valid_additions(test_input, expected):
    response = client.post('/addition/', json=test_input)
    assert response.status_code == 200
    assert response.json()['result'] == expected

@pytest.mark.parametrize("test_input, invalid_key, expected_error", common_validation_test_cases)
def test_addition_returns_error_on_invalid_input(test_input, invalid_key, expected_error):
    response = client.post('/addition/', json=test_input)
    assert response.status_code == 400
    assert response.json()['validation_errors'][invalid_key] == [expected_error]


'''
Subtraction endpoint tests
'''
@pytest.mark.parametrize("test_input,expected", [
    ({'x': 1, 'y': 2}, -1.0),
    ({'x': -99999.124032984e12, 'y': 999999.123124e16}, -1.0000091230364034e+22),
])
def test_valid_subtractions(test_input, expected):
    response = client.post('/subtraction/', json=test_input)
    assert response.status_code == 200
    assert response.json()['result'] == expected

@pytest.mark.parametrize("test_input, invalid_key, expected_error", common_validation_test_cases)
def test_subtraction_returns_error_on_invalid_input(test_input, invalid_key, expected_error):
    response = client.post('/subtraction/', json=test_input)
    assert response.status_code == 400
    assert response.json()['validation_errors'][invalid_key] == [expected_error]


'''
Division endpoint tests
'''
@pytest.mark.parametrize("test_input,expected", [
    ({'x': 8, 'y': 2}, 4.0),
    ({'x': -99999.124032984e12, 'y': 999999.123124e16}, -9.999921171989277e-06),
])
def test_valid_division(test_input, expected):
    response = client.post('/division/', json=test_input)
    assert response.status_code == 200
    assert response.json()['result'] == expected

@pytest.mark.parametrize("test_input, invalid_key, expected_error", common_validation_test_cases)
def test_division_returns_error_on_invalid_input(test_input, invalid_key, expected_error):
    response = client.post('/division/', json=test_input)
    assert response.status_code == 400
    assert response.json()['validation_errors'][invalid_key] == [expected_error]