from fastapi import status

# from test.schema.test_input_schema import PasswordBody


def check_any_alnum(string: str):
    return any(char.isnumeric() for char in string) and any(char.isalpha() for char in string)


def test_complex_password_route(client):
    strings_list = ["Gab", "tao", "2018"]
    char_list = ["a", "b", "0"]

    body = {
        "suffle_string_inject": False,
        "char_inject": char_list,
        "string_inject": strings_list,
    }

    response = client.post("/complex_password/10?quantity=3&ponctuation=False", json=body)
    response_json = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(response_json["data"]) == 3

    # 10 + sum([sum(len(string) for string in strings_list), sum(len(char) for char in char_list)])
    assert len(response_json["data"][0]["1º pin"]) == 10 + sum(
        [
            sum(len(string) for string in strings_list),
            sum(len(char) for char in char_list),
        ]
    )
    assert str(response_json["data"][0]["1º pin"]).isascii()
    assert check_any_alnum(response_json["data"][0]["1º pin"])
    assert all(text in response_json["data"][0]["1º pin"] for text in strings_list)
    assert all(text in response_json["data"][0]["1º pin"] for text in char_list)

    assert len(response_json["data"][1]["2º pin"]) == 10 + sum(
        [
            sum(len(string) for string in strings_list),
            sum(len(char) for char in char_list),
        ]
    )
    assert str(response_json["data"][1]["2º pin"]).isascii()
    assert check_any_alnum(response_json["data"][1]["2º pin"])
    assert all(text in response_json["data"][1]["2º pin"] for text in strings_list)
    assert all(text in response_json["data"][1]["2º pin"] for text in char_list)

    assert len(response_json["data"][2]["3º pin"]) == 10 + sum(
        [
            sum(len(string) for string in strings_list),
            sum(len(char) for char in char_list),
        ]
    )
    assert str(response_json["data"][2]["3º pin"]).isascii()
    assert check_any_alnum(response_json["data"][2]["3º pin"])
    assert all(text in response_json["data"][2]["3º pin"] for text in strings_list)
    assert all(text in response_json["data"][2]["3º pin"] for text in char_list)
