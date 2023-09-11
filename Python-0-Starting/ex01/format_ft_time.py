from datetime import datetime
from datetime import date

date_ref = date(1970, 1, 1)
now = datetime.now().timestamp()

print(f'Seconds since {date_ref:%B %-d, %Y}: {now:,.4f} or {now:.2e} in scientific notation')
print(date.today().strftime('%b %d %Y'))
