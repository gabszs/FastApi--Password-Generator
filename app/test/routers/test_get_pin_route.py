from fastapi.testclient import TestClient
from app.main import app
from fastapi import status
import json

client = TestClient(app=app)

def test_pin_unique_route():
    response = client.get('/password/pin/4?quantity=5')
    response_json = response.json()

    assert response.status_code == status.HTTP_200_OK

    assert len(response_json["data"]) == 5
    assert isinstance(response_json["data"], list)

    assert len(response_json["data"][0]["1º pin"]) == 4

    assert str(response_json["data"][0]["1º pin"]).isnumeric()

    assert len(response_json["data"][1]["2º pin"]) == 4
    assert str(response_json["data"][1]["2º pin"]).isnumeric()

    assert len(response_json["data"][2]["3º pin"]) == 4
    assert str(response_json["data"][2]["3º pin"]).isnumeric()    

    assert len(response_json["data"][3]["4º pin"]) == 4
    assert str(response_json["data"][3]["4º pin"]).isnumeric()    
