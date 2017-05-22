import hotelapi.manage as mgr

class TestSettings:
    def test_app(self):
        assert hasattr(mgr, "app")



    def test_manager(self):
        assert hasattr(mgr, "manager")