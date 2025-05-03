# gold_pulse

This Python program fetches and displays real-time gold price data (e.g., price, low price, high price, chp) using a public API (GoldAPI.io). Upon each launch, it automatically retrieves the latest gold price from the internet, stores it in a local PostgreSQL database for historical tracking, and shows the updated information in a clean command-line interface. Key features include:

* API Integration: Uses requests to pull live data.
* Database Management: Stores historical prices with timestamps via PostgreSQL.
* Error Handling: Gracefully manages API failures or connectivity issues.

## Getting Started
Before running the program, edit the connect.py file to specify the connection details for your local database server PostgreSQL running on your machine. Example connect.py connection details structure:

``` txt
"DB_NAME":"postgres",
"DB_USER":"postgres",
"DB_PASS":"0000",
"DB_HOST":"localhost",
"DB_PORT":"5432" # Replace with your database port 
```
Ensure your local database server is running and accessible with the credentials provided.

### Dependencies

Install dependencies using pip in your terminal:

``` python
pip install requests
pip install psycopg2
pip install urllib
```

### Executing program

Run a test script or the main program to ensure the database connection works. The program will automatically create tables (if missing) and start fetching/storing gold price data.

* How to run the program
  Go to the location of the main.py file
  Then enter the command in cmd
  ``` 
  python main.py
  ```

## Authors

kacperpszky  

## Version History

* 0.1
    * Initial Release
