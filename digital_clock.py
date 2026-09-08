"""
Digital Clock Application - Displays the current time in different time zones
"""

import tkinter as tk
from tkinter import font
from datetime import datetime
import pytz
from typing import List, Tuple


class DigitalClockApp:
    """A digital clock application that displays time in multiple time zones."""
    
    def __init__(self, root: tk.Tk, time_zones: List[str]):
        """
        Initialize the Digital Clock Application.
        
        Args:
            root: The root Tkinter window
            time_zones: List of timezone strings (e.g., ['UTC', 'US/Eastern', 'Asia/Tokyo'])
        """
        self.root = root
        self.root.title("Digital Clock - Multiple Time Zones")
        self.root.geometry("900x400")
        self.root.configure(bg="#1a1a1a")
        self.root.resizable(False, False)
        
        self.time_zones = time_zones
        self.time_labels = {}
        self.timezone_labels = {}
        
        # Configure fonts
        self.time_font = font.Font(family="Courier New", size=36, weight="bold")
        self.tz_font = font.Font(family="Courier New", size=14, weight="bold")
        self.label_font = font.Font(family="Courier New", size=10)
        
        self.setup_ui()
        self.update_time()
    
    def setup_ui(self) -> None:
        """Set up the user interface with clock displays for each timezone."""
        # Title
        title = tk.Label(
            self.root,
            text="🕐 Digital Clock - Multiple Time Zones",
            font=("Courier New", 16, "bold"),
            bg="#1a1a1a",
            fg="#00ff00"
        )
        title.pack(pady=10)
        
        # Main frame for clocks
        main_frame = tk.Frame(self.root, bg="#1a1a1a")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create clock display for each timezone
        for i, tz in enumerate(self.time_zones):
            # Calculate grid position
            row = i // 3
            col = i % 3
            
            # Frame for each timezone
            frame = tk.Frame(
                main_frame,
                bg="#2a2a2a",
                bd=2,
                relief=tk.RAISED,
                width=250,
                height=120
            )
            frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            frame.pack_propagate(False)
            
            # Timezone name
            tz_label = tk.Label(
                frame,
                text=tz,
                font=self.tz_font,
                bg="#2a2a2a",
                fg="#00ff00"
            )
            tz_label.pack(pady=5)
            
            # Time display
            time_label = tk.Label(
                frame,
                text="00:00:00",
                font=self.time_font,
                bg="#2a2a2a",
                fg="#00ffff"
            )
            time_label.pack(pady=5)
            
            # Date display
            date_label = tk.Label(
                frame,
                text="YYYY-MM-DD",
                font=self.label_font,
                bg="#2a2a2a",
                fg="#ffff00"
            )
            date_label.pack(pady=5)
            
            # Store references
            self.time_labels[tz] = time_label
            self.timezone_labels[tz] = (tz_label, date_label)
        
        # Configure grid weights
        for i in range((len(self.time_zones) + 2) // 3):
            main_frame.grid_rowconfigure(i, weight=1)
        for i in range(3):
            main_frame.grid_columnconfigure(i, weight=1)
    
    def get_time_in_timezone(self, tz: str) -> Tuple[str, str]:
        """
        Get the current time and date in a specific timezone.
        
        Args:
            tz: Timezone string
            
        Returns:
            Tuple of (time_string, date_string)
        """
        try:
            tz_obj = pytz.timezone(tz)
            now = datetime.now(tz_obj)
            time_str = now.strftime("%H:%M:%S")
            date_str = now.strftime("%Y-%m-%d")
            return time_str, date_str
        except pytz.exceptions.UnknownTimeZoneError:
            return "ERROR", "Invalid TZ"
    
    def update_time(self) -> None:
        """Update all clock displays with current time."""
        for tz in self.time_zones:
            time_str, date_str = self.get_time_in_timezone(tz)
            self.time_labels[tz].config(text=time_str)
            self.timezone_labels[tz][1].config(text=date_str)
        
        # Schedule next update in 1000ms (1 second)
        self.root.after(1000, self.update_time)


def main():
    """Main entry point for the Digital Clock application."""
    # Define timezones to display
    time_zones = [
        "UTC",
        "US/Eastern",
        "Europe/London",
        "Asia/Tokyo",
        "Australia/Sydney",
        "Asia/Kolkata",
        "US/Pacific",
        "Europe/Paris",
        "Asia/Dubai"
    ]
    
    root = tk.Tk()
    app = DigitalClockApp(root, time_zones)
    root.mainloop()


if __name__ == "__main__":
    main()
