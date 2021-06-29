from flask import Flask, render_template, request
import hfunct

app = Flask("Hash Converter")

def main_html(hash_md5,hash_sha1,hash_sha2):
    return render_template("mainpage.html",
    md5=hash_md5,
    sha1=hash_sha1,
    sha2=hash_sha2)

@app.route("/compute")
def compute_html():
    return render_template("compute.html")

@app.route("/result", methods=["POST"])
def result():
    itext=request.form['itext']
    hf=request.form['h_function']

    if(hf == "md5"):
        oval = hfunct.MD5(itext)
    elif(hf == "sha1"):
        oval = hfunct.SHA1(itext)
    elif(hf == "sha2"):
        oval = hfunct.SHA2(itext)

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
