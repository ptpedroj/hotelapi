import hotelapi.settings as s

class TestSettings:
    def test_secret_key(self):
        assert hasattr(s, "SECRET_KEY")


    def test_debug(self):
        assert hasattr(s, "DEBUG")