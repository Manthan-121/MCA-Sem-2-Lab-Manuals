import csv
def generate_html_table(file_name):
    html_output = "<html>\n<head>\n<title>CSV to HTML Table</title>\n</head>\n<body>\n"
    html_output += "<table border='1'>\n"
    with open(file_name, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            html_output += "<tr>\n"
            for cell in row:
                html_output += "<td>{}</td>\n".format(cell)
            html_output += "</tr>\n"
    
    html_output += "</table>\n</body>\n</html>"
    return html_output
# Read CSV file and generate HTML table
html_content = generate_html_table("empData.csv")
# Write HTML content to a file
with open("Output.html", "w") as html_file:
    html_file.write(html_content)
print("HTML output generated successfully in output.html file.")
