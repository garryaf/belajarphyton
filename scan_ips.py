from flask import Flask, render_template, request
import socket
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/scan_ips', methods=['POST'])
def scan_ips():
    subnet = request.form['subnet']
    start = int(request.form['start'])
    end = int(request.form['end'])

    # Looping untuk mengiterasi alamat IP
    active_ips = []
    for i in range(start, end+1):
        ip = subnet + str(i)
        try:
            # Mencoba membuat koneksi dengan alamat IP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((ip, 80))
            if result == 0:
                active_ips.append(ip)
            s.close()

            # Mencoba ping IP dengan protokol ICMP
            ping = subprocess.Popen(["ping", "-c", "1", ip], stdout=subprocess.PIPE)
            output = ping.communicate()[0]
            if "ttl" in str(output):
                active_ips.append(ip)

            # Mencoba koneksi ke port tertentu di alamat IP
            port = 443  # Port HTTPS
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                active_ips.append(ip)
            s.close()
        except:
            pass

    # Looping untuk mencari port yang terbuka di setiap alamat IP yang aktif
    open_ports = {}
    for ip in active_ips:
        open_ports[ip] = []
        for port in range(1, 65536):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.1)
            result = s.connect_ex((ip, port))
            if result == 0:
                open_ports[ip].append(port)
            s.close()

    return render_template('results.html', active_ips=active_ips, open_ports=open_ports)

if __name__ == '__main__':
    app.run(debug=True)