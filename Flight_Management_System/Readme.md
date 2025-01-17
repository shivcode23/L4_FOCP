# Flight Management System

This folder contains the code and resources for a comprehensive Flight Management System. Below is a detailed description of each file, its purpose, and how it works.

---

## Files

### Flight_Management_System_Presentation.pptx
- **Description**: A PowerPoint presentation explaining the Flight Management System.
- **Purpose**: To provide an overview and detailed explanation of the system's features and functionalities.
- **Contents**: Slides covering the system architecture, use cases, and user interface.

### code/
This directory contains the main code files for the Flight Management System.

#### flight_history.xlsx
- **Description**: An Excel file containing historical flight data.
- **Purpose**: To store and manage historical data of flights for analysis and reporting.
- **Contents**: Columns for flight number, date, origin, destination, passenger count, and status.

#### flights.xlsx
- **Description**: An Excel file containing current flight data.
- **Purpose**: To store and manage data of ongoing and upcoming flights.
- **Contents**: Columns for flight number, date, origin, destination, available seats, and status.

#### main.py
- **Description**: The main Python script for the Flight Management System.
- **Purpose**: To manage and execute the core functionalities of the system, including flight scheduling, booking, and management.
- **How it works**:
  - **Initialization**: Loads flight data from `flights.xlsx` and `flight_history.xlsx` using the `pandas` library.
  - **Flight Scheduling**: Allows users to schedule new flights by adding entries to `flights.xlsx`.
  - **Booking Management**: Manages flight bookings by updating the available seats and passenger information.
  - **Reporting**: Generates reports based on historical flight data, providing insights into flight performance and trends.
  - **User Interface**: Provides a command-line interface for users to interact with the system.
- **Key Functions**:
  - `load_data()`: Loads flight data from Excel files into pandas DataFrames.
  - `save_data()`: Saves updated flight data back to the Excel files.
  - `schedule_flight()`: Adds a new flight to the `flights.xlsx` file.
  - `book_flight()`: Books a flight and updates the available seats.
  - `generate_report()`: Generates reports based on historical flight data.
- **Run**: 
  ```sh
  python code/main.py
  ```

---

### requirements.txt
- **Description**: A text file listing the dependencies required to run the Flight Management System.
- **Purpose**: To ensure that all necessary Python packages are installed.
- **Dependencies**:
  - `pandas`: For data manipulation and analysis.
  - `openpyxl`: For reading and writing Excel files.
- **How to install dependencies**:
  ```sh
  pip install -r requirements.txt
  ```

### Introduction.md
- **Description**: A Markdown file providing an introduction to the Flight Management System.
- **Purpose**: To give a brief overview of the system, its features, and how to use it.
- **Contents**: Sections on system objectives, key features, and user instructions.

---

## How to Run
1. Ensure you have Python installed on your system.
2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the main script:
   ```sh
   python code/main.py
   ```

---

## Features
- **Flight Scheduling**: Schedule new flights and manage existing ones.
- **Booking Management**: Book flights and manage passenger information.
- **Data Analysis**: Analyze historical flight data for reporting and decision-making.
- **User Interface**: Command-line interface for easy interaction with the system.

---

## Mechanism
The Flight Management System works by reading flight data from Excel files, allowing users to interact with the data through a command-line interface. Users can schedule flights, manage bookings, and generate reports. The system updates the Excel files with any changes made during the session.

### Detailed Workflow
1. **Initialization**: The system loads flight data from `flights.xlsx` and `flight_history.xlsx` into pandas DataFrames.
2. **User Interaction**: Users interact with the system through a series of command-line prompts.
3. **Flight Scheduling**: Users can add new flights by providing flight details, which are then appended to the `flights.xlsx` file.
4. **Booking Management**: Users can book flights by specifying the flight number and passenger details. The system updates the available seats and records the booking.
5. **Data Analysis**: Users can generate reports on historical flight data, including metrics such as average passenger count, flight frequency, and performance trends.
6. **Data Persistence**: Any changes made during the session are saved back to the Excel files to ensure data persistence.

---

## Purpose
The purpose of the Flight Management System is to provide a comprehensive tool for managing flights, bookings, and analyzing flight data. It is designed to be used by airlines, travel agencies, and other organizations involved in flight management. The system aims to streamline flight operations, improve booking efficiency, and provide valuable insights through data analysis.

---

## Conclusion
The Flight Management System is a robust and versatile tool for managing flight operations. With its comprehensive features and user-friendly interface, it simplifies the process of scheduling flights, managing bookings, and analyzing flight data. By leveraging the power of Python and pandas, the system ensures efficient data handling and provides valuable insights for decision-making.
