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
            print("Port 80 aktif di IP", ip)
        
        # Mencoba membuat koneksi ICMP ke alamat IP
        icmp = socket.getprotobyname("icmp")
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.settimeout(0.5)
        s.bind(('', 0))
        packet = b'ping'
        s.sendto(packet, (ip, 1))
        s.recvfrom(1024)
        s.close()
        print("ICMP aktif di IP", ip)

        # Looping untuk mencoba koneksi ke port-port tertentu
        for port in [21, 22, 23, 25, 53, 80, 110, 143, 443, 465, 587, 993, 995]:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                active_ips.append(ip)
                print(f"Port {port} aktif di IP", ip)
            s.close()
    except:
        pass

    return render_template('results.html', active_ips=active_ips)

if __name__ == '__main__':
    app.run(debug=True)