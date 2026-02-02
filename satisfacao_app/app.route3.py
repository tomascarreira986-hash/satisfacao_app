@app.route("/export/csv")
def export_csv():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, satisfaction, date, time, weekday FROM feedback")
    rows = c.fetchall()
    conn.close()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["id", "satisfaction", "date", "time", "weekday"])
    writer.writerows(rows)

    mem = io.BytesIO()
    mem.write(output.getvalue().encode("utf-8"))
    mem.seek(0)

    return send_file(
        mem,
        as_attachment=True,
        download_name="feedback.csv",
        mimetype="text/csv"
    )

@app.route("/export/txt")
def export_txt():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, satisfaction, date, time, weekday FROM feedback")
    rows = c.fetchall()
    conn.close()

    lines = ["id\tsatisfaction\tdate\ttime\tweekday"]
    for r in rows:
        lines.append("\t".join(str(x) for x in r))

    mem = io.BytesIO("\n".join(lines).encode("utf-8"))
    mem.seek(0)

    return send_file(
        mem,
        as_attachment=True,
        download_name="feedback.txt",
        mimetype="text/plain"
    )
