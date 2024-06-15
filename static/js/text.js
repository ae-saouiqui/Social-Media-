socket=new WebSocket(`ws://${window.location.host}/ws/chatroom/`)
var message='';
socket.onmessage=function (e) {
    let data=JSON.parse(e.data)
    if(data.type==='connection_established')console.log('Data: ',data.message)
    if(data.type==='chat')message=data.message
}
btn = document.getElementsByTagName('button').item(0)
text = document.getElementsByTagName('input').item(1)
btn.onclick = _ => {
    el1 = document.createElement('div')
    el1.classList.add('message')
    el1.classList.add('sender')
    el2 = document.createElement('div')
    el2.classList.add('message-content')
    el2.textContent=message
    socket.send(JSON.stringify({
        'message':text.value
    }))
    el3 = document.createElement('img');
    el3.src = ''
    el1.appendChild(el2)
    el1.appendChild(el3);
    el = document.getElementsByClassName('message-box').item(0);
    el.appendChild(el1);
    text.value = ''
}
/*
btn1 = document.getElementsByTagName('button').item(1);
btn1.onclick = _ => {
    el1 = document.createElement('div');
    el1.classList.add('message')
    el1.classList.add('receiver')
    el2 = document.createElement('div')
    el2.classList.add('message-content')
    el2.textContent = text.value;
    el3 = document.createElement('img');
    el3.src = './pics/facebook 🔶/images/user.jpg'
    el1.appendChild(el2)
    el1.appendChild(el3);
    el = document.getElementsByClassName('message-box').item(0);
    el.appendChild(el1);
    text.value = ''
}*/
console.log(window.location.host)
