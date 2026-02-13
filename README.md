# 🗺️ Geo-Data Logic: Indian States & UTs Game

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Data Handling](https://img.shields.io/badge/Library-Pandas-150458?style=for-the-badge&logo=pandas)

> **A technical implementation of coordinate-based data visualization using Python and Pandas.**

---

## 🔄 System Architecture
The core objective was to transition from manual state management to a **Data-Driven Architecture**. The application serves as a rendering engine for an external CSV dataset.

* **Logic Pipeline**: Matches user input against normalized CSV indices and retrieves $(x, y)$ coordinates for real-time UI updates.
* **Reporting Logic**: Executes a data-diff between the master state list and user progress, outputting a learning-focused CSV for missed divisions.

## 🛠️ Technical Stack
* **Language**: Python 3.14
* **Data Management**: Pandas
* **Rendering**: Turtle Graphics
