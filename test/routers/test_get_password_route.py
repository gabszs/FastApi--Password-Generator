from fastapi import status


def test_pass_get_route(client):
    response = client.get("pass/10?quantity=3&ponctuation=True")
    response_json = response.json()

    assert response.status_code == status.HTTP_200_OK

    assert len(response_json["data"]) == 3
    assert isinstance(response_json["data"], list)

    assert len(response_json["data"][0]["1º pin"]) == 10
    assert str(response_json["data"][0]["1º pin"]).isascii()

    assert len(response_json["data"][1]["2º pin"]) == 10
    assert str(response_json["data"][1]["2º pin"]).isascii()

    assert len(response_json["data"][2]["3º pin"]) == 10
    assert str(response_json["data"][2]["3º pin"]).isascii()


def test_pass_get_no_ponctuation_route(client):
    response = client.get("pass/10?quantity=3")
    response_json = response.json()

    assert response.status_code == status.HTTP_200_OK

    assert len(response_json["data"]) == 3
    assert isinstance(response_json["data"], list)

    assert len(response_json["data"][0]["1º pin"]) == 10
    assert str(response_json["data"][0]["1º pin"]).isalnum()

    assert len(response_json["data"][1]["2º pin"]) == 10
    assert str(response_json["data"][1]["2º pin"]).isalnum()

    assert len(response_json["data"][2]["3º pin"]) == 10
    assert str(response_json["data"][2]["3º pin"]).isalnum()
