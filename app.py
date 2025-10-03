#!/usr/bin/env python3
"""
Zodiac Sign App
A Streamlit web application that determines your zodiac sign based on your birthday
"""

import streamlit as st
import sqlite3
import datetime
from typing import Tuple, Optional

# Configure page
st.set_page_config(
    page_title="🔮 Zodiac Sign Finder",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

def init_database_if_needed():
    """Initialize database if it doesn't exist"""
    import os
    if not os.path.exists("zodiac.db"):
        exec(open("init_database.py").read())

def get_zodiac_sign(month: int, day: int) -> Optional[dict]:
    """
    Get zodiac sign information based on birth month and day
    
    Args:
        month: Birth month (1-12)
        day: Birth day (1-31)
    
    Returns:
        Dictionary with zodiac sign information or None if not found
    """
    try:
        conn = sqlite3.connect("zodiac.db")
        cursor = conn.cursor()
        
        # Query to find the zodiac sign
        # Handle year transition (Capricorn spans Dec-Jan)
        query = '''
            SELECT sign_name, description, element, ruling_planet, emoji
            FROM zodiac_signs
            WHERE (
                -- Normal case: same year
                (start_month < end_month AND ? = start_month AND ? >= start_day) OR
                (start_month < end_month AND ? = end_month AND ? <= end_day) OR
                (start_month < end_month AND ? > start_month AND ? < end_month) OR
                -- Year transition case (Dec-Jan)
                (start_month > end_month AND (
                    (? = start_month AND ? >= start_day) OR
                    (? = end_month AND ? <= end_day) OR
                    (? > start_month OR ? < end_month)
                ))
            )
        '''
        
        cursor.execute(query, (month, day, month, day, month, month, 
                              month, day, month, day, month, month))
        result = cursor.fetchone()
        conn.close()
        
        if result:
            return {
                "name": result[0],
                "description": result[1],
                "element": result[2],
                "ruling_planet": result[3],
                "emoji": result[4]
            }
        return None
        
    except Exception as e:
        st.error(f"Database error: {e}")
        return None

def validate_date(month: int, day: int) -> bool:
    """Validate if the given month and day form a valid date"""
    try:
        # Use 2024 as it's a leap year to handle Feb 29
        datetime.date(2024, month, day)
        return True
    except ValueError:
        return False

def main():
    """Main Streamlit application"""
    
    # Initialize database
    init_database_if_needed()
    
    # Custom CSS for better styling
    st.markdown("""
        <style>
        .main-title {
            text-align: center;
            color: #4B0082;
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        .subtitle {
            text-align: center;
            color: #666;
            font-size: 1.2rem;
            margin-bottom: 2rem;
        }
        .zodiac-result {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            border-radius: 15px;
            margin: 2rem 0;
            color: white;
            text-align: center;
        }
        .zodiac-emoji {
            font-size: 4rem;
            margin-bottom: 1rem;
        }
        .zodiac-name {
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        .zodiac-details {
            background: rgba(255, 255, 255, 0.1);
            padding: 1rem;
            border-radius: 10px;
            margin-top: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # App header
    st.markdown('<h1 class="main-title">🔮 Zodiac Sign Finder</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Discover your zodiac sign and learn about your cosmic personality!</p>', unsafe_allow_html=True)
    
    # Create input form
    st.markdown("### 🎂 Enter Your Birthday")
    
    col1, col2 = st.columns(2)
    
    with col1:
        month = st.selectbox(
            "Month",
            options=list(range(1, 13)),
            format_func=lambda x: datetime.date(2024, x, 1).strftime("%B"),
            index=0
        )
    
    with col2:
        # Get max days for selected month
        if month in [1, 3, 5, 7, 8, 10, 12]:
            max_day = 31
        elif month in [4, 6, 9, 11]:
            max_day = 30
        else:  # February
            max_day = 29
            
        day = st.selectbox(
            "Day",
            options=list(range(1, max_day + 1)),
            index=0
        )
    
    # Add some spacing
    st.markdown("---")
    
    # Calculate and display zodiac sign
    if st.button("🌟 Find My Zodiac Sign", type="primary", use_container_width=True):
        if validate_date(month, day):
            zodiac_info = get_zodiac_sign(month, day)
            
            if zodiac_info:
                # Display zodiac result with custom styling
                st.markdown(f"""
                    <div class="zodiac-result">
                        <div class="zodiac-emoji">{zodiac_info['emoji']}</div>
                        <div class="zodiac-name">{zodiac_info['name']}</div>
                        <p style="font-size: 1.1rem; line-height: 1.6;">{zodiac_info['description']}</p>
                        <div class="zodiac-details">
                            <p><strong>Element:</strong> {zodiac_info['element']}</p>
                            <p><strong>Ruling Planet:</strong> {zodiac_info['ruling_planet']}</p>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Add fun facts section
                st.markdown("### ✨ Fun Facts About Your Sign")
                
                # Element descriptions
                element_info = {
                    "Fire": "🔥 Fire signs are passionate, dynamic, and energetic!",
                    "Earth": "🌍 Earth signs are practical, stable, and grounded!",
                    "Air": "💨 Air signs are intellectual, communicative, and social!",
                    "Water": "🌊 Water signs are emotional, intuitive, and empathetic!"
                }
                
                if zodiac_info['element'] in element_info:
                    st.info(element_info[zodiac_info['element']])
                
            else:
                st.error("❌ Could not determine zodiac sign. Please check your date.")
        else:
            st.error("❌ Invalid date. Please enter a valid month and day.")
    
    # Add footer
    st.markdown("---")
    st.markdown("""
        <div style="text-align: center; color: #666; margin-top: 2rem;">
            <p>Made with ❤️ using Streamlit | Your cosmic journey awaits! 🌟</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Sidebar with additional info
    with st.sidebar:
        st.markdown("### 📚 About Zodiac Signs")
        st.markdown("""
        Zodiac signs are based on the position of the sun at the time of your birth. 
        Each sign has unique characteristics and is associated with specific elements and planets.
        
        **The 12 Zodiac Signs:**
        - ♈ Aries (Mar 21 - Apr 19)
        - ♉ Taurus (Apr 20 - May 20)
        - ♊ Gemini (May 21 - Jun 20)
        - ♋ Cancer (Jun 21 - Jul 22)
        - ♌ Leo (Jul 23 - Aug 22)
        - ♍ Virgo (Aug 23 - Sep 22)
        - ♎ Libra (Sep 23 - Oct 22)
        - ♏ Scorpio (Oct 23 - Nov 21)
        - ♐ Sagittarius (Nov 22 - Dec 21)
        - ♑ Capricorn (Dec 22 - Jan 19)
        - ♒ Aquarius (Jan 20 - Feb 18)
        - ♓ Pisces (Feb 19 - Mar 20)
        """)

if __name__ == "__main__":
    main()