from fastapi import status


def test_pass_get_route(client):
    response = client.get("/v1/?password_length=10&quantity=3&has_punctuation=true")
    response_json = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(response_json["data"]) == 3
    assert isinstance(response_json["data"], list)

    for password in response_json["data"]:
        assert isinstance(password, str)
        assert len(password) == 10
        assert password.isascii()


def test_pass_get_no_punctuation_route(client):
    response = client.get("/v1/?password_length=10&quantity=3&has_punctuation=false")
    response_json = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(response_json["data"]) == 3
    assert isinstance(response_json["data"], list)

    for password in response_json["data"]:
        assert isinstance(password, str)
        assert len(password) == 10
        assert password.isalnum()
