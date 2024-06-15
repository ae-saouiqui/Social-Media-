contact = document.querySelectorAll('.room');
contact.forEach(element => {
    element.onclick = _ => {
        contact.forEach(element => {
            element.style.backgroundColor = '#f67280';
        })
        element.style.backgroundColor = 'red'
        notif = element.getElementsByClassName('notification').item(0)
        notif.style.visibility = 'hidden'
    }
});
button = document.querySelector('.send-message');
text = document.getElementsByTagName('input').item(0);
button.onclick = _ => {
    if (text.value != '') {
        message = document.createElement('li');
        message.classList.add('send')
        img = document.createElement('img')
        img.src = './pics/facebook 🔶/images/us2.png';
        messageText = document.createElement('p')
        messageText.textContent = text.value;
        message.appendChild(img);
        message.appendChild(messageText)
        cont = document.getElementsByClassName('messages').item(0)
        cont.appendChild(message)
        text.value = ''
    }
}