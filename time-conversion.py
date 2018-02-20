#!/bin/python3

import sys
from datetime import datetime
# from dateutil import parser


def time_conversion(m_time):

    dt_str = '01/01/2018 ' + m_time
    dt_obj = datetime.strptime(dt_str, '%d/%m/%Y %I:%M:%S%p')
    return dt_obj.strftime('%H:%M:%S')

s = input().strip()
result = time_conversion(s)
print(result)
