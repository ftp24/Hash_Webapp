from flask import Flask, render_template, request
from reqpack import hfunct
import psycopg2
app = Flask("Hash Converter")

def main_html(hash_md5,hash_sha1,hash_sha2):
    return render_template("mainpage.html",
    md5=hash_md5,
    sha1=hash_sha1,
    sha2=hash_sha2)

def add_data(input, hash_md5,hash_sha1,hash_sha2):
    conn=psycopg2.connect("dbname=hash_webapp")
    cur = conn.cursor()
    cur.execute("""INSERT INTO hashes (input,MD5,SHA1,SHA2) VALUES (%s,%s,%s,%s)
    ON CONFLICT (input) DO NOTHING;""",
    (input,hash_md5,hash_sha1,hash_sha2))
    conn.commit()

@app.route("/rainbowtable")
def print_data():
    conn=psycopg2.connect("dbname=hash_webapp")
    cur = conn.cursor()
    cur.execute("SELECT * FROM hashes")
    hlist=cur.fetchall()
    return render_template('rainbowtable.html',hlist=hlist)


@app.route("/compute")
def compute_html():
    return render_template("compute.html")

@app.route("/result", methods=["POST"])
def result():
    itext=request.form['itext']
    hf=request.form['h_function']
    md5 = hfunct.MD5(itext)
    sha1 = hfunct.SHA1(itext)
    sha2 = hfunct.SHA2(itext)

    if("save" not in request.form):
        add_data(itext,md5,sha1,sha2)

    if(hf == "md5"):
        oval = md5
    elif(hf == "sha1"):
        oval = sha1
    elif(hf == "sha2"):
        oval = sha2

    return render_template("results.html",
    h_function=hf,
    otext=oval)

@app.route("/")
def main():
    password = "hello world"
    hash_md5=hfunct.MD5(password)
    hash_sha1=hfunct.SHA1(password)
    hash_sha2=hfunct.SHA2(password)
    return main_html(hash_md5,hash_sha1,hash_sha2)

if __name__ == "__main__":
    app.run()
