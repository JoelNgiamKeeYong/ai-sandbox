Number of attempts: 1 out of 2

Grade: pass 

## Overview

### Criterias Met:

- **Data Loading and Duplicate Handling**: 
    - You successfully loaded the data from a CSV file and ensured successful loading into a Pandas DataFrame, as demonstrated in the snippets:
        ```python
        # ⏬ **4. Load Data** This section will perform the following tasks: - Establish a connection to the SQLite database and retrieve the `noshow` table into a Pandas DataFrame.
        ```
        ```python
        from src.load_data import load_data
        ```
        ```python
        df = load_data(db_path=DB_PATH, db_table_name=DB_TABLE_NAME)
        ```
        ```python
        df.shape # Displays the dimensions of the DataFrame (i.e. number of rows and columns)
        ```
    - Excellent job on identifying and handling duplicates, where you confirmed no duplicated rows remained in the dataset:
        ```python
        duplicate_rows = df_cleaned[df_cleaned.duplicated(keep=False)]
        duplicate_rows
        ```
        ```python
        # Verified using df.duplicated().sum(): No fully duplicated rows were found in the dataset.
        ```
        ```python
        # Additionally, the booking_id column contains 119,391 unique values, which matches the total number of rows in the dataset.
        ```
    - These actions are crucial as they ensure the dataset's integrity and accuracy, forming the foundation for reliable modeling.

### Criterias Met (Partially):

- **Data Type Check and Conversion**:
    - You reviewed data types for certain columns, specifically documenting changes for `price` and `no show`, but comprehensive documentation for all columns was lacking:
        ```python
        df.info()
        ```
        ```python
        # Display in normal notation instead of scientific with pd.option_context('float_format', '{:f}'.format):
        # Include all columns in the summary statistics
        df.describe(include='all')
        ```
        - Establishing correct data types is pivotal for ensuring accurate computations and analysis during model training.

- **Descriptive Statistics**:
    - Descriptive statistics were generated using methods like `df.describe(include='all')`, although detailed measures of central tendency and frequency counts for categorical features were not fully explored:
        ```python
        df.describe(include='all')
        ```
        ```python
        df.info()
        ```
        - Complete descriptive statistics provide insights into data distribution, essential for interpreting feature importance and data preprocessing.

- **Outlier Identification and Handling**:
    - You've visualized outliers, particularly in the `price` column, but did not specify a statistical method for detection or detail binning strategies:
        ```python
        perform_univariate_analysis(df=df_cleaned, column_name='price', show_graphs=False, show_distribution=False)
        ```
        - Proper outlier handling is vital to mitigate their impact on model accuracy and reduce variability in the dataset.

- **Handling Missing Values**:
    - While missing values were identified, the methodology for managing these, including imputation strategies, was not exhaustively documented:
        ```python
        df.isnull().sum()
        ```
        ```python
        msno.heatmap(df[['price', 'room']], figsize=(8, 4), cmap='flare')
        ```
        - Appropriately handling missing data is critical to enhance model reliability and prevent biased outcomes.

- **Feature Classification**:
    - You acknowledged the need to convert some features like `no_show` and `price` into suitable data types but did not fully classify all features:
        ```python
        💡 **Incorrect Data Types**: - The target variable `no_show` is currently as type float64, which is technically correct, but these column should be mapped to categorical values (i.e.1 = Yes and 0 = No) as type object for classification purposes.
        ```
        - Proper feature classification facilitates targeted data cleaning and preprocessing strategies, improving model performance.

- **Visualization of Feature Distributions**:
    - Although employing visualizations for missing data was effective, detailed distribution visualizations for numeric and categorical features were limited:
        ```python
        msno.matrix(df)
        ```
        ```python
        sns.PairGrid(data=df_train_engineered, hue=TARGET, palette='inferno', diag_sharey=False)
        ```
        - Detailed visualizations aid in recognizing patterns and anomalies, informing robust model design.

- **Correlation and Association Tests**:
    - A correlation heatmap was provided, yet specific association tests like Chi-Square for categorical features were not extensively applied or discussed:
        ```python
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
        plt.title("Correlation Heatmap of Numerical Features", fontsize=14, fontweight="bold")
        plt.show()
        ```
        - Understanding correlations helps in feature selection and dimensionality reduction, optimizing the training process.
        
