from lib.Facebook import get_data
from lib import calc_afinn
from lib import date_range


def main():

    dates = date_range.DateRange()
    run_fb = get_data.FaceBook(dates.start_date, dates.end_date)
    calc_afinn.YourSentiment(run_fb.aggr_messages)

if __name__ == '__main__':
    main()
