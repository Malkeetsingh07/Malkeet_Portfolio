import qrcode
from PIL import Image, ImageDraw, ImageFont

# GitHub Repository URL
url = "https://github.com/Malkeetsingh07/Retail-Sales-Analysis-System"

# Create QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=4
)

qr.add_data(url)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

# Resize QR
qr_img = qr_img.resize((300, 300))

# Create canvas for text
canvas = Image.new("RGB", (300, 360), "white")
canvas.paste(qr_img, (0, 0))

draw = ImageDraw.Draw(canvas)

try:
    font = ImageFont.truetype("arialbd.ttf", 24)  # Bold font
except:
    font = ImageFont.load_default()

text = "SCAN HERE"

bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]

draw.text(
    ((300 - text_width) // 2, 315),
    text,
    fill="black",
    font=font
)

# Save QR
canvas.save("retail_sales_github_qr.png")

print("✅ Professional QR Code Generated Successfully!")