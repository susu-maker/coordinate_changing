define(['example'], function (require) {

    var message = "Hello!" ;
     //共用方法
    function aa(num1, num2) {
      console.log( "被共享的方法哦~" );
      console.log(num1 + num2);
    }
  
    return {
      message: message,
      bb: aa
    };
  });