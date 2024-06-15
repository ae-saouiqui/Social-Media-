let form = document.getElementsByTagName('form').item(0);
let fname = document.getElementById('firstname')
let sname = document.getElementById('secondname')
let email = document.getElementById('email')
let pwd1 = document.getElementById('pwd1')
let pwd2 = document.getElementById('pwd2')
let bd = document.getElementById('birthday')
let phone = document.getElementById('phone')
let check = document.getElementById('confirm')
check.onclick = _ => {
    console.log(check.checked)
}
form.addEventListener('submit', e => {
    e.preventDefault();
    Validate();
})
console.log(typeof check.value)
function Validate() {
    let fnamevalue = fname.value.trim()
    let snamevalue = sname.value.trim()
    let emailvalue = email.value.trim()
    let pwd1value = pwd1.value.trim()
    let pwd2value = pwd2.value.trim()
    let bdvalue = bd.value.trim()
    let phonevalue = phone.value.trim()

    let estValide = _ => {
        if (fnamevalue === '') {
            setError(fname, 'fill this field');
            return false;
        }
        else setValide(fname, 'First Name');
        if (snamevalue === '') {
            setError(sname, 'fill this field');
            return false;
        }
        else setValide(sname, 'Last Name');
        if (pwd1value === '') {
            setError(pwd1, 'fill this field');
            return false
        }else if(pwd1value.length<8){
            setError(pwd1,'password must be >8')
            return  false
        }
        else setValide(pwd1, 'Password');
        if (pwd2value === '') {
            setError(pwd2, 'fill this field');
            return false;
        }
        else setValide(pwd2, 'Re-confirm Password');
        if (pwd2value !== pwd1value) {
            setError(pwd2, 'unmatching password');
            return false
        }
        else {
            setValide(pwd1, 'Password');
            setValide(pwd2, 'Re-confirm Password')
        }
        if (phonevalue === '') {
            setError(phone, 'fill this field')
            return false;
        }
        else if (!phonevalue.match("[0-9]{10}")) {
            setError(phone, 'incorrect phonenumber');
            return false
        }
        else { setValide(phone, '+212********') }
        if (bdvalue === '') {
            setError(bd, 'fill this field')
            return false
        }
        else setValide(bd, 'mm/dd/yyyy')
        if (!check.checked) {
            setCheckError(check);
            return false
        } else setCheckValide(check);
        return true;
    }
    if (estValide()) form.submit();
}
function setError(element, message) {
    if (element.hasAttribute("placeholder")) {
        element.setAttribute("placeholder", message)
        element.classList.add('error')
    }
}
function setCheckError(element) {
    const el = element.nextElementSibling
    el.innerText = "You have to confirm";
    el.classList.add('check-error')
}
function setCheckValide(element) {
    el = element.nextElementSibling
    el.innerText = 'Confirm'
    el.classList.remove('check-error')
}
function setValide(element, message = '') {
    element.setAttribute("placeholder", message)
    element.classList.remove("error")
}