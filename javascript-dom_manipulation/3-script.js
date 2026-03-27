// On sélectionne l'élément header et l'élément qui servira de bouton (toggle_header)
const header = document.querySelector('header');
const toggleButton = document.querySelector('#toggle_header');

// On ajoute un écouteur d'événement au clic sur le bouton
toggleButton.addEventListener('click', function() {
  // On vérifie la classe actuelle et on bascule
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
});
