var me_email = document.getElementById("me_email").value;
createjs.Sound.registerSound("/static/vacay/sound/notification.mp3", "x");
navigator.vibrate = navigator.vibrate || navigator.webkitVibrate || navigator.mozVibrate || navigator.msVibrate;

var keys = [];
me_email = me_email.replace(".com","").replace(".","ddoott");
var starCountRef = firebase.database().ref('notification/' + me_email);
starCountRef.on('child_added', function(snapshot) {
  var key = snapshot.val();
  keys.push(key);
  if(keys.length == 1){
      createjs.Sound.play("x");
//      if(confirm("Hi, You have message!\nWould you contact them?")){
//         window.location.href = "/get_notifications";
//      }
      document.getElementById("alert").style.display = 'block';
      if (navigator.vibrate) {
	      // vibration API supported
	      navigator.vibrate(500);
      }else {
          window.navigator.vibrate(500); // vibrate for 500ms
      }
//       window.navigator.vibrate(500); // vibrate for 500ms
//     window.alert("Hi, You have messsage!");
  }
});

function getChildObj (obj) {
    var obj2;
    for (var p in obj) {
        if (obj.hasOwnProperty(p)) {
            obj2 = obj[p];
        }
    }
    return obj2;
}


//setTimeout(function () {
//
//}, 10000)