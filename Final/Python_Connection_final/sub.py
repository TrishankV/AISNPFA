from jinja2 import Environment, FileSystemLoader
import random
from pdf import *

def generate_random_word():
    # Create a list of all lowercase letters
    letters = list('abcdefghijklmnopqrstuvwxyz')

    # Generate a random word of length 5
    word = ''.join(random.choice(letters) for _ in range(5))
    print(word)

    return word

def generate_html(name,cost,p,d,email):
    word = generate_random_word()

    # Load the template
    template_loader = FileSystemLoader('templates')
    template_env = Environment(loader=template_loader)
    template = template_env.get_template('invoice.html')

    # Prepare the invoice data
    invoice_number = 'INV-2023-001'
    invoice_date = '2023-12-08'
    due_date = '2023-11-30'
    pick = p
    drop = d
    name_user = name
    invoice_items = [
        {'description': 'Operational Cost', 'amount': cost},
        {'description': 'CGST (9%)', 'amount': 90.00},
        {'description': 'SGST (9%)', 'amount': 90.00},
    ]
    invoice_total = sum(item['amount'] for item in invoice_items)

    # Render the template with the data
    rendered_html = template.render(
        name_user = name_user,
        pick = pick,
        drop = drop,
        invoice_number=invoice_number,
        invoice_date=invoice_date,
        due_date=due_date,
        invoice_items=invoice_items,
        invoice_total=invoice_total,
    )

    # Save the rendered HTML to a file
    with open(word+'.html', 'w') as f:
        f.write(rendered_html)

    convert('http://127.0.0.1:5500/'+word+'.html',name,email)

if __name__=="__main__":
    generate_html("Vedant",100,'A','G',"ai.58.vedant.ranade@gmail.com")
