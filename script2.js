let obj = {
    let convert = function() {
        let send_request = require('./script1.js');
        // 獲取輸入框中的數字
        var input = document.getElementById("input").value;
        console.log(input);
        // 檢查是否為有效的數字
        input = input.split(',');
        console.log(input);
        // send request
        output = new send_request(input);
        // 貼出結果
        document.getElementById("output").value = output;
    }  
};
export {obj}
