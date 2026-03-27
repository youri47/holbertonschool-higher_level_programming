// 1. On sélectionne l'élément sur lequel on va cliquer (l'ID add_item)
const addItemButton = document.querySelector('#add_item');

// 2. On sélectionne la liste où on veut ajouter l'élément (la classe my_list)
const myList = document.querySelector('.my_list');

// 3. On ajoute l'écouteur d'événement au clic
addItemButton.addEventListener('click', function() {
  // Création d'un nouvel élément <li>
  const newItem = document.createElement('li');
  
  // Ajout du texte "Item" à l'intérieur du <li>
  newItem.textContent = 'Item';
  
  // On ajoute ce nouveau <li> comme enfant de la liste <ul>
  myList.appendChild(newItem);
});
