import os

import starkbank
import uvicorn
from fastapi import FastAPI
from mangum import Mangum

from models import WebhookCallback, WebhookResponse

app = FastAPI()

private_key_content = os.getenv("PRIVATE_KEY")
project = starkbank.Project(
    environment="sandbox", id="6214492773941248", private_key=private_key_content
)
starkbank.user = project


@app.get("/")
def root():
    return {
        "message": "Welcome to the Starkbank Challenge Webhook made by Guilherme Gonçalves. See the /docs to see models and endpoints",
        "docs_endpoint": "/docs",
    }


@app.post("/invoices_webhook", response_model=WebhookResponse)
def invoices_webhook(weebhook_callback: WebhookCallback):
    invoice_type = weebhook_callback.event.log.type
    if invoice_type == "credited":
        invoice_amount = weebhook_callback.event.log.invoice.amount
        invoice_fee = weebhook_callback.event.log.invoice.fee
        transfer_amount = invoice_amount - invoice_fee
        transfer_tags = weebhook_callback.event.log.invoice.tags
        transfer_dict = {
            "amount": transfer_amount,
            "tax_id": "20.018.183/0001-80",
            "name": "Stark Bank S.A.",
            "bank_code": "20018183",
            "branch_code": "0001",
            "account_number": "6341320293482496",
            "account_type": "payment",
            "tags": transfer_tags,
        }
        transfer_list = [starkbank.Transfer(**transfer_dict)]
        transfer = starkbank.transfer.create(transfer_list)
        return {
            "transfer_created": True,
            "invoice_type": invoice_type,
        }
    else:
        return {
            "transfer_created": False,
            "invoice_type": invoice_type,
        }


running_environment = os.getenv("PYTHON_ENV")

if running_environment == "prod":
    print("Production mode started")
    lambda_handler = Mangum(app, lifespan="off")

if running_environment == "dev":
    print("Development mode started")
    if __name__ == "__main__":
        uvicorn.run("lambda_function:app", host="0.0.0.0", port=8080, reload=True)
