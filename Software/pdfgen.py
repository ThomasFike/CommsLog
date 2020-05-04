from fpdf import FPDF
from tinydb import TinyDB, Query
import time

db = TinyDB('Database.json')
space = '                                             '
field8 = '8. Prepared by:    Name:' + space + 'Position/Title:' + space + 'Signature:\n'
class PDF(FPDF):
    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-0.75)
        # Arial italic 8
        self.set_font('Arial', size=10)
        # Page number
        self.multi_cell(0, pdf.font_size*1.5, field8 + 'ICS 309, Page ' + str(self.page_no() ) + space + space[0:13] +'Date/Time:', border=1, align='L', fill=False)

pdf = PDF(orientation='P', unit='in', format='letter')
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font("Arial", size=12)

def Header(spacing = 1):
    col_width = pdf.w / 4.5
    row_height = pdf.font_size

    #Row 0
    pdf.multi_cell(pdf.w/6.5, row_height * spacing * 1.5,
                txt='COMM LOG\nICS-309', border=1, align='C')
    pdf.ln(-row_height * spacing * 3)
    pdf.set_x(pdf.w/6.5 + pdf.get_x())
    pdf.multi_cell(pdf.w/3.5, row_height * spacing * 1.5,
                txt='1. Incident Name\n Luke Flyover Observer Net',
                border=1, align='L')
    pdf.ln(-row_height * spacing * 3)
    pdf.set_x(pdf.w/6.5 + pdf.get_x() + pdf.w/ 3.5)
    pdf.multi_cell(0, row_height * spacing * 1.5,
                txt='2. Operational Period\nFrom: 2020-05-01 15:00  To: 2020-05-01 16:00',
                border=1, align='L')
    
    #Row 1
    pdf.multi_cell(pdf.w/2.275, row_height * spacing * 1.5,
                txt='3. Net Name\nAEN-MAR',
                border=1, align='L')
    pdf.ln(-row_height * spacing * 3)
    pdf.set_x(pdf.w/2.275 + pdf.get_x())
    pdf.multi_cell(0, row_height * spacing * 1.5,
                txt='4. RADO (Name, Callsign)\nThomas Fike, KG7FXT',
                border=1, align='L')


def DataTable(spacing=1):
    data = [['Time', 'Tx', 'Rx', 'Message']]
    for item in db.all():
        data.append(list(item.values()))
    col_width = pdf.w / 6
    row_height = pdf.font_size
    for row in data[1:]:
        itime = time.localtime(int(row[0]))
        row[0] = str(itime.tm_hour) + ':' + str(itime.tm_min) + ':' + str(itime.tm_sec)
    for row in data:
        for item in row[0:-1]:
            pdf.cell(col_width, row_height*spacing,
                     txt=item, border=1)
        pdf.cell(0,row_height*spacing, txt=row[-1], border=1)
        pdf.ln(row_height*spacing)


def simple_table(spacing=1):
    data = [['First Name', 'Last Name', 'email', 'zip'],
            ['Mike', 'Driscoll', 'mike@somewhere.com', '55555'],
            ['John', 'Doe', 'jdoe@doe.com', '12345'],
            ['Nina', 'Ma', 'inane@where.com', '54321']
            ]

    col_width = pdf.w / 4.5
    row_height = pdf.font_size
    for row in data:
        for item in row:
            pdf.cell(col_width, row_height*spacing,
                     txt=item, border=1)
        pdf.ln(row_height*spacing)

Header()
pdf.ln(pdf.font_size)
DataTable(1.5)
pdf.output("test.pdf", 'F')
