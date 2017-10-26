class MyMRJob():
    def mapper(self, key, value):
        raise NotImplementedError

    def reducer(self, key, values):
        raise NotImplementedError

