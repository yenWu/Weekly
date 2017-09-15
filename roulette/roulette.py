class Roulette():
    def __init__(self, policy, cands = (None)):
        self.__policy = None
        self.__candidates = None
        self.setUp(policy, cands)

    @property
    def setUp(self, plcy = None, cands = (None)):
        self.__policy = plcy if plcy != None else self.__policy
        self.__candidates = cands if cands != None else self.__candidates
        self.__ptr = None

    @property
    def lottery(self):
        self.__ptr = self.__policy(self.__ptr, self.__candidates)
        return self.__ptr
