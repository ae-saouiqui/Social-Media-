const textarea = document
    .querySelector('#post-desc');
const postBtn = document
    .querySelector('.post-btn');

document.body.style.overflowX = 'none';

textarea.addEventListener("input", () => {
    if (textarea.value != '')
        postBtn.disabled = false;
    else
        postBtn.disabled = true;
})
backBtn.addEventListener('click', () => {
    document.querySelector('.wrapper');
    createPostSection.style.display = 'block';
})