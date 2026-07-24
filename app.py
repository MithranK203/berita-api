from flask import Flask, jsonify
from scraper import ambil_berita

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({
        "status": "success",
        "message": "API Berita Berjalan"
    })


@app.route("/berita")
def berita():
    try:
        data_berita = ambil_berita()

        return jsonify({
            "status": "success",
            "jumlah": len(data_berita),
            "data": data_berita
        })

    except Exception as error:
        return jsonify({
            "status": "error",
            "message": str(error)
        }), 500


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)