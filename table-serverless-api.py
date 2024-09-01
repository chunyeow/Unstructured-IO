# Reference: https://docs.unstructured.io/api-reference/api-services/sdk-python

import os, json

import unstructured_client
from unstructured_client.models import operations, shared

client = unstructured_client.UnstructuredClient(
    api_key_auth=os.getenv("UNSTRUCTURED_API_KEY"),
    server_url=os.getenv("UNSTRUCTURED_API_URL"),
)

filename = "data/in/ME28-2016.pdf"
with open(filename, "rb") as f:
    data = f.read()

req = operations.PartitionRequest(
    partition_parameters=shared.PartitionParameters(
        files=shared.Files(
            content=data,
            file_name=filename,
        ),
        strategy=shared.Strategy.HI_RES,
        languages=['eng'],
        split_pdf_page=False,            # If True, splits the PDF file into smaller chunks of pages.
        split_pdf_allow_failed=True,    # If True, the partitioning continues even if some pages fail.
        split_pdf_concurrency_level=15  # Set the number of concurrent request to the maximum value: 15.
    ),
)

try:
    res = client.general.partition(request=req)
    element_dicts = [element for element in res.elements]
    json_elements = json.dumps(element_dicts, indent=2)
    tables = [el for el in json.loads(json_elements) if el['type'] == "Table"]

    # Write the processed data to a local file.
    with open("data/out/ME28-2016-table.json", "w") as file:
        for table in tables:
            table = table['metadata']['text_as_html']
            file.write(table)
except Exception as e:
    print(e)
