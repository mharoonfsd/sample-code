# -*- coding: utf-8 -*-
import csv

from cStringIO import StringIO
from django.core.files.uploadedfile import SimpleUploadedFile

file_name = 'temp.csv'
data = [['first_name', 'last_name',
		 'email', 'title',
         'department', 'is_staff'],
        ['Henry', 'Smith',
         'henry@lighthousetraders.com', 'Software Engineer',
         'Engineering', 'FALSE']]

buff = StringIO()
w = csv.writer(buff)

w.writerows(data)
buff.seek(0)
content = b'' + buff.read().encode('ascii')
file_data = SimpleUploadedFile(file_name, content, content_type="text/csv")

r = csv.reader(file_data)
for row in r:
    print(row)

buff.seek(0)

m = file_data.read().decode("utf-8")
print(m)
