# Digital Clock - Multiple Time Zones

A Python application that displays the current time and date across multiple time zones in a clean, modern GUI interface.

## 🌍 Features

- **Real-Time Updates**: Updates every second to show the current time
- **Multiple Time Zones**: Displays 9 different time zones simultaneously
- **Clean UI**: Modern dark-themed interface with color-coded information
- **Easy to Customize**: Simply modify the timezone list to display your preferred zones
- **Error Handling**: Gracefully handles invalid timezone entries
- **Date Display**: Shows both time (HH:MM:SS) and date (YYYY-MM-DD)

## 📍 Included Time Zones

- UTC (Coordinated Universal Time)
- US/Eastern (Eastern Standard/Daylight Time)
- Europe/London (Greenwich Mean Time / British Summer Time)
- Asia/Tokyo (Japan Standard Time)
- Australia/Sydney (Australian Eastern Time)
- Asia/Kolkata (Indian Standard Time)
- US/Pacific (Pacific Standard/Daylight Time)
- Europe/Paris (Central European Time)
- Asia/Dubai (Gulf Standard Time)

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- tkinter (usually comes with Python)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/ahersoham44-droid/customer-churn-prediction.git
cd customer-churn-prediction
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📖 Usage

Run the application:
```bash
python digital_clock.py
```

The application window will open displaying the current time and date for all configured time zones in a grid layout.

## 🎨 UI Layout

The application displays clocks in a 3-column grid:
- **Green Text**: Timezone names
- **Cyan Text**: Current time (HH:MM:SS)
- **Yellow Text**: Current date (YYYY-MM-DD)
- **Dark Background**: Modern, comfortable viewing experience

## 🔧 Customization

To display different time zones, edit the `time_zones` list in the `main()` function:

```python
time_zones = [
    "UTC",
    "US/Eastern",
    "Europe/London",
    # Add your preferred timezones here
]
```

For a complete list of available timezones, check [pytz documentation](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

## 📦 Dependencies

- **pytz**: Python timezone library for accurate timezone handling
- **tkinter**: GUI toolkit (included with Python)

## 🏗️ Project Structure

```
digital_clock.py       # Main application file
requirements.txt       # Project dependencies
README_CLOCK.md        # This file
```

## 💻 Code Overview

### Main Classes

**DigitalClockApp**
- `__init__(root, time_zones)`: Initialize the application
- `setup_ui()`: Create the GUI layout
- `get_time_in_timezone(tz)`: Get current time for a timezone
- `update_time()`: Update all clock displays

### Key Methods

- `setup_ui()`: Builds the user interface with frames for each timezone
- `get_time_in_timezone()`: Fetches current time in specified timezone
- `update_time()`: Refreshes all time displays every second

## 🐛 Error Handling

The application includes error handling for:
- Invalid timezone strings (displays "ERROR" and "Invalid TZ")
- Missing pytz library (installation via requirements.txt)

## 📝 Example Output

```
🕐 Digital Clock - Multiple Time Zones

┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ UTC         │  │ US/Eastern  │  │ Europe/London│
│ 14:30:45    │  │ 10:30:45    │  │ 15:30:45    │
│ 2024-01-15  │  │ 2024-01-15  │  │ 2024-01-15  │
└─────────────┘  └─────────────┘  └─────────────┘

[More timezone boxes below...]
```

## 🔮 Future Enhancements

Potential features for future versions:
- [ ] 12/hour vs 24-hour format toggle
- [ ] Configurable update frequency
- [ ] Add/remove timezones on the fly
- [ ] Timezone name search
- [ ] Display timezone offset from UTC
- [ ] Alarm functionality
- [ ] Custom color themes

## 📄 License

This project is part of the customer-churn-prediction repository.

## 👤 Author

**ahersoham44-droid**

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for any improvements!

---

**Last Updated**: September 8, 2024
**Version**: 1.0.0
