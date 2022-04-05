#7. Convert string into a datetime object
#Input : date_string = "Mar 09 2022 11:20AM"
# output: 2022-03-09 11:20:00
from datetime import datetime
date_time_str = 'Mar 09 2022 11:20AM'
datetime_object = datetime.strptime(date_time_str, '%b %d %Y %I:%M%p')
print(datetime_object)

#8. Calculate the date 4 months from the current date
from datetime import date
from dateutil.relativedelta import relativedelta
four_months = date.today() + relativedelta(months=+4)
print(four_months)

