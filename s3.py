import boto3
from flask import Flask, jsonify, request, send_file

app = Flask(__name__)

def download_s3_file(bucket_name, s3_key, local_dir):
    s3= boto3.client('s3')
    try:
        s3.download_file(bucket_name, s3_key, local_dir)
        print("file downloaded successfully")
        return True
    except Exception as e:
        print(f"File download failed, error:{e}")
        return False

@app.route('/download', methods=['POST'])        
def download_file_pg():
    data = request.json
    bucket_name=data.get('bucket_name')
    s3_key = data.get('s3_key')
    local_dir=data.get('local_dir')
    try:
        res = download_s3_file(bucket_name, s3_key, local_dir)
        return 'file successsfully downloaded'
    except Exception as e:
        return f'File download failed, error:{e}'
    
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify, request, send_file

def download_s3_file(bucket_name, s3_key, local_dir):
    s3= boto3.client('s3')
    try:
        s3.download_file(bucket_name, s3_key, local_dir)
        print("file downloaded successfully")
        return True
    except Exception as e:
        print(f"File download failed, error:{e}")
        return False

@app.route('/download', methods=['GET'])        
def download_file_app():
    data = request.json
    bucket_name=data.get('bucket_name')
    s3_key = data.get('s3_key')
    local_dir=data.get('local_dir')
    try:
        res = download_s3_file(bucket_name, s3_key, local_dir)
        return 'file successsfully downloaded'
    except Exception as e:
        return f'File download failed, error:{e}'
    




    
if __name__ == '__main__':
    app.run(debug=True)

