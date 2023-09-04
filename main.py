import csv


with open('contact_data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

import csv

with open('contact_data.csv', mode='a') as file:
    employee_writer = csv.writer(file)

    employee_writer.writerow(['7','John Smith','jhonsmith@nsw.gov.au','male','07-09-1997','1 Nsk','7364829837']),
    employee_writer.writerow(['8','Tony Smith','tonysmith@nsw.gov.au','male','15-07-1999','1 Nsk','7348298380']),
    employee_writer.writerow(['9','Rogan Smith','rogansth@nsw.gov.au','male','18-08-1993','1 Nsk','7648298479']),
    employee_writer.writerow(['10','Leo Smith','leosmith@nsw.gov.au','male','17-05-1987','1 Nsk','73648292379'])

    file.close()





