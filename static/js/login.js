let form = document.getElementsByTagName('form').item(0);
let email = document.getElementById('email')
let pwd = document.getElementById('pwd')
let check = document.getElementById('remember-me')
form.addEventListener('submit', e => {
    e.preventDefault();
    if(Validate()){
        console.log(Validate())
        form.submit()
    }
})
function Validate() {
    const estValide = _ => {
        if (!email.value.trim().match("[A-Za-z0-9]@gmail\\.com")) {
            setError(email, 'invalide email');
            return false;
        } else {
            console.log('Siuuu')
            setValide(email);}
        if (pwd.value.trim().length < 8) {
            setError(pwd, 'short password')
            return false;
        } else {
            setValide(pwd);
            console.log('CR7')
        }
        if (!check.checked) {
            setError(check);
            return false;
        } else setValide(check);
        return true;
    }
    return estValide();
}
function setError(element, message = '') {
    if (element.hasAttribute("placeholder")) element.setAttribute("placeholder", message)
    element.classList.add('error')
}
function setValide(element, message = '') {
    if (element.hasAttribute("placeholder")) element.setAttribute("placeholder", message)
    element.classList.remove('error')
}