import xml.etree.cElementTree as Et
import datetime

'''
:parameter : depart days - integer
parameter : return days - integer
'''


def update_departure_return(depart_days, rtn_days):
    tree = Et.parse('test_payload1.xml')
    root = tree.getroot()

    for element in root.findall('REQUEST'):
        tp = element.find('TP')
        tp.find('DEPART').text = add_days(tp.find('DEPART').text, depart_days)
        tp.find('RETURN').text = add_days(tp.find('RETURN').text, rtn_days)

    tree.write('updated_test_payload.xml')


'''
this method converts a string to date format and add days
parameter = string eg:20191925, days eg:5 
returns a string for xml
'''


def add_days(str_dt, days):
    date = datetime.datetime.strptime(str_dt, '%Y%m%d')

    # convert to a date format to add days
    t_delta = datetime.timedelta(days=int(days))
    new_date = date + t_delta
    updated_date = datetime.datetime.strftime(new_date, '%Y%m%d')

    return updated_date


# test the method
update_departure_return(2, 2)
