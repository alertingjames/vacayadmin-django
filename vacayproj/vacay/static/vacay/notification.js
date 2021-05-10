var me_email = document.getElementById("me_email").value;
var ul = document.getElementById("list");
var keys = [];
me_email = me_email.replace(".com","").replace(".","ddoott");
var starCountRef = firebase.database().ref('notification/' + me_email);
starCountRef.on('child_added', function(snapshot) {
  var key = snapshot.val();
  if (key){
    var key2 = getChildObj(key);
    var sender_name = key2.senderName
//    window.alert(key2.message);
    var li = document.createElement("div");
    li.style.color = 'black';
    li.style.fontSize = '16';
    li.style.maxWidth = "auto";
    li.style.width = "auto";
    li.innerHTML = "<label style='font-size:18px; font-weight:600;'>" + sender_name + "</label>" + "<br>" + "<label style='font-size:15px; font-weight:300; padding-left:10px;'>" + key2.msg + "</label>" + "<br>" + "<label style='color:red; width:95%; text-align:right; font-size:13px; font-weight:300;'>Click here</label>";
    li.style.textAlign = 'left';
    var ul2 = document.createElement("div");
    var img = document.createElement("img");
    img.src = key2.senderPhoto;
    ul2.appendChild(img);
    ul2.append(li);
    ul2.addEventListener('click', function (event) {
       var context = {
            'friend_email': key2.sender,
            'friend_name': key2.senderName,
            'friend_photo': key2.senderPhoto
       }
       post('/chat_page', context);
    });
    ul.appendChild(ul2);
  }else {
      var lii = document.createElement("div");
      lii.style.color = 'white';
      lii.style.fontSize = '16';
      lii.style.textAlign = 'center';
      lii.innerHTML = "No message ...";
      ul.append(lii);
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

function post(path, params, method) {
   method = method || "post"; // Set method to post by default if not specified.

   // The rest of this code assumes you are not using a library.
   // It can be made less wordy if you use one.
   var form = document.createElement("form");
   form.setAttribute("method", method);
   form.setAttribute("action", path);

   for(var key in params) {
      if(params.hasOwnProperty(key)) {
          var hiddenField = document.createElement("input");
          hiddenField.setAttribute("type", "hidden");
          hiddenField.setAttribute("name", key);
          hiddenField.setAttribute("value", params[key]);

          form.appendChild(hiddenField);
      }
   }

   var hiddenField1 = document.createElement("input");
   hiddenField1.setAttribute("type", "hidden");
   hiddenField1.setAttribute("name", 'csrfmiddlewaretoken');
   hiddenField1.setAttribute("value", getCookie('csrftoken'));
   form.appendChild(hiddenField1);

   document.body.appendChild(form);
   form.submit();
}

function getCookie(name) {
    console.log('getCookie');
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                    }
            }
    }
    console.log('cookie:' + cookieValue);
    return cookieValue;
}











