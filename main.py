from flask import Flask, render_template
from pyngrok import ngrok, conf
import datafunctions, qrcode

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('mainpage.html', func=datafunctions)


@app.route('/qr')
def qr():
    return render_template('qrcodepage.html')


conf.get_default().auth_token = datafunctions.getAuthtoken()
datafunctions.initialize()
tunnelURL = str(ngrok.connect(proto='http', addr='localhost:1337').public_url)
qrcovid = qrcode.make(tunnelURL)
qrcovid.save(str('static/qrcovid.png'))
print('YOUR QR IS HERE: ', str(tunnelURL + '/qr'))
app.run(port='1337')
