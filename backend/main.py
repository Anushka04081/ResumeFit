
from section_parser import extract_sections
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pypdf import PdfReader
from io import BytesIO
from parser import parse_resume
from analyzer import calculate_score

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "ResumeFit Backend Running 🚀"
    }


def clean_text(text):
   
    text = text.replace("|", " ")

    lines = []

    for line in text.split("\n"):
        line = " ".join(line.split())

        if line:
            lines.append(line)

    return "\n".join(lines)


@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    contents = await file.read()

    pdf = PdfReader(BytesIO(contents))

    text = ""

    for page in pdf.pages:
        text += page.extract_text() or ""

    text = clean_text(text)
    print("=" * 80)
    print("RAW RESUME TEXT")
    print(text)
    print("=" * 80)

    sections = extract_sections(text)

    print("=" * 100)
    print(sections)
    print("=" * 100)

    resume_data = parse_resume(text)
    analysis = calculate_score(resume_data)

    return {
    "filename": file.filename,
    "message": "Resume analyzed successfully",
    "resume_data": resume_data,
    "analysis": analysis
}