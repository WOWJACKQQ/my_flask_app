from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    avg = None
    status = ""  # 新增：用來存放傳給網頁的評語
    
    if request.method == "POST":
        C = int(request.form.get("chinese", 0))
        E = int(request.form.get("english", 0))
        M = int(request.form.get("math", 0))
        S = int(request.form.get("chemistry", 0))
        p = int(request.form.get("physics", 0))
        b = int(request.form.get("biology", 0))
        so = int(request.form.get("civics", 0))
        g = int(request.form.get("geography", 0))
        
        avg = (((C + E + M) * 4) + ((S + p + b + so + g) * 2)) // 22
        
        # ===== 第 14 週 Jinja2 邏輯串接：由 Python 決定評語內容 =====
        if avg >= 90:
            status = "excellent"  # 優秀
        elif avg >= 60:
            status = "pass"       # 及格
        else:
            status = "fail"       # 需要加強
            
        return render_template("index.html", avg_result=avg, grade_status=status)
        
    return render_template("index.html", avg_result=None, grade_status=status)

if __name__ == "__main__":
    app.run(debug=True)
if __name__ == '__main__':
    # Render 會提供環境變數 PORT，如果沒有就預設使用 10000
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)