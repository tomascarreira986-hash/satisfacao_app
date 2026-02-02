# app.py
import sqlite3
from flask import Flask, render_template, request, jsonify, send_file
from datetime import datetime
import csv
import io
import os

app = Flask(__name__)
DB_PATH = "feedback.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            satisfaction TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            weekday TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()
