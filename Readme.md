# 🔮 Zodiac Sign Finder App

A beautiful Streamlit web application that determines your zodiac sign based on your birthday and provides detailed information about your cosmic personality!

## Features

- 🎂 Easy birthday input with month/day selectors
- 🔮 Accurate zodiac sign calculation based on astronomical dates
- ✨ Beautiful, responsive design with custom CSS
- 📊 SQLite database storing zodiac sign information
- 🌟 Detailed descriptions including elements and ruling planets
- 📱 Mobile-friendly interface

## Tech Stack

- **Frontend**: Streamlit with custom CSS
- **Backend**: Python with SQLite database
- **Database**: SQLite (no server required)
- **Hosting**: Streamlit Cloud (free)

## Local Development

### Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

### Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd App_tester
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
python init_database.py
```

5. Run the app:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Deployment on Streamlit Cloud

### Option 1: Using GitHub (Recommended)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select your repository
5. Set main file as `app.py`
6. Deploy!

### Option 2: Direct Upload

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Upload your files directly
3. Streamlit Cloud will automatically detect and deploy

## Project Structure

```
App_tester/
├── app.py              # Main Streamlit application
├── init_database.py    # Database initialization script
├── requirements.txt    # Python dependencies
├── Readme.md          # This file
└── zodiac.db          # SQLite database (created automatically)
```

## Database Schema

The app uses a simple SQLite database with the following schema:

```sql
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
);
```

## Zodiac Signs Data

The app includes all 12 zodiac signs with accurate date ranges:

- ♈ **Aries** (March 21 - April 19) - Fire
- ♉ **Taurus** (April 20 - May 20) - Earth
- ♊ **Gemini** (May 21 - June 20) - Air
- ♋ **Cancer** (June 21 - July 22) - Water
- ♌ **Leo** (July 23 - August 22) - Fire
- ♍ **Virgo** (August 23 - September 22) - Earth
- ♎ **Libra** (September 23 - October 22) - Air
- ♏ **Scorpio** (October 23 - November 21) - Water
- ♐ **Sagittarius** (November 22 - December 21) - Fire
- ♑ **Capricorn** (December 22 - January 19) - Earth
- ♒ **Aquarius** (January 20 - February 18) - Air
- ♓ **Pisces** (February 19 - March 20) - Water

## Features Included

### User Interface
- Clean, modern design with gradient backgrounds
- Emoji integration for visual appeal
- Responsive layout for mobile and desktop
- Custom CSS styling

### Functionality
- Input validation for dates
- Accurate zodiac calculation including year transitions
- Database integration for sign information
- Error handling and user feedback

### Data Storage
- SQLite database for zodiac sign information
- Automatic database initialization
- Efficient queries for date-based lookups

## Future Enhancements

Potential features to add:
- User history/favorites
- Compatibility between signs
- Daily horoscopes
- Birth chart calculations
- Multiple language support

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Feel free to fork this project and submit pull requests for any improvements!

---

Made with ❤️ using Streamlit | Your cosmic journey awaits! 🌟