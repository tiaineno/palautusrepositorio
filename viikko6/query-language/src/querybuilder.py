from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

class QueryBuilder:
    def __init__(self):
        self._queries = []

    def build(self):
        if self._queries == []:
            return All()
        
        return And(self._queries)
    
    def one_of(self, *matchers):
        for i in matchers:
            print(i)
        self._queries.append(Or(*matchers))
        return self
    
    def plays_in(self, team):
        self._queries.append(PlaysIn(team))
        return self

    def has_at_least(self, value, attr):
        self._queries.append(HasAtLeast(value, attr))
        return self

    def has_fewer_than(self, value, attr):
        self._queries.append(HasFewerThan(value, attr))
        return self