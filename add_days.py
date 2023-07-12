import datetime

def add_days_func(date, delta_days=1):
    """日付と日数を受け取って、日付に日数を加算した日付を返します。

    Args:
        date (str): 日時の始点(yyyy-mm-dd)
        days (int): 日数(defalut: 1)

    Returns:
        date オブジェクト: 受け取った日付に日数を加算した日付
    """
    y, m, d = map(int, date.split('-'))
    date = datetime.date(year=y, month=m, day=d)
    delta_days = datetime.timedelta(days=delta_days)
    return str(date + delta_days)