from hotelapi.common.singleton import Singleton

class TestSingleton(object):
    def test_create_singleton(self):
        class SingleSub(metaclass = Singleton):
            def __init__(self, tag):
                self.tag = tag

        obj1 = SingleSub(False)
        obj2 = SingleSub(True)

        assert obj1 is obj2