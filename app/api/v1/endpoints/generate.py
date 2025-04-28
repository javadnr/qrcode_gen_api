from fastapi import APIRouter, Query
from fastapi.responses import StreamingResponse
import qrcode
import io

router = APIRouter()

@router.get("/generate")
def generate_qr(data: str = Query(..., description="Text or URL to encode into QR code")):
    qr = qrcode.make(data)
    img_io = io.BytesIO()
    qr.save(img_io, 'PNG')
    img_io.seek(0)
    return StreamingResponse(img_io, media_type="image/png")
