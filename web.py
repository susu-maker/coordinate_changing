# 導入Flask模組
from flask import Flask, request, render_template, jsonify,request,make_response
from flask_socketio import SocketIO
from flask_cors import CORS
import change_coordinate as cc
import re
# 創建Flask應用
app = Flask(__name__)

socketio = SocketIO(app, cors_allowd_origins = '*')
# 定義首頁路由
@app.route('/', methods = ['GET','POST','OPTIONS'])

def index():
#     # 渲染首頁模板
    
#     method = request.method

#     res = make_response(jsonify(token=123456, gender=0, method = method))  # 设置响应体
#     res.status = '200'  # 设置状态码
#     res.headers['Access-Control-Allow-Origin'] = "*"  # 设置允许跨域
#     res.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
#     return res
    
    return render_template('coordinate.html')

@app.route('/change_coordinate', methods = ['GET','POST','OPTIONS'])
def change_coordinate():
    if request.method == 'POST':
        print("success")
        # coor = request.values.get('CoordValue').split(",")
        coor = re.split(r'[;,\s]\s*', request.values.get('CoordValue'))
        coor = [float(i) for i in coor]
        print(coor)
        if(coor[0]>10000):
            print('to wgs84')
            if(coor[1]>coor[0]):
                new_coor = cc.get_wgs84(coor[0], coor[1])
                print(new_coor)
                data = { 
                    "Modules" : 15, 
                    "Subject" : "Data Structures and Algorithms",
                    "coor" :  new_coor,
                } 
                return jsonify(data) 
            else:
                new_coor = cc.get_wgs84(coor[1], coor[0])
                print(new_coor)
                data = { 
                    "Modules" : 15, 
                    "Subject" : "Data Structures and Algorithms",
                    "coor" :  new_coor,
                } 
                return jsonify(data)
        else:
            print("to twd97")
            if(coor[0]>coor[1]):
                new_coor = cc.get_twd97(coor[0], coor[1])
                print(new_coor)
                data = { 
                    "Modules" : 15, 
                    "Subject" : "Data Structures and Algorithms",
                    "coor" :  new_coor,
                } 
                return jsonify(data) 
            else:
                new_coor = cc.get_twd97(coor[1], coor[0])
                print(new_coor)
                data = { 
                    "Modules" : 15, 
                    "Subject" : "Data Structures and Algorithms",
                    "coor" :  new_coor,
                } 
                return jsonify(data) 
    else: 
        print('else')
        print(request.method)
        data = { 
            "Modules" : 15, 
            "Subject" : "Data Structures and Algorithms", 
        } 
        return jsonify(data)
    # return 100
    # return render_template('coordinate.html')
# 定義計算路由，接收POST請求
# @app.route('/calculate', methods=['POST'])
# def calculate():
#     return render_template('coordinate.html')
#     # 獲取表單中的數字
#     number = request.form.get('number')
#     # 轉換為浮點數
#     number = float(number)
#     # 計算平方
#     square = number ** 2
#     # 渲染結果模板，傳遞數字和平方
#     return render_template('result.html', number=number, square=square)

# 運行Flask應用
if __name__ == '__main__':
    app.run(debug = True, port = 8000)
    CORS(app)
    