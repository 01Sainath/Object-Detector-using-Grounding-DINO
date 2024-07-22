from groundingdino.util.inference import load_model, load_image, predict
from fastapi import FastAPI, File, UploadFile

CONFIG_PATH = "groundingdino/config/GroundingDINO_SwinT_OGC.py"

# Checkpoint is the model weight. We need download model weight
CHECK_POINT_PATH = "weights/groundingdino_swint_ogc.pth"
my_model = load_model(CONFIG_PATH, CHECK_POINT_PATH)

IMAGE_DIR = "Uploaded_Images/"

IMAGE_PATH = f"{IMAGE_DIR}paper.jpg"
TEXT_PROMPT = "text . paper"
BOX_THRESHOLD = 0.35
TEXT_THRESHOLD = 0.25

def detect():
    image_source, image = load_image(IMAGE_PATH)
    boxes, accuracy, obj_name = predict(
        model=my_model,
        image=image,
        caption=TEXT_PROMPT,
        box_threshold=BOX_THRESHOLD,
        text_threshold=TEXT_THRESHOLD
    )
    list_boxes = boxes.tolist()
    print(obj_name)
    print(list_boxes)
    return {
        "OBJECTS": obj_name,
        "BOXES": list_boxes
        }

app = FastAPI()

@app.get("/api/testing")
def testing():
    return {
        "MSG": "Server is running..."
    }

@app.post("/api/detect")
async def upload_image(image: UploadFile):

    image.filename = "paper.jpg"
    contents = await image.read()

    # SAVE the image
    saved_image = f"{IMAGE_DIR}{image.filename}"
    with open(saved_image, "wb") as f:
        f.write(contents)

    return detect()

