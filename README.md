# World Rally Cross Championship Management System

A command-line application built in Python to manage a World Rally Cross Championship effectively. This system allows users to:

- **Add Driver Details (ADD):** Input and store key details such as driver name, age, team, car, and current points.
- **Delete Driver Details (DDD):** Search and remove driver details using their name.
- **Update Driver Details (UDD):** Modify information of an existing driver by searching via name.
- **View Championship Standings Table (VCT):** Display standings ordered by points in descending order, neatly formatted.
- **Simulate Random Race (SRR):** Run a simulated race, assign points to drivers, and save race details (e.g., date, location, positions) to a text file.
- **View Race List Sorted by Date (VRL):** View past races, sorted chronologically using a custom algorithm.
- **Save to File (STF):** Save all championship and race data to text files for persistent storage.
- **Load from File (RFF):** Load data from text files to resume from where you left off.
- **Exit Program (ESC):** Exit the system safely.

## Key Features
- User-friendly console menu system for navigation and interaction.
- Persistent data storage in text files, allowing retrieval and resume capabilities.
- No reliance on external libraries for data sorting or database management.
- Custom algorithm for date-based sorting of races.

## Usage
The application is ideal for rally enthusiasts or organizations looking to manage driver standings, simulate races, and maintain a record of events efficiently.

## Requirements
- Python 3.6 or above.
