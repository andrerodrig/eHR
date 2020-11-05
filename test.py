from xhtml2pdf import pisa  # import python module

# Define your data
source_html = "<html><body><p>To PDF or not to PDF</p></body></html>"
output_filename = "test.pdf"


# Utility function
def convert_html_to_pdf(source_html, output_filename):
    # open output file for writing (truncated binary)
    with open(output_filename, "w+b") as opened_file:

        # convert HTML to PDF
        pisa_status = pisa.CreatePDF(source_html, dest=opened_file)

    # return False on success and True on errors
    return pisa_status.err


# Main program
if __name__ == "__main__":
    pisa.showLogging()
    convert_html_to_pdf(source_html, output_filename)
