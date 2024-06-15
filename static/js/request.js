btn=document.querySelectorAll('.add')
btn.forEach(icon=>{
    icon.onclick=_=>{
        let req=icon.previousElementSibling
        if(icon.classList.contains('fa-user-plus')){
            req.setAttribute('value','send')
        icon.classList.remove('fa-user-plus')
        icon.classList.add('fa-user-check')}
        else{
            req.setAttribute('value','decline')
        icon.classList.remove('fa-user-check')
                   icon.classList.add('fa-user-plus')
        }

        form=icon.parentElement.parentElement.parentElement
        form.submit()

    }
})