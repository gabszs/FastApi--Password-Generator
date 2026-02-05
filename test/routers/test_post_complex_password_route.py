from fastapi import status


def check_any_alnum(string: str):
    return any(char.isnumeric() for char in string) and any(char.isalpha() for char in string)


def test_complex_password_route(client):
    strings_list = ["Gab", "tao", "2018"]
    char_list = ["a", "b", "0"]

    body = {
        "additional_length": 10,
        "quantity": 3,
        "punctuation": False,
        "shuffle_string_inject": False,
        "char_inject": char_list,
        "string_inject": strings_list,
    }

    response = client.post("/v1/complex_password", json=body)
    response_json = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(response_json["data"]) == 3

    expected_length = 10 + sum(len(s) for s in strings_list) + sum(len(c) for c in char_list)

    for password in response_json["data"]:
        assert isinstance(password, str)
        assert len(password) == expected_length
        assert password.isascii()
        assert check_any_alnum(password)
        assert all(text in password for text in strings_list)
        assert all(text in password for text in char_list)
