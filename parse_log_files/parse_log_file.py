import csv
from datetime import datetime
from pytz import timezone
import pytz

'''
 Create a python script that parses jmeter log files in CSV format,
and in the case if there are any non-successful endpoint responses recorded in the log,
prints out the label, response code, response message, failure message,
and the time of non-200 response in human-readable format in PST timezone
(e.g. 2021-02-09 06:02:55 PST).

'''


def convert_to_PST_date(t_stamp):
    date_format = '%Y-%m-%d %H:%M:%S %Z'
    date = datetime.fromtimestamp(t_stamp, tz=pytz.utc)
    date = date.astimezone(timezone('US/Pacific'))
    return date.strftime(date_format)


'''
:parameter : input file, out file

'''


def updated_logs(file_name, writefile_name):
    with open(file_name, 'r') as file:
        csv_reader = csv.DictReader(file)
        with open(writefile_name, 'w') as new_file:
            fieldnames = ['timeStamp', 'label', 'responseCode', 'responseMessage', 'failureMessage']
            csv_writer = csv.DictWriter(new_file, fieldnames, extrasaction='ignore')
            csv_writer.writeheader()
            next(csv_reader)
            for line in csv_reader:
                if line['responseCode'] != '200':
                    dt = convert_to_PST_date(int(line['timeStamp'][:10]))
                    line['timeStamp'] = dt
                    csv_writer.writerow(line)


# test the function
updated_logs('Jmeter_log1.jtl', 'updated_Jmeter_log1.jtl')
updated_logs('Jmeter_log2.jtl', 'updated_Jmeter_log2.jtl')
