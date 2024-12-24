import requests

from book.models import BookItem


class GetQRCodeBook:
    def get_request_book(self, number):
        params = {
            "frame_name": "no-frame",
            # "qr_code_text": f"http://127.0.0.1:8000/library/book_details/{number}/",
            "qr_code_text": number,
            "image_format": "SVG",
            "qr_code_logo": "no-logo"
        }
        response = requests.post("https://api.qr-code-generator.com/v1/create?access-token=your-acces-token-here",
                                 params=params)
        if response.status_code == 200:
            return response
        else:
            raise Exception("Failed to create QR code")


# qr = GetQRCodeBook()
# print(qr.get_request_book(12))
