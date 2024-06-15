form=document.getElementById('search')
search=document.getElementById('search-friends')
btn=document.getElementsByClassName('fa-search').item(0)

btn.onclick=_=>{
    if(search.value!=='')form.submit();
}