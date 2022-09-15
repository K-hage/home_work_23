class Query:
    """ Класс запроса """

    def __init__(self, path):
        self.path = path
        self._command = {
            'filter': self._filter,
            'sort': self._sort,
            'map': self._map,
            'unique': self._unique,
            'limit': self._limit
        }

    def prepared_data(self):
        """ Подготовка данных из файла """
        with open(self.path) as f:
            return list(map(lambda x: x.strip(), f))

    def get_query(self, params):
        """ Возвращает данные по параметрам из запроса """

        data = self.prepared_data()
        for param in params:
            data = self._command[param['cmd']](param=param['value'], data=data)
        return data

    @staticmethod
    def _filter(param, data):
        return list(filter(lambda v: param in v, data))

    @staticmethod
    def _map(param, data):
        column_number = int(param)

        return list(map(lambda v: v.split()[column_number], data))

    @staticmethod
    def _unique(data, *args, **kwargs):
        return list(set(data))

    @staticmethod
    def _sort(param, data):
        reverse = False if param == 'asc' else True
        return sorted(data, reverse=reverse)

    @staticmethod
    def _limit(param, data):
        limit = int(param)
        return list(data)[:limit]
