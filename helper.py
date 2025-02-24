from datetime import date, timedelta


class Helper:
    @staticmethod
    def generate_date_order_next_day_1_set():
        date_order = str(date.today() + timedelta(days=1))
        return date_order

    @staticmethod
    def generate_date_order_in_2_weeks_2_set():
        date_order = str(date.today() + timedelta(weeks=1))
        return date_order
