#
# Unstructured provides OCR-based and Transformer-based models to detect elements in the documents. 
# The hi_res_model_name parameter supports the yolox - yolox_l0.05.onnx based on the current env
# Reference: https://docs.unstructured.io/examplecode/codesamples/apioss/table-extraction-from-pdf
#
from unstructured.partition.pdf import partition_pdf

fname = "data/in/ME28-2016.pdf"
foname = "data/out/ME28-2016.json"

elements = partition_pdf(filename=fname,
                         infer_table_structure=True,
                         strategy='hi_res',
           )

tables = [el for el in elements if el.category == "Table"]

with open(foname, "w") as file:
   for table in tables:
      #table = table.text
      table = table.metadata.text_as_html
      file.write(table)
