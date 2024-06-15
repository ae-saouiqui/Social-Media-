var likes=document.querySelectorAll('.fa-heart');
likes.forEach(like=>{
    like.addEventListener('click',_=>{
        var id=like.dataset.postId
        console.log(like)
        like.classList.remove('fa-regular')
        like.classList.add('fa-solid')
        like.style.color='red'
        console.log('hi',id)
        fetch('',{
            method:'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ postId: id})
        })
        .then(response => response.json()).then(data=>{
            console.log(data)
            content=like.nextElementSibling
            content.textContent=data.likes
        }).catch(
            error => {
            console.error('Error:', error);
        });
})})
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }