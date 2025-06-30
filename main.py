import qrcode
import sys
import os

def generate_qr(url, output_dir="qr_codes"):
    os.makedirs(output_dir, exist_ok=True)
    img = qrcode.make(url)
    file_path = os.path.join(output_dir, "qr_code.png")
    img.save(file_path)
    print(f"QR Code saved to {file_path}")

if __name__ == "__main__":
    default_url = "https://www.njit.edu"
    url = sys.argv[1] if len(sys.argv) > 1 else default_url
    generate_qr(url)
