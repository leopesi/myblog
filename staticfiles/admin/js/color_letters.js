function letras(i) {

      document.getElementsByTagName('span')[i].onmouseover = function() {
    mouseOver()
    }

    function mouseOver() {
      document.getElementsByTagName('span')[i].style.color = getRandomColor();
    }

    function getRandomColor() {

        var letters = "0123456789ABCDEF";
        var color = "#";
        for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    }
    var newColor = getRandomColor(); // #E943F0

    }
