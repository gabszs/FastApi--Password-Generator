from app.schemas.Input_scheme import PasswordBody


def test_input_scheme():
    pb = PasswordBody(
        suffle_string_inject=False,
        char_inject=["s", "b", "_", "2"],
        string_inject=["gabriel23%#@", "dudus1@"],
    )

    assert pb.dict() == {
        "suffle_string_inject": False,
        "char_inject": ["s", "b", "_", "2"],
        "string_inject": ["gabriel23%#@", "dudus1@"],
    }


if __name__ == "__main__":
    test = test_input_scheme()
