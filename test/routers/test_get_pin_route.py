from fastapi import status


def test_pin_unique_route(client):
    response = client.get("/v1/pin?password_length=4&quantity=5")
    response_json = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(response_json["data"]) == 5
    assert isinstance(response_json["data"], list)

    for pin in response_json["data"]:
        assert isinstance(pin, str)
        assert len(pin) == 4
        assert pin.isnumeric()
