from app.schemas.Output_Scheme import PasswordOutput


def test_output_scheme():
    output_scheme = PasswordOutput(message="Success", data=[{"name1": "Gabriel", "name2": "Pedro"}])

    assert output_scheme.dict() == {
        "message": "Success",
        "data": [{"name1": "Gabriel", "name2": "Pedro"}],
    }
