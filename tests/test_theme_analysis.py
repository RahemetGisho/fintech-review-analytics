from src.theme_analysis import identify_theme


def test_identify_theme():

    text = "login error and otp problem"

    result = identify_theme(text)

    assert result == "Account Access Issues"