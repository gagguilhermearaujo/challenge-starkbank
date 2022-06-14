import random
import time

import starkbank

with open("../private-key.pem", "r") as key:
    private_key_content = key.read()

print(private_key_content)

project = starkbank.Project(
    environment="sandbox", id="6214492773941248", private_key=private_key_content
)
starkbank.user = project

persons = {
    "Dustin Henderson": "314.751.700-41",
    "Steve Harrington": "702.855.160-19",
    "The Mind Flayer": "132.025.100-53",
    "Eleven": "007.075.170-60",
}

interval_time = 3
total_time = 24
n_batches = total_time / interval_time
min_invoices_number = 8
max_invoices_number = 12
min_invoice_value = 300  # in BRL cents
max_invoice_value = 1000  # in BRL cents
for i in range(n_batches):
    invoices_list = []
    n_invoices = random.randint(min_invoices_number, max_invoices_number)
    for j in range(n_invoices):
        invoice_amount = random.randint(min_invoice_value, max_invoice_value)
        invoice_person = random.choice(list(persons))
        invoice_tax_id = persons[invoice_person]
        invoices_list.append(
            starkbank.Invoice(
                amount=invoice_amount,
                name=invoice_person,
                tax_id=invoice_tax_id,
            )
        )
    invoices = starkbank.invoice.create(invoices_list)
    print("Sent invoice batch...")
    for invoice in invoices:
        print(invoice)
    time.sleep(60 * 60 * interval_time)  # batches occur with spacing of interval_time
