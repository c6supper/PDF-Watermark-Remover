from pypdf import PdfReader, PdfWriter

def show_tree(outlines, indent=0):
    for item in outlines:
        if isinstance(item, list):
            show_tree(item, indent+4)
        else:           
            print(f'{" "*indent}{item.title}')

def removeWatermark(input_fname: str, output_fname: str):

    with open(input_fname, "rb") as input_file:

        reader = PdfReader(input_file)
        writer = PdfWriter()

        writer.clone_document_from_reader(reader)
        
        for page in writer.pages:
            del page["/Contents"][-1]
        

    with open(output_fname, "wb") as output_file:
        writer.write(output_file)

if __name__ == "__main__":

    import sys

    if len(sys.argv) == 2:
        removeWatermark(sys.argv[1], sys.argv[1])
    elif len(sys.argv) == 3:
        removeWatermark(sys.argv[1], sys.argv[2])
    else:
        raise RuntimeError("Wrong number of arguments!")

