let navbar = document.querySelector('nav');

document.querySelector('#menu-btn').onclick = () => {
    navbar.classList.toggle('active');
    buyItem.classList.remove('active');
}

let buyItem = document.querySelector('.buy_item_conteiner');

document.querySelector('#buy-btn').onclick = () => {
    buyItem.classList.toggle('active');
    navbar.classList.remove('active');
}

window.onscroll = () => {
    navbar.classList.remove('active');
    buyItem.classList.remove('active');
}

