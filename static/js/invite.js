let btns = document.querySelectorAll('.btn')
btns.forEach(btn => {
    accept = btn.getElementsByClassName('fa-check').item(0)
    reject = btn.getElementsByClassName('fa-xmark').item(0)
    let response = btn.getElementsByClassName('add').item(0)



    accept.onclick = _ => {
        response.setAttribute('value', 'yes')
        let el = btn.parentElement.parentElement
        let form = el.parentElement
        el.style.display = 'none'
        form.submit()
    }
    reject.onclick = _ => {
        response.setAttribute('value', 'no')
        let el = btn.parentElement.parentElement
        let form = el.parentElement
        el.style.display = 'none'
        form.submit()
    }
})