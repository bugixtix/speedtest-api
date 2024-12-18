from flask import Flask, jsonify, render_template
import speedtest
import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/speedtest', methods=['GET'])
def speedtest_handler():
    st = speedtest.Speedtest()
    st.get_best_server()
    ping = st.results.ping
    download = st.download()
    upload = st.upload()
    #Convert and return the values in Mbps
    return jsonify({'ping':ping, 'download':round(download/1e6, 2), 'upload':round(upload/1e6,2)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)