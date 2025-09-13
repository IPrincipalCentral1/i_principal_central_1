














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


from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# صفحة HTML مدمجة
html_page = """
<!DOCTYPE html>
<html lang="ar">
<head>
  <meta charset="UTF-8">
  <title>اتصال بالسيرفر</title>
</head>
<body>
  <h2>اختبار الاتصال بالسيرفر</h2>
  <button onclick="checkServer()">افحص الإتصال</button>
  <p id="result"></p>

  <script>
    async function checkServer() {
      try {
        let response = await fetch("/check");
        if (response.ok) {
          let data = await response.json();
          document.getElementById("result").innerText = data.message;
        } else {
          document.getElementById("result").innerText = "لا يوجد إتصال (status " + response.status + ")";
        }
      } catch (error) {
        document.getElementById("result").innerText = "لا يوجد إتصال (خطأ في الشبكة)";
        console.error(error);
      }
    }
  </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(html_page)

@app.route("/check", methods=["GET"])
def check_connection():
    return jsonify({"status": "success", "message": "نجح الإتصال"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)









