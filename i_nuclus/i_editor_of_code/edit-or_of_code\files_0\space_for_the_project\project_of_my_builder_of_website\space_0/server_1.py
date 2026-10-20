


















list_of_liberary_to_install = [

                            ["flask"] ,
                            
                            



]










import os


import traceback

import sys


import subprocess




try:
    
    counter_0 = 0
    
    
    while (counter_0 < len(list_of_liberary_to_install)):
    

                
        try:
        
        
            print(f"\n\n\npip install {list_of_liberary_to_install[counter_0][0]}\n\n\n")
            
            
            subprocess.check_call([sys.executable, "-m", "pip", "install", f"{list_of_liberary_to_install[counter_0][0]}"])
            
            
                
        except:
        
                
                        
            traceback.print_exc()
            
            error = traceback.format_exc()
            
            semaphore = True
            
            print(f"Erreur : {str(error)}")
            
        
        
        counter_0 += 1
        
        
    
except:

        
                
    traceback.print_exc()
    
    error = traceback.format_exc()
    
    semaphore = True
    
    print(f"Erreur : {str(error)}")
    
    
    


print("\n" * 10)












from flask import Flask, render_template_string, jsonify
import socket

app = Flask(__name__)

# دالة للتحقق من السيرفر
def check_server(host="127.0.0.1", port=5000):
    try:
        with socket.create_connection((host, port), timeout=3):
            return True
    except Exception:
        return False

# صفحة رئيسية فيها زر
@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Server Checker</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
            button { padding: 10px 20px; font-size: 16px; cursor: pointer; }
            #result { margin-top: 20px; font-weight: bold; font-size: 18px; }
        </style>
    </head>
    <body>
        <h1>🔍 Server Status Checker</h1>
        <button onclick="checkStatus()">Check Connection</button>
        <div id="result"></div>

        <script>
            function checkStatus() {
                fetch("/status")
                    .then(response => response.json())
                    .then(data => {
                        let res = document.getElementById("result");
                        if (data.status === "UP") {
                            res.innerHTML = "✅ الاتصال شغال مع " + data.server;
                            res.style.color = "green";
                        } else {
                            res.innerHTML = "❌ الاتصال غير شغال مع " + data.server;
                            res.style.color = "red";
                        }
                    })
                    .catch(err => {
                        document.getElementById("result").innerHTML = "⚠️ خطأ في التحقق";
                    });
            }
        </script>
    </body>
    </html>
    """)

# API يرجع حالة السيرفر
@app.route("/status")
def status():
    host = "127.0.0.1"   # غيرها بعنوان السيرفر
    port = 5000          # غيرها بالمنفذ
    if check_server(host, port):
        return jsonify({"server": f"{host}:{port}", "status": "UP"})
    else:
        return jsonify({"server": f"{host}:{port}", "status": "DOWN"})

if __name__ == "__main__":
    app.run(debug=True)



















