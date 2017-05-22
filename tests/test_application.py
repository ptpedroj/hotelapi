import hotelapi.application as app

class TestApplication:
    def test_create_app(self):
        assert hasattr(app, "create_app")
        assert app.create_app() is not None