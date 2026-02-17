from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS
import os
# Load template from folder
env =  Environment(loader=FileSystemLoader('.'))
template = env.get_template('projectSheet.html')

def generate(formData):
    # Variables to inject
    # data = {
    #     "projectName": "Test Project",
    #     "temp_url":"test.esstemp.net",
    #     "username":"web",
    #     "password":"9$ja%e9",
    #     "siteAddress":"123 Big WalkWay",
    #     "sitePhone":"1234567890",
    #     "serviceArea":"Clearwater",
    #     "hours":"8 AM - 5 PM M-F",
    #     "formInfo":"Name,phone,Confirm Phone, Email, Message",
    #     "websiteUrl":"test.com",
    #     "gmb":"none",
    #     "fb":"none",
    #     "county":"none",
    #     "other":"none",
    #     "colors":"#FFFFF, White",
    #     "logo":"none",
    #     "images":"pexels or unsplash",
    #     "specials": "none",
    #     "exclude": "",
    #     "include": "",
    #     "functionality": "",
    #     "inspo":"https://expansionsupportservices.com",
    #     "postTemplate":"",
    # }
    # Use the actual form data instead of hardcoded values
    data = {
        "projectName": formData.get("projectName", "Untitled Project"),
        "temp_url": formData.get("temp_url", ""),
        "username": formData.get("username", ""),
        "password": formData.get("password", ""),
        "siteAddress": formData.get("siteAddress", ""),
        "sitePhone": formData.get("sitePhone", ""),
        "serviceArea": formData.get("serviceArea", ""),
        "hours": formData.get("hours", ""),
        "formInfo": formData.get("formInfo", ""),
        "websiteUrl": formData.get("websiteUrl", ""),
        "gmb": formData.get("gmb", ""),
        "fb": formData.get("fb", ""),
        "county": formData.get("county", ""),
        "other": formData.get("other", ""),
        "colors": formData.get("colors", ""),
        "logo": formData.get("logo", ""),
        "images": formData.get("images", ""),
        "specials": formData.get("specials", ""),
        "exclude": formData.get("exclude", ""),
        "include": formData.get("include", ""),
        "functionality": ", ".join(formData.get("functionality", [])),
        "functionalityOther": formData.get("functionalityOther", ""),
        "inspo": formData.get("inspo", []),
        "postTemplate": formData.get("postTemplate", ""),
    }

    # Render HTML with variables
    html_out = template.render(data)

    # Create Directory if it doesn't exist
    os.makedirs("output", exist_ok=True)

    # Generate filename
    safe_project_name = "".join(c for c in data["projectName"] if c.isalnum() or c in (' ', '-', '_')).strip()
    safe_project_name = safe_project_name.replace(' ', '_')
    pdf_filename = f"output/projectSheet-{safe_project_name}.pdf"

    # Generate PDF
    HTML(string=html_out, base_url='.').write_pdf(
        pdf_filename,
        stylesheets=[CSS("ESS/css/projects.css")]
    )

    return pdf_filename

# HTML("projectSheet.html").write_pdf(
#     "output/projectSheet.pdf",
#     stylesheets=[CSS("ESS/css/projects.css")]
# )

# Read the HTML to see what we're working with
# with open("projectSheet.html", "r") as f:
#     html_content = f.read()
#     print(f"HTML length: {len(html_content)} characters")
#
# # Generate PDF with more info
# html = HTML(string=html_content)
# css = CSS("ESS/css/projects.css")
#
# document = html.render(stylesheets=[css])
# print(f"Number of pages rendered: {len(document.pages)}")
#
# document.write_pdf("output/projectSheet.pdf")
# print("PDF written")