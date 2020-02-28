import PyPDF2
import sqlite3
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobproject.settings')

import django
django.setup()

from jobapp.models import Review

# Job IDs Starting From 1
jid = int(input("Enter The Job Description ID : "))

def find_desc():
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    query = '''select job_description from jobapp_review where id = ?'''
    cur.execute(query, (jid,))
    r = cur.fetchall()
    print(r)
    rfile = r[0][0]
    print(rfile)
    conn.commit()
    cur.close()
    conn.close()
    return 'jobapp/media/' + rfile

def extract_pdf(rfile):
    pdfFileObj = open(rfile, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    pdfFileObj.close()
    return str(text)

def update_job_text(text):
    s = Review.objects.filter(id=jid)
    r = s.update(job_text = text)
    r.save()

rfile = find_desc()
print(rfile)
text = extract_pdf(rfile)
print(text)
update_job_text(text)
