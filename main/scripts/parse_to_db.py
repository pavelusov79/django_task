import os
import datetime

from main.models import Logs

def run():
    with open(os.path.join(os.path.dirname(__file__), 'access.log'), 'r') as f:
        for line in f:
            l = Logs.objects.filter(datetime_field=datetime.datetime.strptime(line.split()[3:5][0].replace('[', ''), '%d/%b/%Y:%H:%M:%S').strftime('%Y-%m-%d %H:%M'))
            if not l:
                obj = Logs(
                    ip_field=line.split()[0], 
                    datetime_field=datetime.datetime.strptime(line.split()[3:5][0].replace('[', ''), '%d/%b/%Y:%H:%M:%S').strftime('%Y-%m-%d %H:%M'),
                    status=int(line.split("\"")[2].split()[0]))
                obj.save()
           