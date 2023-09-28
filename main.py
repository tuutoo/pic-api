from mangum import Mangum
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

from PIL import Image
import numpy as np
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello, World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/invert/")
async def invert_image(file: UploadFile = File(...)):
    # 使用 PIL 打开图片
    image = Image.open(io.BytesIO(await file.read()))

    # 将图片转换为 NumPy 数组
    image_array = np.array(image)

    # 执行反色操作
    inverted_image_array = 255 - image_array

    # 将 NumPy 数组转回为 PIL 图片
    inverted_image = Image.fromarray(np.uint8(inverted_image_array))

    # 保存到一个字节流中，以便可以直接返回
    byte_io = io.BytesIO()
    inverted_image.save(byte_io, 'JPEG')
    byte_io.seek(0)

    return StreamingResponse(byte_io, media_type="image/jpeg", headers={"Content-Disposition": "attachment; filename=inverted_image.jpg"})

handler = Mangum(app)