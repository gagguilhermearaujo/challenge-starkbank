# challenge-starkbank

This is the response of Guilherme Gonçalves to the challenge of Starkbank.

The code is separate in two folders:
-webhook_server -> contains the webhook server listening to a post request from Starkbank webhook and business logic
-invoice_issuer -> contains the invoice issuer

The webserver is hosted at AWS Lambda under the url https://qkjyjevmvw3lcjlzsykn5yidui0attis.lambda-url.us-east-1.on.aws/ so there is no need to execute it to listen to the incoming request, it's already done.

The invoice issuer is not hosted, it's a script to execute on-premise, but it won't work if tou try to execute because it would be missing my private key. If it's necessary to execute it, please ask for the private key and put it on the root folder name as "private-key.pem".

This repo contains a CI/CD script base on Github Actions that automatically updates the lambda function on pushing to main branch.
