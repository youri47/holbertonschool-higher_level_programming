// 1. On sélectionne l'élément qui sert de bouton (ID update_header)
const updateButton = document.querySelector('#update_header');

// 2. On sélectionne l'élément dont on veut changer le texte (le header)
const header = document.querySelector('header');

// 3. On écoute le clic et on modifie le texte
updateButton.addEventListener('click', function() {
    header.textContent = 'New Header!!!';
});
