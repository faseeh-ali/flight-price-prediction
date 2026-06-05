# ✈️ Flight Price Prediction

Predicting Indian domestic flight fares using machine learning — end-to-end project covering data cleaning, feature engineering, model training, hyperparameter tuning, and business insights.

🚀 **Live Demo:** [Flight Price Predictor App](https://flight-price-prediction-eppasvzsokesaywfpqmcsn.streamlit.app/)

---

## 📌 Problem Statement

Flight ticket prices in India vary significantly based on factors like airline, duration, number of stops, and travel date. The goal of this project is to build a regression model that can accurately predict flight fares, helping travelers and businesses make informed booking decisions.

---

## 📂 Dataset

- **Source:** Kaggle — [Flight Fare Prediction Dataset](https://www.kaggle.com/datasets/nikhilmittal/flight-fare-prediction-mh)
- **Size:** ~10,000 rows, 11 columns
- **Target Variable:** `Price` (INR)
- **Features:** Airline, Source, Destination, Date of Journey, Departure Time, Arrival Time, Duration, Total Stops, Additional Info

---

## 🔧 Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3 |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Modeling | Scikit-learn (Random Forest, Extra Trees) |
| Tuning | RandomizedSearchCV |
| Model Saving | Joblib |
| Environment | Jupyter Notebook |

---

## 🛠️ Project Workflow

### 1. Data Cleaning
- Removed 1 missing row from `Route` and `Total_Stops` columns
- Removed duplicate rows

### 2. Feature Engineering
- Extracted `Journey_day` and `Journey_month` from `Date_of_Journey`
- Extracted hour and minute from `Dep_Time` and `Arrival_Time`
- Parsed `Duration` column into `Duration_hours` and `Duration_mins`
- Ordinal encoded `Total_Stops` (non-stop → 0, 1 stop → 1, etc.)
- One Hot Encoded `Airline`, `Source`, and `Destination`
- Dropped `Route` (128 unique values — high dimensionality, high overfitting risk)

### 3. Model Training & Comparison

| Model | R² Score | RMSE (₹) | MAE (₹) |
|---|---|---|---|
| Random Forest | 0.8118 | 1980 | 1182 |
| **Tuned Random Forest** | **0.8349** | **1855** | **1140** |
| Extra Trees Regressor | 0.7798 | 2142 | 1229 |

✅ **Best Model:** Tuned Random Forest Regressor (via RandomizedSearchCV)

### 4. Hyperparameter Tuning
Tuned using `RandomizedSearchCV` with 3-fold CV across parameters:
- `n_estimators`, `max_depth`, `min_samples_split`, `min_samples_leaf`

### 5. Feature Importance
Top predictors of flight price:
1. **Duration** — longer flights cost more
2. **Airline type** — premium vs budget airlines
3. **Journey date** — seasonal and weekend demand effects
4. **Total Stops** — indirect flights affect pricing patterns

---

## 📊 Visualizations

- Actual vs Predicted price scatter plot
- Residual distribution histogram
- Top 10 feature importance bar chart

---

## 💡 Business Insights

1. **Flight duration** is the strongest predictor of ticket price — operational and fuel costs drive fares up with distance
2. **Airline category** matters significantly — Jet Airways Business fares were notably higher than budget carriers like SpiceJet and AirAsia
3. **Journey date** (day + month) influences pricing due to seasonal demand and holiday travel patterns
4. **Number of stops** affects fare patterns, with non-stop flights sometimes priced higher due to convenience premium
5. **Price outliers** reflect real-world premium ticket scenarios — retained intentionally to preserve model realism

---

## 📁 Repository Structure

```
flight-price-prediction/
│
├── Flight_Price_Prediction.ipynb   # Main notebook
├── flight_price_prediction_model.pkl  # Saved best model
├── flight-fare/
│   └── Flight_Fare.xlsx            # Dataset
└── README.md
```

---

## 🚀 How to Run

1. Clone the repository
   ```bash
   git clone https://github.com/faseeh-ali/flight-price-prediction.git
   cd flight-price-prediction
   ```

2. Install dependencies
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn joblib openpyxl
   ```

3. Open the notebook
   ```bash
   jupyter notebook Flight_Price_Prediction.ipynb
   ```

4. Run all cells — model will be saved as `flight_price_prediction_model.pkl`

---

## 👤 Author

**Abdulla Faseeh Ali**  
B.Tech in AI & Data Science | Certified Data Scientist (DataMites)  
[LinkedIn](https://linkedin.com/in/faseeh-ali) • [GitHub](https://github.com/faseeh-ali)
