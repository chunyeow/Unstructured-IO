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
