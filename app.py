from flask import Flask, jsonify
import speedtest

app = Flask(__name__)


@app.route('/speedtest', methods=['GET'])
def speedtest_handler():
    st = speedtest.Speedtest()
    st.get_best_server()
    ping = st.results.ping
    download = st.download() / 1_000_000
    upload = st.upload() / 1_000_000
    return jsonify({'ping':ping, 'download':download, 'upload':upload})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)