from app.schemas.input_schemas import ComplexPasswordBody


def test_input_schema():
    pb = ComplexPasswordBody(
        additional_length=10,
        shuffle_string_inject=False,
        char_inject=["s", "b", "_", "2"],
        string_inject=["gabriel23%#@", "dudus1@"],
    )

    data = pb.model_dump()
    assert data["shuffle_string_inject"] is False
    assert data["char_inject"] == ["s", "b", "_", "2"]
    assert data["string_inject"] == ["gabriel23%#@", "dudus1@"]
    assert data["additional_length"] == 10


def test_input_schema_defaults():
    pb = ComplexPasswordBody(additional_length=5)

    data = pb.model_dump()
    assert data["quantity"] == 1
    assert data["punctuation"] is False
    assert data["shuffle_string_inject"] is False
    assert data["char_inject"] == []
    assert data["string_inject"] == []
