


















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






from flask import Flask, jsonify
import socket

app = Flask(__name__)

def check_server(host="127.0.0.1", port=5000):
    try:
        with socket.create_connection((host, port), timeout=3):
            return True
    except Exception:
        return False

@app.route("/")
def home():
    return "Welcome! Go to /status to check the server."

@app.route("/status")
def status():
    host = "127.0.0.1"   # ضع هنا IP السيرفر
    port = 5000          # ضع هنا البورت
    
    if check_server(host, port):
        return jsonify({"server": f"{host}:{port}", "status": "UP ✅"})
    else:
        return jsonify({"server": f"{host}:{port}", "status": "DOWN ❌"})

if __name__ == "__main__":
    app.run(debug=True)







