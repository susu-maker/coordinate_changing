// 建立一個XMLHttpRequest物件
const express = require('express');
const axios = require('axios');
const cheerio = require('cheerio/lib/slim');  // 引入 cheerio 库，用于解析 HTML
const XMLHttpRequest = require('xhr2');
const { getElementsByTagName } = require('domutils');
var xhr = new XMLHttpRequest();


// 設定請求的網址和方法
xhr.open("POST", "http://gis.thl.ncku.edu.tw/coordtrans/coordtrans.aspx");

// 設定請求的header
xhr.setRequestHeader("Upgrade-Insecure-Requests", "1");
xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
xhr.setRequestHeader("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36");
xhr.setRequestHeader("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7");

// 設定請求的body
var body = {
  'BUTTON1':'轉換',
  'CoordFormat':'4',
  'CoordValue':'162615.934, 2550191.182',
  '__EVENTVALIDATION':'/wEWBwLlxrnMAwKyy4GNBwKzy4GNBwKwy4GNBwKxy4GNBwL5muahDAKMm5KEDaYjgdhgAGJ5Ne1L7rPtx+ycuzC/',
  '__VIEWSTATE':'/wEPDwUKMTA0MDk3Njk0Mg9kFgICAQ9kFgICBw8PFgIeBFRleHQFkQNUV0Q2N+e2k+e3r+W6puWdkOaomeWAvCA644CA44CA44CAIOOAgDxiPjEyMDowODoyMS4xMTQwMCwgMjM6MDM6MTAuMTE1MDA8c21hbGw+ICgxMjAuMTM5MTk4MzMzMzMzLDIzLjA1MjgwOTcyMjIyMjIpPC9zbWFsbD48L2I+PGJyPlRXRDY35LqM5bqm5YiG5bi25Z2Q5qiZ5YC8IDrjgIDjgIAg44CAPGI+MTYxNzg4Ljk4NSwgMjU1MDM5OS4yMjA8L2I+PGJyPlRXRDk3KFdHUzg0Kee2k+e3r+W6puWdkOaomeWAvCA6 IDxiPjEyMDowODo1MC4xOTIyMCwgMjM6MDM6MDMuNzk2MjQ8c21hbGw+ICgxMjAuMTQ3Mjc1NjExMzcyLDIzLjA1MTA1NDUxMDI2NjMpPC9zbWFsbD48L2I+PGJyPlRXRDk35LqM5bqm5YiG5bi25Z2Q5qiZ5YC8 IDrjgIAg44CA44CAPGI+MTYyNjE1LjkzNCwgMjU1MDE5MS4xODI8L2I+PGJyPmRkZG/sibbFSPm1K+nXL2AG/J+PInJM',
  '__VIEWSTATEGENERATOR':'F862B26F'
};

// 將body轉換為字串
var bodyString = JSON.stringify(body);
// var parser = new DOMParser();

// 發送請求
xhr.send(bodyString);

// 設定請求的回調函數
xhr.onload = function() {
  // 如果請求成功
  if (xhr.status == 200) {
    // 獲取回應的內容
    var response = xhr.responseText;
    // 在控制台打印回應的內容
    const html = response.data;  // 获取响应中的 HTML 内容
    // var htmlDoc = parser.parseFromString(response.data);
    // console.log(htmlDoc.getElementByID("Message"))

    const $ = cheerio.load(response);  // 将 HTML 文本传递给 cheerio，创建一个类似于 jQuery 的对象
    // const title = $('span[id=Message]').text();
    const title = $('span[id=Message]').children("b").eq(3).text();
    // const title = $('span[id=Message]').find("b")[3];
    // const title = $('span[id=Message]').find("b").childNodes[0];
    console.log(title);
    // 根據需要處理回應的內容
    // ...
  }
  // 如果請求失敗
  else {
    // 在控制台打印錯誤訊息
    console.error("Error: " + xhr.status);
  }
};
