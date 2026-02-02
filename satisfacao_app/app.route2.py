@app.route("/api/admin/records")
def api_admin_records():
    from flask import request
    date_filter = request.args.get("date")

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if date_filter:
        c.execute("""
            SELECT id, satisfaction, date, time, weekday
            FROM feedback
            WHERE date = ?
            ORDER BY date DESC, time DESC
            LIMIT 200
        """, (date_filter,))
    else:
        c.execute("""
            SELECT id, satisfaction, date, time, weekday
            FROM feedback
            ORDER BY date DESC, time DESC
            LIMIT 200
        """)

    rows = c.fetchall()
    conn.close()

    records = [
        {
            "id": r[0],
            "satisfaction": r[1],
            "date": r[2],
            "time": r[3],
            "weekday": r[4]
        }
        for r in rows
    ]
    return jsonify({"records": records})
