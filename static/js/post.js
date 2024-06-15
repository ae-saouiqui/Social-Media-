form1 = document.getElementById('post')
text = document.getElementsByClassName('text-area').item(0)
send = document.getElementsByClassName('create').item(0)
send.onclick = _ => {
    if (text.value !== '') {
        form1.submit();
    }
}