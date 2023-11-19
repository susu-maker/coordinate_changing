# 導入Flask模組
from flask import Flask, request, render_template

# 創建Flask應用
app = Flask(__name__)

# 定義首頁路由
@app.route('/')
def index():
    # 渲染首頁模板
    return render_template('index.html')

# 定義計算路由，接收POST請求
@app.route('/calculate', methods=['POST'])
def calculate():
    # 獲取表單中的數字
    number = request.form.get('number')
    # 轉換為浮點數
    number = float(number)
    # 計算平方
    square = number ** 2
    # 渲染結果模板，傳遞數字和平方
    return render_template('result.html', number=number, square=square)

# 運行Flask應用
if __name__ == '__main__':
    app.run(debug = True, port = 8000)