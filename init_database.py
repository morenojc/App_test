#!/usr/bin/env python3
"""
Database initialization script for the Zodiac Sign App
Creates and populates the SQLite database with zodiac signs data
"""

import sqlite3
import os

def create_database():
    """Create the zodiac signs database and populate it with data"""
    
    # Database file path
    db_path = "zodiac.db"
    
    # Remove existing database if it exists
    if os.path.exists(db_path):
        os.remove(db_path)
        print("Removed existing database")
    
    # Connect to database (creates new file)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create zodiac_signs table
    cursor.execute('''
        CREATE TABLE zodiac_signs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sign_name TEXT NOT NULL,
            start_month INTEGER NOT NULL,
            start_day INTEGER NOT NULL,
            end_month INTEGER NOT NULL,
            end_day INTEGER NOT NULL,
            description TEXT,
            element TEXT,
            ruling_planet TEXT,
            emoji TEXT
        )
    ''')
    
    # Zodiac signs data with accurate date ranges
    zodiac_data = [
        ("Aries", 3, 21, 4, 19, "Bold, ambitious, and adventurous. Natural leaders who love challenges.", "Fire", "Mars", "♈"),
        ("Taurus", 4, 20, 5, 20, "Reliable, patient, and practical. Values stability and enjoys luxury.", "Earth", "Venus", "♉"),
        ("Gemini", 5, 21, 6, 20, "Curious, adaptable, and communicative. Quick-witted and social.", "Air", "Mercury", "♊"),
        ("Cancer", 6, 21, 7, 22, "Nurturing, emotional, and intuitive. Strong connection to family and home.", "Water", "Moon", "♋"),
        ("Leo", 7, 23, 8, 22, "Confident, generous, and dramatic. Natural performers who love attention.", "Fire", "Sun", "♌"),
        ("Virgo", 8, 23, 9, 22, "Analytical, practical, and detail-oriented. Perfectionist with strong work ethic.", "Earth", "Mercury", "♍"),
        ("Libra", 9, 23, 10, 22, "Diplomatic, charming, and fair-minded. Seeks balance and harmony.", "Air", "Venus", "♎"),
        ("Scorpio", 10, 23, 11, 21, "Intense, passionate, and mysterious. Deep emotional and intuitive nature.", "Water", "Pluto", "♏"),
        ("Sagittarius", 11, 22, 12, 21, "Optimistic, adventurous, and philosophical. Loves freedom and exploration.", "Fire", "Jupiter", "♐"),
        ("Capricorn", 12, 22, 1, 19, "Ambitious, disciplined, and practical. Strong sense of responsibility and tradition.", "Earth", "Saturn", "♑"),
        ("Aquarius", 1, 20, 2, 18, "Independent, innovative, and humanitarian. Forward-thinking and unique.", "Air", "Uranus", "♒"),
        ("Pisces", 2, 19, 3, 20, "Compassionate, artistic, and intuitive. Deeply emotional and imaginative.", "Water", "Neptune", "♓")
    ]
    
    # Insert zodiac signs data
    cursor.executemany('''
        INSERT INTO zodiac_signs 
        (sign_name, start_month, start_day, end_month, end_day, description, element, ruling_planet, emoji)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', zodiac_data)
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    
    print(f"Database '{db_path}' created successfully!")
    print(f"Inserted {len(zodiac_data)} zodiac signs.")

def verify_database():
    """Verify the database was created correctly"""
    conn = sqlite3.connect("zodiac.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM zodiac_signs")
    count = cursor.fetchone()[0]
    print(f"Database contains {count} zodiac signs.")
    
    # Show a sample record
    cursor.execute("SELECT sign_name, emoji, element FROM zodiac_signs LIMIT 3")
    sample_signs = cursor.fetchall()
    print("\nSample signs:")
    for sign in sample_signs:
        print(f"  {sign[1]} {sign[0]} ({sign[2]})")
    
    conn.close()

if __name__ == "__main__":
    print("Creating zodiac signs database...")
    create_database()
    verify_database()
    print("\nDatabase initialization complete!")