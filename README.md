# Pygmy URL Shortener

Pygmy is an simple AWS serverless implementation of a url shortener. It deploys an API and creates a custom domain name based on a domain in Route 53. It creates an ACM certificate, which requires a manual DNS validation in the stack creation. The output is a Cloudfront endpoint, which can be added as a DNS record in Route 53.

To use the endpoint takes the form:

POST {"url": URL_TO_SHORTEN}

URL_TO_SHORTEN is a string.
It then returns a url of the form: https://BASE_URL/URL_ID, where URL_ID is an automatically generated slug.

In the stack the option of RootUrl is required, this is used as a redirect from a GET request with no slug to a potential frontend endpoint to create new apis.

Limitations:

Due to ACM and API Gateway distributions this must be deployed in the us-east-1 region.
There are are no restrictions on creating or sharing this API, so avoid using it for sensitive data.