### Criterias Not Fulfilled:

- **There are no criteria that were completely unfulfilled**, suggesting a baseline of engagement with each requirement, even if only partially addressed. Ensuring completeness across all tasks will solidify the foundations of your classification model and enhance its predictive capabilities. 
### Extra Effort Recognition:

- **Feature Engineering for Temporal and Duration Insights in Customer Behavior:**

```python
from src.preprocess_data import create_months_to_arrival_feature
[df_train_engineered] = create_months_to_arrival_feature(list_of_dfs=[df_train_engineered])
df_train_engineered
```
```python
from src.preprocess_data import create_stay_duration_days_feature
[df_train_engineered] = create_stay_duration_days_feature(list_of_dfs=[df_train_engineered])
df_train_engineered
```

- You implemented advanced feature engineering techniques by creating new features, such as `months_to_arrival` and `stay_duration_days`. These features provide deeper insights into customer planning and behavior patterns, which are not immediately apparent from the raw dataset. This enhancement allows the predictive model to capture nuances in customer booking habits and their potential impact on no-show rates, thus playing a crucial role in formulating more targeted strategies for the hotel chain to reduce expenses due to no-shows. Your proactive approach to deriving additional inferential features is commendable and significantly enhances the dataset's analytical depth.
## Things to Work on

1. **Comprehensive Data Type Conversion and Documentation**:
   - You have started converting data types, like changing the target variable `no_show` and `price`, but ensure you extend this to all columns needing conversion. Use `.info()` after conversion to confirm changes.
   - Document each conversion clearly in your notebook to enhance reproducibility and understanding, marking before-and-after states for key columns.

2. **Enhanced Descriptive Statistics**:
   - While you have described some data using `df.describe()`, consider including additional measures for both numeric and categorical features such as mean, median, mode, standard deviation, and frequency counts.
   - Clearly list features with their types (numeric or categorical) before exploring their statistics to provide a comprehensive overview.

3. **Targeted Handling of Outliers**:
   - For feature columns like `price`, where potential outliers exist, explicitly detail the statistical methods used for their detection, such as Interquartile Range (IQR) or z-score thresholds, and communicate how you handle them using techniques like binning, if applicable.
   - Clearly document the thought process so that readers can understand why certain decisions regarding outlier handling were made.

4. **Systematic Handling of Missing Values**:
   - Continue using methods like visualizations to identify missing values, but make sure to provide a clear percentage breakdown of missingness for each feature.
   - Explicitly document the method used for dealing with these missing values, whether it's mean/median imputation, filling, or dropping, and apply it systematically across relevant columns.

5. **Distinct Classification of Features**:
   - While you've begun assessing data types, ensure full classification of features into numeric or categorical categories is explicitly stated.
   - List all features with their classifications early in your analysis, setting a foundation for differentiated budgetary allocation and preprocessing treatment.

6. **Comprehensive Generation of Visualizations**:
   - Although several visualizations are present, ensure that both numeric and categorical feature distributions are thoroughly explored using histograms, box plots, and count plots.
   - These plots will help to better understand feature distributions and should be clearly labeled with axes and titles to aid interpretation.

7. **Performing Association Tests and Correlation Analysis**:
   - In addition to using heatmaps, include association tests like Chi-Square for categorical variables to bolster your understanding of their relationships.
   - For numerical features, ensure clear articulation of the implications of correlation findings and consider how these insights could inform your feature selection and modeling phase.

Addressing these aspects will significantly contribute to a more robust exploratory analysis and lay a strong foundation for subsequent modeling efforts.
## Extra Recommendations

1. **Enhanced Duplicate Detection Approach:**
   - While your current approach effectively identifies duplicate entries using the `duplicated()` function, consider implementing pairwise comparisons for critical features beyond `booking_id` in future analyses. This can help identify partial duplicates where only some columns are identical while others vary slightly due to data entry errors. 
   - Personalized Feedback: Evaluate additional attributes such as `branch`, `arrival_month`, and `room` for potential matches, and use domain knowledge to determine if such partial duplicates need further investigation or consolidation.

