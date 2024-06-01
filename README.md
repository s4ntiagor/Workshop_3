# Workshop_3
# Welcome!
Welcome to the Machine Learning Data Streaming Code Challenge. This project utilis an exercise that uses Apache Kafka to predict happiness scores across various countries using a regression machine learning model. We will work with a dataset comprised of 5 CSV files containing country-specific information. The entire workflow encompasses Exploratory Data Analysis (EDA) and Extract, Transform, Load (ETL) processes on the 5 CSV files, which include transformations, feature selection, splitting the data 70-30 for training, streaming the transformed data, making predictions, and storing the predictions in a database. We will employ the following tools to complete this project: 
- Python <img src="https://camo.githubusercontent.com/10b1bd6838c581f883d95518a336eea6613b96a55f8b29f7391108633d28c5de/68747470733a2f2f63646e2d69636f6e732d706e672e666c617469636f6e2e636f6d2f3132382f333039382f333039383039302e706e67" alt="Python" width="25"/>
- Jupyter Notebook <img src="https://camo.githubusercontent.com/b077d57822f5450d766a915fd5e97d4f7f0928a0ab6a9d65fc53315bd40b1cbb/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f7468756d622f332f33382f4a7570797465725f6c6f676f2e7376672f38383370782d4a7570797465725f6c6f676f2e7376672e706e67" alt="Jupyter Notebook" width="25"/>
- Kafka <img src="https://www.striim.com/wp-content/themes/striim2022/images/connectors_icons/white/kafka.png" alt="Apache Kafka" width="60"/>
- PostgreSQL as the relational database management system (this was chosen by personal preference). <img src="https://camo.githubusercontent.com/da57f50ec8a976bd0704ad504559e1a0ae6f70398a927b1438560c806a45b012/68747470733a2f2f63646e2d69636f6e732d706e672e666c617469636f6e2e636f6d2f3132382f353936382f353936383334322e706e67" width="25"/>
---
# Objectives
In this project, we aim to predict the happiness score of different countries using regression machine learning models based on five CSV files containing relevant data.

- EDA and ETL: We begin by performing exploratory data analysis and preparing the data for modeling. This includes cleaning, preprocessing, and selecting relevant features from the files.

- Regression Model Training: We develop a regression model using a 70-30 data split for training and testing, optimizing its performance.

- Data Streaming with Kafka: We implement a streaming architecture with Kafka to process real-time data from the EDA/ETL stage to model prediction.

- Prediction and Storage: The trained model predicts happiness scores in real time, and these predictions, along with the corresponding features, are stored in a database.

- This integrated approach leverages data analysis, machine learning, and real-time data processing to accurately predict and store happiness scores for various countries.

---
# Repository Structure
```plaintext
📦Workshop_3
├── 📂data                                # Contains CSV data files
├── 📂main                                # Contains the project's main source code
│   ├── 📄db_conn.py                      # Script for database connection
│   └── 📄Kafka.py                        # Kafka utility script
├── 📂Model
│   └── 📄random_forest_model.pkl         # Pickle file with the trained Random Forest model
├── 📂notebooks                           # Contains Jupyter notebooks for data analysis
│   └── 📄EDA.ipynb                       # Notebook for Exploratory Data Analysis
├── 📄.gitignore                          # File for ignoring files in version control
├── 📄README.md                           # This README file
├── 📄requirements.txt                    # Requirements file for installing Python dependencies
├── 📄docker-compose.yml                  # Docker Compose configuration file          
├── 📄kafka_consumer.py                   # Script for the Kafka consumer
└── 📄kafka_producer.py                   # Script for the Kafka producer
```
---
# How to run this proyect

## Step 1: Clone the Repository
```plaintext
git clone https://github.com/s4ntiagor/Workshop_3.git
```
## Step 2: Create your db_config.json
In the main folder Create a db_config.json file and copy the credentials of your database into it.
```plaintext
{
    "host": "host", 
    "user": "user",
    "password": "password",
    "database": "your_database"
}
```
## Step 3: Create your Virtual Environment
```plaintext
python -m venv venv
```
## Step 4: Start your virtual environment
```plaintext
./venv/Scripts/activate
```
## Step 5: Installs the requirements
```plaintext
pip install -r requirements.txt
```
## Step 6: Setting up Kafka
Run Docker Compose
```
docker-compose up
```

After Access Kafka Container
```
docker exec -it kafka bash
```

Create Kafka Topic
```
kafka-topics --bootstrap-server kafka --create --topic kafka-new_happy
```
This command sets up a Kafka topic that will be used for streaming happiness data.

### Step 8: Running the Streming:
Once you have set up Kafka, open two new terminals and run the following command in each terminal:
```
python kafka_consumer.py
```
```
python kafka_producer.py
```
---
And that's it! Thank you for checking this workshop, have great day!!
