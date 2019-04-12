class Tariff:
    def __init__(self,
                 name,
                 *,  # включаем keyword для значений ниже - ключ+значение в обязательном порядке
                 price=0,  # 0 - без абонентской платы, None - не указано
                 price_period='month',
                 gb=0,  # -1 - безлимит
                 minutes=0,
                 sms=0,
                 hit=False,
                 gb_unlim=None,
                 minutes_unlim_tele2=True,  # None - не указано
                 archived=False):
        self.name = name
        self.price = price
        self.price_period = price_period
        self.gb = gb
        self.minutes = minutes
        self.sms = sms
        self.hit = hit
        self.gb_unlim = gb_unlim
        self.minutes_unlim_tele2 = minutes_unlim_tele2
        self.archived = archived


class TariffManager:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def actual(self):
        return filter(lambda x: not x.archived, self.items)

    def archived(self):
        return list(filter(lambda o: o.archived, self.items))  # передаем имя функции! вызывать будем сам filter
