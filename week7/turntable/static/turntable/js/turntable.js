
//turntable js
function rotateDegree(prize){
    var cat = 36; //总共10个扇形区域，每个区域约36度
    var randomDeg = Math.random() * 36 - 15; //干扰角度，每次不会都指向区域正中心
    var deg = 2160;
    if (prize == 1) {
        deg += 360-36*2 + randomDeg;
    }
    else if (prize == 2) {
        deg += 360+36*2 + randomDeg;
    }
    else if (prize == 3) {
        deg += 360-6*36 + randomDeg;
    }
    else if (prize == 4) {
        deg += 360-36 + randomDeg;
    }
    else if (prize == 5) {
        deg += 360-36*4 + randomDeg;
    }
    else if (prize == 6) {
        deg += randomDeg;
    }
    else if (prize == 7) { 
        no_prize_items = [36, 108, 180, 252];
        deg += no_prize_items[Math.floor(Math.random()*no_prize_items.length)] + randomDeg;
    } 
    return deg;
}

$(document).ready(function(){
    var oPointer = document.getElementsByTagName("img")[1];
    var oTurntable = document.getElementsByTagName("img")[2];
    
    var num = 0; //转圈结束后停留的度数
    var offOn = true; //是否正在抽奖

    // todo: Raphael, 这里你告诉我中哪个奖品 1-7
    // 1: Sports hat/cap 奔馳運動帽 （0.3%）
    // 2: Sport sunglasses 奔馳運動墨鏡 （0.3%）
    // 3: Wine stopper/opener set 奔馳開瓶器/酒塞 （0.3%）
    // 4: Smart brand silicone mug  Smart馬克杯 （0.3%）
    // 5: Metal water bottle 奔馳金屬質水壺 （0.2%）
    // 6: Golf ball, tees, towel set 奔馳高爾夫球/球釘/毛巾三件套 （0.1%）
    // 7: no prize

    var prize = prize_id; //todo: Raphael change this dynamic


    oPointer.onclick = function () {
        if (offOn) {
            oTurntable.style.transform = "rotate(0deg)";
            offOn = !offOn;
            rotating(prize);
        }
    }
    //旋转
    function rotating(prize) {
        var timer = null;
        clearInterval(timer);
        // var rdm = 360 * 3 + cat * (prize-Math.random()-1) ; //度数取决于prize
        var rdm = rotateDegree(prize);
        timer = setInterval(function () {
            oTurntable.style.transform = "rotate(" + rdm + "deg)";
            clearInterval(timer);
            setTimeout(function () {
                offOn = !offOn;
                num = rdm % 360;
    

                // // todo: remove precentage
                // if (prize == 1) { 
                //     // Sports hat/cap 奔馳運動帽 （0.3%）
                //     // todo: Raphael 这个地方你需要改一下prize.html 来配合我
                //     window.location.href = "./prize.html?name=Sportshat";
                // }
                // else if (prize == 2) { 
                //     // Sport sunglasses 奔馳運動墨鏡 （0.3%）
                //     window.location.href = "./prize.html?name=sunglasses";
                // }
                // else if (prize == 3) { 
                //     // Wine stopper/opener set 奔馳開瓶器/酒塞 （0.3%）
                //     window.location.href = "./prize.html?name=stopper";
                // }
                // else if (prize == 4) {
                //     // Smart brand silicone mug  Smart馬克杯 （0.3%）
                //     window.location.href = "./prize.html?name=stopper";
                // }
                // else if (prize == 5) {
                //     // Metal water bottle 奔馳金屬質水壺 （0.2%）
                //     window.location.href = "./prize.html?name=stopper";
                // }
                // else if (prize == 6) {
                //     // Golf ball, tees, towel set 奔馳高爾夫球/球釘/毛巾三件套 （0.1%）
                //     window.location.href = "./prize.html?name=golf";
                // }
                // else if (prize == 7) { 
                //     //未中奖
                //     window.location.href = "./no_prize.html";
                // }
            }, 4000);
        }, 30);
    }
    $(function(){
        $('#reward').submit();
    });
})

