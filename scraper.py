import feedparser


RSS_URL = "https://www.cnnindonesia.com/rss"


def ambil_berita():
    feed = feedparser.parse(RSS_URL)
    hasil = []

    for item in feed.entries[:10]:
        hasil.append({
            "judul": item.get("title", ""),
            "link": item.get("link", ""),
            "sumber": "CNN Indonesia",
            "tanggal": item.get("published", "")
        })

    return hasil