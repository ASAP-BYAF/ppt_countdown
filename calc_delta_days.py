import datetime

def calc_delta_days_func(date_st, date_ed):
    """二つの日付を受け取り、日数の差を返します。

    Args:
        date_st (str): 日時の始点(yyyy-mm-dd)
        date_st (str): 日時の終点(yyyy-mm-dd)

    Returns:
        int: 日数の差。
    """
    y_st, m_st, d_st = map(int, date_st.split('-'))
    y_ed, m_ed, d_ed = map(int, date_ed.split('-'))
    date_st = datetime.date(year=y_st, month=m_st, day=d_st)
    date_ed = datetime.date(year=y_ed, month=m_ed, day=d_ed)
    delta_days = date_ed - date_st
    return int(delta_days.days)