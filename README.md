# 📊 CORD-19 Data Explorer

This project is part of the **Frameworks Assignment**.  
It explores the **CORD-19 metadata.csv dataset** using **Pandas, Matplotlib, and Streamlit**.  

---

## 🚀 Features
- Load and clean the CORD-19 metadata dataset  
- Handle missing values and prepare data for analysis  
- Perform basic analysis:
  - Publications by year  
  - Top journals publishing COVID-19 research  
  - Sources of papers  
- Interactive **Streamlit App**:
  - Year range filter  
  - Visualizations (bar charts, counts)  
  - Data sample preview  

---

## 📂 Project Structure
```
Frameworks_Assignment/
│
├── app.py              # Streamlit app
├── frames.py           # Data cleaning, analysis & visualization script
├── metadata.csv        # Dataset (CORD-19 metadata file)
├── CORD19_Report.docx  # Report with findings & reflection
└── README.md           # Project documentation
```

---

## 🛠️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/itsvickiey/Frameworks_Assignment.git
   cd Frameworks_Assignment
   ```

2. **Create virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Mac/Linux
   venv\Scripts\activate    # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   Or install manually:
   ```bash
   pip install pandas matplotlib streamlit seaborn
   ```

---

## ▶️ Running the Project

- **Run the Streamlit App**
  ```bash
  streamlit run app.py
  ```

- **Run the analysis script**
  ```bash
  python frames.py
  ```

---

## 📊 Example Visualizations
- Publications by Year  
- Top 10 Journals  
- Distribution of Paper Counts by Source  

---

## 📝 Report
The project includes a detailed **report (CORD19_Report.docx)** with:
- Data cleaning steps  
- Analysis results  
- Visualizations  
- Reflections and challenges  

---

## 🤝 Author
**Victoria Mumo Mbithi**  
Bachelor of Science in Information Technology  
Dedan Kimathi University of Technology  

GitHub: [@itsvickiey](https://github.com/itsvickiey)  

---

## 📌 Notes
- Ensure the `metadata.csv` file is in the same folder as `app.py` and `frames.py`.  
- Some columns contain many missing values, so preprocessing is required.  