2. **Utilizing Domain Knowledge for Deduplication:**
   - Integrate domain-specific rules and thresholds for what constitutes a duplicate. This could include specific timeframes or guest demographics that are contextually unique or redundant.
   - Personalized Feedback: Collaborate with domain experts to craft these rules to align the data processing with real-world scenarios, thus enhancing the accuracy of your duplicate handling strategy.

3. **Combining Duplicate Handling with Data Cleaning:**
   - Explore methods to integrate duplicate detection with broader data cleaning tasks. This could involve linking duplicated entries to other anomalies such as outliers or missing data.
   - Personalized Feedback: By coordinating duplicate detection with other cleaning efforts, you may discover additional insights and inconsistencies that manifest in complex datasets, refining not just the integrity but the overall quality of your dataset. 

Implementing these strategies will deepen your understanding and handling of data quality issues, thereby leading to more accurate model inputs and improved predictive performance.
## Code Evaluation

Your recent code submission has been carefully reviewed and showcases proficient coding skills with attention to the key aspects of efficiency, readability, style, conventions, and scalability. You've demonstrated a strong understanding of how to effectively manage configurations and data handling using Python and its libraries.

___

### Commendable Code Practices

```python
# Define the config file
CONFIG_FILE = "config.yaml"

# Load the configuration file
try:
    with open(CONFIG_FILE, "r") as f:
        config = yaml.safe_load(f)

        # Extract config
        DATA_URL = config.get("data_url")
        DB_PATH = config.get("db_path")
        DB_TABLE_NAME = config.get("db_table_name")
        TARGET = config.get("target")
        TEST_SIZE = config.get("test_size")
        RANDOM_STATE = config.get("random_state")

        print(f"✅ Config loaded successfully.")

except FileNotFoundError:
    raise FileNotFoundError("❌ Configuration file 'config.yaml' not found.")

# Validate configuration
if not DATA_URL or not DB_PATH or not DB_TABLE_NAME or not TARGET or not TEST_SIZE or not RANDOM_STATE:
    raise ValueError("❌ Missing constants in the configuration file. Please check the config.yaml file.")
```

- This code effectively loads and validates the configuration, demonstrating excellent error handling and readability.

```python
# Ensure the 'data' directory exists
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

# Check if the file exists locally
if os.path.exists(DB_PATH):
    print("✅ File already exists.")
else:
    print("⚠️ File not found. Downloading...")
    try:
        # Download the file
        response = requests.get(DATA_URL, stream=True)
        response.raise_for_status() 
        
        with open(DB_PATH, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"✅ File downloaded successfully: {DB_PATH}")
    except requests.RequestException as e:
        print(f"❌ Error downloading the file: {e}")
```

- The code exhibits reliable file downloading procedures, ensuring directories exist and handling download errors robustly, showcasing thoughtful programming practices.

```python
# Create copy of DataFrame
df_cleaned = df.copy()
```

- This snippet is a best practice for data manipulation, ensuring the original data remains unaltered.

```python
duplicate_rows = df_cleaned[df_cleaned.duplicated(keep=False)]
duplicate_rows
```

- Efficiently identifies duplicates using pandas built-in capabilities, promoting performance and clarity in data analysis.

___

### Recommendations for Code Improvement

- **Implement Additional Checks for Edge Cases**
  - While your code handles errors proficiently, consider adding checks specifically for scenarios where no duplicates are detected during analysis. This can enhance the code's robustness by clearly communicating such results to users.
  ```python
  if duplicate_rows.empty:
      print('No duplicates found.')
  else:
      print('Duplicates found:')
      print(duplicate_rows)
  ```
  - Incorporating this logic ensures that the user is informed about the absence of duplicates, thereby improving the program's descriptive output.

- **Consistency in Style and Spacing**
  - Maintaining consistency in spacing, especially around comments, can enhance readability and make the code more approachable for future reference by yourself or others.

Overall, your code demonstrates a high degree of skill in handling configurations and working with data structures efficiently. Keep up the great work and continue refining these practices to excel further!