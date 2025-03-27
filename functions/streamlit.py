import subprocess
import json

def handler(event, context):
    try:
        subprocess.run([
            "streamlit", "run", 
            "main.py", 
            "--server.port", "8501",
            "--server.headless", "true"
        ], check=True)
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "App started successfully"})
        }
    except subprocess.CalledProcessError as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
