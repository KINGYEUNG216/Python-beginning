"""
Date Scheduler Function

Objective:
Write a function named 'date_passed' to determine the relationship between two dates.

Function Parameters:
1. todays_date (string): The current date in the format 'day Month'.
2. scheduled_date (string): The scheduled date to compare, in the same format.

Instructions:
- The function should compare todays_date and scheduled_date and print whether the scheduled date has passed, is yet to pass, or is today.
- Assume the dates are in the same year.
- The dates are in a format like '26th March'. Consider how to convert these for comparison.
#要把表格的数字提取出来，新字符串 = 原始字符串.replace(旧子字符串, 新子字符串)
- https://www.w3schools.com/python/python_datetime.asp

Example Test Cases:
1. date_passed('26th March', '25th March') should indicate that the scheduled date has passed.
2. date_passed('26th March', '26th March') should indicate that the scheduled date is today.
3. date_passed('26th March', '27th March') should indicate that the scheduled date is yet to pass.
"""

from datetime import datetime
def date_passed(todays_date, scheduled_date):

    todays_date = datetime.strptime(todays_date.replace("th","").replace("st","").replace("nd","").replace("rd",""),"%d %B")
    scheduled_date = datetime.strptime(scheduled_date.replace("th","").replace("st","").replace("nd","").replace("rd",""),"%d %B")
#strptime 是 datetime 模块中方法，用于将字符串解析为日期时间对象  移除日期后缀                                                 定义清理后的数据格式“day of month” “month name”
#补充一下：strftime 用于将日期时间对象格式化为字符串


    #日期时间对象可以直接比大小
    if todays_date == scheduled_date:
        print("Scheduled date is today")
    elif todays_date > scheduled_date:
        print("Scheduled date has passed")
    else:
        print("Scheduled date is yet to pass")


    # Your code goes here
    # Implement the logic to compare the dates and print the appropriate message
    pass  # Delete this after implementing some code inside this function


# Test cases
date_passed("26th March", "25th March")  # Expected: Scheduled date has passed
date_passed("26th March", "26th March")  # Expected: Scheduled date is today
date_passed("26th March", "27th March")  # Expected: Scheduled date is yet to pass
