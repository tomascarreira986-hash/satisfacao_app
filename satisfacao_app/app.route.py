@app.route("/api/feedback", methods=["POST"])
def api_feedback():
    data = request.get_json()
    satisfaction = data.get("satisfaction")

    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")
    weekday_str = now.strftime("%A")  # ou traduzir para PT

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        INSERT INTO feedback (satisfaction, date, time, weekday)
        VALUES (?, ?, ?, ?)
    """, (satisfaction, date_str, time_str, weekday_str))
    conn.commit()
    conn.close()

    return jsonify({"status": "ok"})
