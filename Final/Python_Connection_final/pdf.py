from pyhtml2pdf import converter
from send_mail import *
def convert(url,name,s_email) :
    converter.convert(url,name+'.pdf')
    print("billing...")
    billing(s_email,"Please Check the bill and Pay Cashless using UPI",name+'.pdf')