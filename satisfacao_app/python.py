from flask import session, redirect, url_for

app.secret_key = "uma_chave_simples"  # para sessão

ADMIN_URL = "/Admin_2026"
ADMIN_PASSWORD = "admin123"  # simples, apenas para o exercício

@app.route(ADMIN_URL, methods=["GET", "POST"])
def admin_login_or_dashboard():
    from flask import request
    if request.method == "POST":
        pwd = request.form.get("password")
        if pwd == ADMIN_PASSWORD:
            session["is_admin"] = True
            return redirect(url_for("admin_dashboard"))
    if not session.get("is_admin"):
        return render_template("admin_login.html")
    return redirect(url_for("admin_dashboard"))

@app.route(ADMIN_URL + "/dashboard")
def admin_dashboard():
    if not session.get("is_admin"):
        return redirect(ADMIN_URL)

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Totais por tipo
    c.execute("""
        SELECT satisfaction, COUNT(*) 
        FROM feedback 
        GROUP BY satisfaction
    """)
    rows = c.fetchall()
    conn.close()

    totals = { "muito_satisfeito": 0, "satisfeito": 0, "insatisfeito": 0 }
    for s, count in rows:
        totals[s] = count

    total_all = sum(totals.values()) or 1
    percentages = {k: (v / total_all) * 100 for k, v in totals.items()}

    return render_template("admin_dashboard.html",
                           totals=totals,
                           percentages=percentages)
