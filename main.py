from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from generate import generate
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
app = FastAPI()

# Add CORS middleware if you're testing locally
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the shape of your form data
class ProjectFormData(BaseModel):
    projectName: str
    temp_url: str
    username: str
    password: str
    siteAddress: str
    sitePhone: str
    serviceArea: str
    hours: str
    formInfo: str
    websiteUrl: Optional[str] = ""
    gmb: Optional[str] = ""
    fb: Optional[str] = ""
    county: Optional[str] = ""
    other: Optional[str] = ""
    colors: str
    logo: str
    images: Optional[str] = ""
    specials: Optional[str] = ""
    exclude: Optional[str] = ""
    include: Optional[str] = ""
    functionality: Optional[List[str]] = []
    functionalityOther: Optional[str] = ""
    inspo: Optional[List[dict]] = []  # [{"url": "...", "notes": "..."}]
    postTemplate: Optional[str] = ""

@app.get("/")
def read_root():
    # return {"Hello": "World"}
    return FileResponse("projectForm.html")


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.get("/template")
def get_template():
    app.mount("/ESS", StaticFiles(directory="ESS"), name="ESS")
    return FileResponse("projectSheet.html")


@app.post("/generate")
async def formGen(formData: ProjectFormData):
    """
    Receives form data and generates a PDF
    """
    try:
        # Convert Pydantic model to dict
        data_dict = formData.dict()

        # Generate PDF
        pdf_filename = generate(data_dict)

        # Return the PDF file
        return FileResponse(
            pdf_filename,
            media_type='application/pdf',
            filename=f"ProjectSheet_{formData.projectName}.pdf",
        )
    except Exception as e:
        return {"error": str(e)}, 500
    data = "test"
    generate(data)
