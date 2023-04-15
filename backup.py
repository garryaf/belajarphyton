from flask import Flask, render_template, request
import os
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('beranda.html')

@app.route('/backup', methods=['POST'])
def backup():
    database_name = request.form['database_name']
    backup_frequency_days = request.form['backup_frequency_days']
    backup_frequency_weeks = request.form['backup_frequency_weeks']
    backup_frequency_months = request.form['backup_frequency_months']
    host_name = request.form['host_name']
    username = request.form['username']
    password = request.form['password']

    # Koneksi ke database
    mydb = mysql.connector.connect(
        host=host_name,
        user=username,
        password=password,
        database=database_name
    )

    # cek apakah koneksi berhasil
    if mydb.is_connected():
        print("Koneksi ke database berhasil!")

    # Membuat folder backup
    folder_name = database_name + "_backup"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Melakukan backup dengan menggunakan mysqldump
    backup_command = "mysqldump -u {} -p{} {} > {}/{}_backup.sql".format(username, password, database_name, folder_name, database_name)
    os.system(backup_command)

    return render_template('backup.html', folder_name=folder_name)

if __name__ == '__main__':
    app.run(debug=True)