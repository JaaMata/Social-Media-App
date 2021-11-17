(function () {
        var words = ["Hiker", "Nature Lover", "Mountaineer", "Adventurer", "Camper"],
        i = 0;
        setInterval(function(){ $('#heading-span').fadeOut(function(){
            $(this).html(words[(i = (i + 1) % words.length)]).fadeIn();
          }); }, 2500)
      })();