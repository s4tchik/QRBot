from flask import Flask, request, jsonify
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    """Генерация QR-кода на основе номера телефона."""
    data = request.json
    phone = data.get("phone")

    if not phone:
        return jsonify({"error": "Номер телефона не указан"}), 400

    # Создаем QR-код
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(phone)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Сохраняем изображение в буфер
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

    # Возвращаем URL изображения в формате base64
    return jsonify({"qr_code_url": f"data:image/png;base64,{img_base64}"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)